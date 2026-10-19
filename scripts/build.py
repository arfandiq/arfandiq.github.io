#!/usr/bin/env python3
"""Build a dependency-free GitHub Pages site and discover original photo files."""
import argparse, html, json, re, shutil
from pathlib import Path
from urllib.parse import quote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
GROUPS = ('projects', 'work', 'internship', 'organization', 'awards', 'articles')
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.webp', '.avif', '.gif'}

def load(name):
    try:
        return json.loads((ROOT / 'data' / (name + '.json')).read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f'data/{name}.json: {exc}') from exc

def natural_key(path):
    return [int(x) if x.isdigit() else x.lower() for x in re.split(r'(\d+)', path.name)]

def photos(folder, fallback):
    relative = Path(folder)
    if relative.is_absolute() or '..' in relative.parts or not folder.startswith('assets/photos/'):
        raise ValueError(f'photoFolder must be inside assets/photos/: {folder}')
    directory = ROOT / relative
    if not directory.exists():
        directory.mkdir(parents=True)
        (directory / '.gitkeep').touch()
    if not directory.resolve().is_relative_to((ROOT / 'assets/photos').resolve()):
        raise ValueError(f'Photo directory escapes assets/photos: {folder}')
    metadata_path = directory / 'metadata.json'
    metadata = json.loads(metadata_path.read_text(encoding='utf-8')) if metadata_path.exists() else {}
    result = []
    for image in sorted(directory.iterdir(), key=natural_key):
        if image.suffix.lower() not in IMAGE_EXTENSIONS or not image.is_file():
            continue
        if image.is_symlink():
            raise ValueError(f'Symlink photos are not supported: {image}')
        info = metadata.get(image.name, {})
        result.append({'src': quote(image.relative_to(ROOT).as_posix(), safe='/'),
                       'alt': info.get('alt', fallback), 'caption': info.get('caption', '')})
    return result

def validate(content):
    ids = set()
    for group in GROUPS:
        if not isinstance(content[group], list):
            raise ValueError(f'data/{group}.json must be an array')
        for entry in content[group]:
            for field in ('id', 'title', 'photoFolder'):
                if not isinstance(entry.get(field), str) or not entry[field].strip():
                    raise ValueError(f'{group}: missing {field}')
            if not re.fullmatch(r'[a-z0-9][a-z0-9-]*', entry['id']):
                raise ValueError(f'Use a lowercase id with hyphens: {entry["id"]}')
            if entry['id'] in ids:
                raise ValueError(f'Duplicate id: {entry["id"]}')
            ids.add(entry['id'])
            if group != 'articles':
                for field in ('date','summary','paragraphs','bullets'):
                    if field not in entry:
                        raise ValueError(f'{group}/{entry["id"]}: missing {field}')
                for field in ('paragraphs','bullets'):
                    if not isinstance(entry[field], list) or not all(isinstance(s,str) for s in entry[field]):
                        raise ValueError(f'{entry["id"]}: {field} must be a list of text')
                if not entry['paragraphs'] and not entry['bullets']:
                    raise ValueError(f'{entry["id"]}: complete detail text is required')
            else:
                url = urlsplit(entry.get('url', ''))
                if url.scheme != 'https' or not url.hostname:
                    raise ValueError(f'Article {entry["id"]} needs an original HTTPS URL')
    profile = content['profile']
    for link in [*profile.get('socials', []), *([profile['anonymousMessage']] if profile.get('anonymousMessage') else [])]:
        url = urlsplit(link.get('url', ''))
        if url.scheme != 'https' or not url.hostname:
            raise ValueError('Social and anonymous-message links must be valid HTTPS URLs')
    featured = [p for p in content['projects'] if p.get('featured')]
    if len(featured) != 3:
        raise ValueError('Select exactly three projects using featured: true')
    text = json.dumps(content, ensure_ascii=False)
    if '\u2014' in text:
        raise ValueError('An em dash was found. Replace it with a normal hyphen or punctuation.')

def cv_document(content):
    e = html.escape
    profile = content['profile']; edu = profile['education']
    parts = [f'<header><p>ARFANDIQA</p><h1>{e(profile["name"])}</h1><p>{e(profile["location"])} · <a href="mailto:{e(profile["email"])}">{e(profile["email"])}</a></p><p><a href="{e(profile["linkedin"])}">LinkedIn</a> · <a href="{e(profile["github"])}">GitHub</a></p><button onclick="window.print()">Print / Save PDF</button> <a href="index.html">Back to website</a></header>',
        '<h2>Professional Summary</h2><p>'+e(profile['summary'])+'</p>',
        '<h2>Skills</h2><p>'+e(' · '.join(profile['skills']))+'</p>',
        '<h2>Education</h2><h3>'+e(edu['title'])+'</h3><p>'+e(edu['org']+' | '+edu['date']+' | '+edu['location'])+'</p><p>'+e(edu['credential']+' · '+edu['status'])+'</p><p>'+e(edu['description'])+'</p>']
    for group, title in [('internship','Internships'),('work','Work Experience'),('projects','Projects'),('awards','Achievements'),('organization','Organization Experience')]:
        parts.append('<section><h2>'+title+'</h2>')
        for entry in content[group]:
            parts.append('<article><h3>'+e(entry['title'])+'</h3><p class="meta">'+e(' | '.join(x for x in [entry.get('org'), entry['date'], entry.get('location')] if x))+'</p>')
            parts.extend('<p>'+e(p)+'</p>' for p in entry['paragraphs'])
            if entry['bullets']:
                parts.append('<ul>'+''.join('<li>'+e(b)+'</li>' for b in entry['bullets'])+'</ul>')
            parts.append('</article>')
        parts.append('</section>')
    parts.append('<h2>Tools</h2><p>'+e(' · '.join(profile['tools']))+'</p>')
    return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>CV | ARFANDIQA</title><style>body{max-width:850px;margin:40px auto;padding:0 24px;color:#0f2744;background:#f8fafc;font:15px/1.7 system-ui}h1{font-size:36px;line-height:1.2}h2{margin-top:38px;border-bottom:2px solid #f97316;padding-bottom:8px}h3{font-size:17px;margin-bottom:5px}a{color:#991b1b}article{margin-bottom:27px}.meta{font-size:13px;color:#43576b}button{padding:9px 14px;background:#0f2744;color:#fff;border:0;cursor:pointer}li{margin:8px 0}@media print{body{margin:0;max-width:none;padding:0;font-size:10pt;background:white}button,header>a{display:none}h2,h3{break-after:avoid}p,li{orphans:3;widows:3}@page{margin:18mm}}</style></head><body>'+''.join(parts)+'</body></html>'

def build(output=None):
    content = {group: load(group) for group in GROUPS}
    content['profile'] = load('profile')
    validate(content)
    for group in GROUPS:
        for entry in content[group]:
            entry['photos'] = photos(entry['photoFolder'], entry['title'])
    p = content['profile']
    content['profilePhotos'] = photos(p['profilePhotoFolder'], p['name'])
    content['designPhotos'] = photos(p['designPhotoFolder'], 'Original design by '+p['name'])
    content['educationPhotos'] = photos(p['education']['photoFolder'], p['education']['org'])
    generated = ROOT / 'assets/js/content.js'
    generated.write_text('// Generated by scripts/build.py. Edit data/*.json instead.\nwindow.CONTENT = '+json.dumps(content, ensure_ascii=False, indent=2).replace('</','<\\/')+';\n',encoding='utf-8')
    (ROOT / 'cv.html').write_text(cv_document(content),encoding='utf-8')
    if output:
        dest = (ROOT / output).resolve()
        if dest != ROOT / '_site':
            raise ValueError('The deployment output must be _site')
        if dest.exists():
            shutil.rmtree(dest)
        dest.mkdir()
        for filename in ('index.html','cv.html','.nojekyll'):
            shutil.copy2(ROOT / filename, dest / filename)
        shutil.copytree(ROOT / 'assets/css', dest / 'assets/css')
        shutil.copytree(ROOT / 'assets/js', dest / 'assets/js')
        for folder in (ROOT / 'assets/photos').rglob('*'):
            if folder.is_file() and folder.suffix.lower() in IMAGE_EXTENSIONS:
                target = dest / folder.relative_to(ROOT)
                target.parent.mkdir(parents=True,exist_ok=True)
                shutil.copy2(folder,target)
    return content

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', help='Use _site for deployment output')
    args=parser.parse_args()
    try:
        c=build(args.output)
        print(f'Built ARFANDIQA: {sum(len(c[g]) for g in GROUPS)} entries; '+str(sum(len(e['photos']) for g in GROUPS for e in c[g])+len(c['profilePhotos'])+len(c['designPhotos'])+len(c['educationPhotos']))+' photos.')
    except (ValueError,OSError) as exc:
        parser.exit(1, f'Build failed: {exc}\n')
