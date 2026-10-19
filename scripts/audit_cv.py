#!/usr/bin/env python3
"""One-time source audit. Intentional future content edits can change this baseline."""
import json,re
from build import ROOT, load
norm=lambda s:re.sub(r'\s+',' ',s).strip()
raw=(ROOT/'docs/source-cv-text.txt').read_text().replace('\f','\n')
raw=re.sub(r'-\n(?=\w)','-',raw)
headings=['Professional Summary','Skills','Education','Internships','Work Experience','Projects','Achievements','Organization Experience']
sections={}
for i,h in enumerate(headings):
    start=re.search(r'(?m)^'+re.escape(h)+r'$',raw).end()
    end=re.search(r'(?m)^'+re.escape(headings[i+1])+r'$',raw).start() if i+1<len(headings) else len(raw)
    sections[h]=raw[start:end].strip()
count=0;bullets=0
for group,heading in {'projects':'Projects','work':'Work Experience','internship':'Internships','organization':'Organization Experience','awards':'Achievements'}.items():
    entries=load(group);section=sections[heading]
    matches=[re.search(r'(?m)^'+re.escape(e['title']).replace(r'\ ',r'\s+')+r'\s*$',section) for e in entries]
    assert all(matches),f'One or more entry names differ in {group}'
    for i,(entry,match) in enumerate(zip(entries,matches)):
        body=section[match.end():matches[i+1].start() if i+1<len(matches) else len(section)]
        body=re.sub(r'(?m)^\d{2}/\d{4}(?: – (?:\d{2}/\d{4}|Present))?\s*$','',body)
        body=re.sub(r'(?m)^Surabaya\s*$','',body)
        text=norm(body)
        if entry.get('org'):
            assert text.startswith(entry['org']),entry['id']+' organization mismatch'
            text=text[len(entry['org']):].strip()
        expected=norm(text.replace('•',' '))
        actual=norm(' '.join(entry['paragraphs']+entry['bullets']))
        assert actual==expected,entry['id']+' detail does not match the full source CV'
        assert len(entry['bullets'])==text.count('•'),entry['id']+' missing bullet'
        count+=1;bullets+=len(entry['bullets'])
p=load('profile')
assert p['summary']==norm(sections['Professional Summary'])
assert set(p['skills'])==set(s.strip() for s in sections['Skills'].splitlines() if s.strip())
education=re.sub(r'(?m)^\d{2}/\d{4}(?: – (?:\d{2}/\d{4}|Present))?\s*$','',sections['Education'])
education=re.sub(r'(?m)^Surabaya\s*$','',education)
assert norm(education)==norm(p['education']['title']+' '+p['education']['org']+' '+p['education']['description'])
print(f'PASS: {count} complete entries, {bullets} responsibility bullets, summary, and skills match the CV. PDF line wraps normalized; original wording retained.')
