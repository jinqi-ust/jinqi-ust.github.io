#!/usr/bin/env python3
"""Build a self-contained static academic website. Requires Python 3.10+ only."""
from pathlib import Path
from html import escape
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
a = json.loads((ROOT / 'data/academic.json').read_text(encoding='utf-8'))
p = json.loads((ROOT / 'data/people.json').read_text(encoding='utf-8'))
e = lambda value: escape(str(value), quote=True)

def heading(kicker, title, identifier, aside=''):
    return f'<div class="section-heading"><div><p class="eyebrow">{e(kicker)}</p><h2 id="{e(identifier)}">{e(title)}</h2></div>{aside}</div>'

def section(identifier, content, classes=''):
    return f'<section id="{identifier}" class="section {classes}" aria-labelledby="{identifier}-title"><div class="content-width">{content}</div></section>'

def disclosure(title, content):
    return f'<details class="disclosure"><summary>{e(title)}</summary>{content}</details>'

def subheading(title, count=None):
    return f'<div class="subheading"><h3>{e(title)}</h3>' + (f'<span class="count">{count}</span>' if count is not None else '') + '</div>'

def paper_list(items, offset=0):
    output = '<ol class="publication-list">'
    for i, paper in enumerate(items, offset + 1):
        student_authors = set(paper.get('student_postdoc_authors', []))
        author_names = paper['authors'].split(', ')
        assert student_authors.issubset(author_names), f'Unknown marked author: {paper["title"]}'
        author_parts = []
        for name in author_names:
            author = f'<strong>{e(name)}</strong>' if name == 'Jin Qi' else e(name)
            if name in student_authors:
                author += '<sup class="author-marker" title="PhD student or post-doc at the time of initiation" aria-label="PhD student or post-doc at the time of initiation">*</sup>'
            author_parts.append(author)
        authors = ', '.join(author_parts)
        alphabetical = '<sup class="alphabetical-marker" title="Alphabetical order, equal contribution" aria-label="Alphabetical order, equal contribution">†</sup>' if paper.get('alphabetical_order') else ''
        output += f'<li class="publication"><span class="paper-number"><span aria-hidden="true">{i:02d}</span>{alphabetical}</span><div><h3>{e(paper["title"])}</h3><p class="authors">{authors}</p><p class="venue">{e(paper["citation"])}</p></div></li>'
    return output + '</ol>'

published = [x for x in a['publications'] if x['kind'] != 'working']
working = [x for x in a['publications'] if x['kind'] == 'working']
publications = heading('Publications', 'Selected & recent work', 'publications-title', '<a class="text-link" href="https://scholar.google.com/citations?hl=en&amp;user=x7VfQHIAAAAJ">Google Scholar ↗</a>')
publications += '<p class="publication-legend"><span><sup>†</sup> Alphabetical order, equal contribution.</span><span><sup>*</sup> PhD student or post-doc at the time of initiation.</span></p>'
publications += paper_list(published[:7])
publications += disclosure(f'More publications ({len(published)-7})', paper_list(published[7:], 7))
publications += disclosure(f'Working papers & manuscripts under review ({len(working)})', paper_list(working))
publications += disclosure('Media', paper_list(a['media']))
publications += f'<p class="section-note" style="margin-top:20px">Publication details and manuscript statuses follow the {e(a["as_of"])} CV.</p>'

def people_cards(people, extra=''):
    output = f'<div class="people-grid {extra}">'
    for person in people:
        note = f'<p class="person-note">{e(person["note"])}</p>' if person.get('note') else ''
        output += f'<article class="person"><h4>{e(person["name"])}</h4><p class="person-type">{e(person["role"])} · {e(person["period"])}</p>{note}</article>'
    return output + '</div>'

def alumni_table(people, label):
    output = f'<table class="alumni-table" aria-label="{e(label)}"><thead><tr><th scope="col">Name</th><th scope="col">Years</th><th scope="col">Position as of {e(p["as_of"])}</th></tr></thead><tbody>'
    for person in people:
        note = f'<span class="table-note">{e(person["note"])}</span>' if person.get('note') else ''
        output += f'<tr><td>{e(person["name"])}{note}</td><td>{e(person["period"])}</td><td>{e(person["position"])}</td></tr>'
    return output + '</tbody></table>'

group = heading('People', 'Research group', 'group-title', f'<p>Students, postdoctoral fellows &amp; alumni <br>As of {e(p["as_of"])}</p>')
group += f'<div class="group-intro"><span><strong>{len(p["students"])}</strong> current students</span><span><strong>{len(p["postdocs"])}</strong> postdoctoral fellows</span></div>'
phd = [x for x in p['students'] if x['role'] == 'PhD student']
mphil = [x for x in p['students'] if x['role'] == 'MPhil student']
group += subheading('PhD students', len(phd)) + people_cards(phd)
group += subheading('MPhil students', len(mphil)) + people_cards(mphil, 'postdoc-grid')
group += subheading('Postdoctoral fellows', len(p['postdocs'])) + people_cards(p['postdocs'], 'postdoc-grid')
group += subheading('PhD graduates', len(p['phd_alumni'])) + alumni_table(p['phd_alumni'], 'PhD graduates and positions')
group += subheading('MPhil graduates', len(p['mphil_alumni']))
group += '<div class="compact-people">' + ''.join(f'<p>{e(x["name"])}<span>MPhil · {e(x["period"])}</span></p>' for x in p['mphil_alumni']) + '</div>'
group += subheading('Former postdoctoral fellows', len(p['former_postdocs'])) + alumni_table(p['former_postdocs'], 'Former postdoctoral fellows and positions')

def timeline(items):
    return '<ul class="timeline">' + ''.join(f'<li><span class="date">{e(x["date"])}</span><h3>{e(x["title"])}</h3><p>{e(x["detail"])}</p></li>' for x in items) + '</ul>'

background = heading('About', 'Academic experience', 'background-title')
background += '<div class="two-columns"><div>' + subheading('Appointments') + timeline(a['appointments']) + '</div><div>' + subheading('Education') + timeline(a['education']) + '</div></div>'
background += disclosure('Affiliations', timeline(a['affiliations']))

def grant_list(items):
    return '<ul class="grant-list">' + ''.join(f'<li><span class="grant-date">{e(x["period"])}</span><div><p class="grant-title">{e(x["title"])}</p><p class="grant-meta">{e(x["funder"])} · {e(x["role"])}</p></div></li>' for x in items) + '</ul>'

grants = heading('Funding', 'Research grants', 'grants-title')
grants += grant_list(a['grants'][:5])
grants += disclosure('Further grants & collaborative projects', grant_list(a['grants'][5:]))

teaching = heading('Teaching', 'Courses at HKUST', 'teaching-title')
teaching += '<ul class="course-list">' + ''.join(f'<li><span class="course-code">{e(x["code"])}</span><span class="course-name">{e(x["name"])}</span><span class="course-dates">{e(x["period"])}</span></li>' for x in a['courses']) + '</ul>'
awards = heading('Recognition', 'Honors & awards', 'recognition-title')
awards += '<ul class="awards-list">' + ''.join(f'<li><span class="award-date">{e(x["year"])}</span><span>{e(x["title"])}</span></li>' for x in a['awards']) + '</ul>'

slots = {'UPDATED':e(a['updated']),'GROUP_DATE':e(p['as_of']),'PUBLICATIONS':section('publications',publications),'GROUP':section('group',group,'group-section'),'BACKGROUND':section('background',background,'about-background'),'GRANTS':section('grants',grants),'TEACHING':section('teaching',teaching),'AWARDS':section('recognition',awards)}
html = (ROOT / 'template.html').read_text(encoding='utf-8')
for name, value in slots.items():
    marker = '{{' + name + '}}'
    assert marker in html, f'Missing template marker: {name}'
    html = html.replace(marker, value)
assert not re.search(r'\{\{[A-Z_]+\}\}', html), 'Unresolved template markers'
(ROOT / 'dist').mkdir(exist_ok=True)
shutil.copytree(ROOT / 'assets', ROOT / 'dist/assets', dirs_exist_ok=True)
(ROOT / 'dist/index.html').write_text(html, encoding='utf-8')
(ROOT / 'dist/.nojekyll').touch()
print(f'Built dist/index.html: {len(a["publications"])} papers, {len(p["students"])} students, {len(p["postdocs"])} current postdocs, {len(p["phd_alumni"])} PhD alumni, {len(p["mphil_alumni"])} MPhil alumni, {len(p["former_postdocs"])} former postdocs.')

# Preserve the established links to academic sections after the redesign.
for old_path, url in {
    'publications': '../#publications',
    'grants': '../#grants',
    'people': '../#group',
    'teaching': '../#teaching',
    'awards': '../#recognition',
    'cv': '../assets/CV_Jin_Qi.pdf',
}.items():
    folder = ROOT / 'dist' / old_path
    folder.mkdir(exist_ok=True)
    redirect = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta http-equiv="refresh" content="0; url={url}"><title>Jin Qi — page moved</title></head><body><p>This page has moved. <a href="{url}">Continue to Jin Qi’s website</a>.</p></body></html>\n'
    (folder / 'index.html').write_text(redirect, encoding='utf-8')
