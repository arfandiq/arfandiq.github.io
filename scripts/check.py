#!/usr/bin/env python3
"""Validate data, built local links, generated JS, and the deployment boundary."""
import json, subprocess, shutil
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
from build import ROOT, GROUPS, load, validate

class Links(HTMLParser):
    def __init__(self): super().__init__(); self.links=[]; self.ids=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        for key in ('src','href'):
            if key in a:self.links.append(a[key])

def main():
    c={g:load(g) for g in GROUPS};c['profile']=load('profile');validate(c)
    site=ROOT/'_site'
    if not site.exists():raise ValueError('Run python3 scripts/build.py --output _site first')
    for name in ('index.html','cv.html'):
        page=site/name;text=page.read_text(encoding='utf-8');parser=Links();parser.feed(text)
        if len(parser.ids)!=len(set(parser.ids)):raise ValueError(f'Duplicate HTML ids in {name}')
        for link in parser.links:
            url=urlsplit(link)
            if url.scheme or url.netloc or not url.path:continue
            if url.path.startswith('/'):raise ValueError(f'Root-relative path breaks project Pages: {link}')
            target=(page.parent/unquote(url.path)).resolve()
            if not target.is_relative_to(site) or not target.exists():raise ValueError(f'Broken local link: {name} -> {link}')
        if '\u2014' in text:raise ValueError(f'Em dash in {name}')
        if 'tel:' in text or '081271524551' in text:raise ValueError(f'Telephone number in {name}')
    for forbidden in ('data','docs','scripts','.github','README.md'):
        if (site/forbidden).exists():raise ValueError(f'Unexpected source material in deployment: {forbidden}')
    if shutil.which('node'):
        for filename in ('site.js','content.js'):
            subprocess.run(['node','--check',str(site/'assets/js'/filename)],check=True)
    else:print('Node not installed; JavaScript syntax check skipped.')
    print('PASS: content, local asset links, project-site relative paths, generated syntax, no phone, and deployment contents.')

if __name__=='__main__':main()
