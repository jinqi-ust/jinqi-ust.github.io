#!/usr/bin/env python3
"""Check generated content, anchors, and local assets before publishing."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from collections import Counter
import json

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'

class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.text, self.images = [], [], [], []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'): self.ids.append(attrs['id'])
        for key in ('src','href'):
            if attrs.get(key): self.links.append(attrs[key])
        if tag == 'img': self.images.append(attrs)
    def handle_data(self, data):
        self.text.append(data)

html = (DIST / 'index.html').read_text(encoding='utf-8')
doc = Document()
doc.feed(html)
assert '{{' not in html, 'Unresolved template fields'
assert not [key for key,count in Counter(doc.ids).items() if count > 1], 'Duplicate HTML IDs'
for link in doc.links:
    parts = urlsplit(link)
    if parts.scheme or parts.netloc: continue
    if not parts.path and parts.fragment:
        assert unquote(parts.fragment) in doc.ids, f'Missing anchor: {link}'
    if parts.path:
        assert (DIST / unquote(parts.path)).is_file(), f'Missing asset: {link}'
for img in doc.images:
    assert img.get('alt'), 'Missing image alt text'
text = ' '.join(doc.text)
people = json.loads((ROOT / 'data/people.json').read_text(encoding='utf-8'))
for group in people.values():
    if isinstance(group,list):
        for person in group:
            assert person['name'] in text, f'Missing person: {person["name"]}'
academic = json.loads((ROOT / 'data/academic.json').read_text(encoding='utf-8'))
for paper in academic['publications']:
    assert paper['title'] in text, f'Missing paper: {paper["title"]}'
assert (DIST / '.nojekyll').exists()
print('Passed: all people and papers rendered; all internal links, assets, and image labels are valid.')
