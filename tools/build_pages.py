#!/usr/bin/env python3
"""Generate site/*.html from the page modules (shared nav/footer). Run: python3 tools/build_pages.py"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from layout import page
from page_home import BODY as HOME
from page_other import HOW, PRICING, BETA
OUT = os.path.join(os.path.dirname(__file__), '..', 'site')
pages = {
  'index.html': page('Harvest for Lucidchart | Lucid', 'Turn prototype reviews in Lucidchart into pull requests with a paper trail.', 'home', HOME),
  'how-it-works.html': page('How Harvest works | Lucid', 'Capture, review, harvest and ship: how a Harvest review cycle works.', 'how', HOW),
  'pricing.html': page('Harvest pricing | Lucid', 'Harvest pricing: coming soon.', 'pricing', PRICING),
  'beta.html': page('Join the Harvest beta | Lucid', 'Join the Harvest for Lucidchart beta list.', 'beta', BETA, announce_bar=False),
}
for name, html in pages.items():
    open(os.path.join(OUT, name), 'w').write(html)
    print('wrote', name, len(html))
