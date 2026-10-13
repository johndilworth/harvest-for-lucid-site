#!/usr/bin/env python3
"""Generate site/*.html from the page modules (shared nav/footer). Run: python3 tools/build_pages.py"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from layout import page
from page_home import BODY as HOME
OUT = os.path.join(os.path.dirname(__file__), '..', 'site')
pages = {
  'index.html': page('Harvest | Lucid', 'Every sticky note becomes a change: team reviews in Lucidchart, shipped by your agents with a paper trail.', 'home', HOME),
}
for name, html in pages.items():
    open(os.path.join(OUT, name), 'w').write(html)
    print('wrote', name, len(html))
