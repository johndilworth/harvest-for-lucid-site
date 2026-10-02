from icons import HARVEST_MARK

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@100..125,600..800&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">')

def head(title, desc):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
{FONTS}
<link rel="stylesheet" href="/assets/site.css">
</head>'''

def nav(active):
    def cur(k): return ' aria-current="page"' if k == active else ''
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="pnav" id="pnav">
  <div class="wrap">
    <a class="pmark" href="/">{HARVEST_MARK}Harvest</a>
    <div class="pnav-menu" id="pnav-menu">
    <ul class="pnav-links">
      <li><a href="/"{cur('home')}>Overview</a></li>
      <li><a href="/how-it-works"{cur('how')}>How it works</a></li>
      <li><a href="/pricing"{cur('pricing')}>Pricing</a></li>
      <li><a href="/beta"{cur('beta')}>Beta</a></li>
    </ul>
    <div class="pnav-right">
      <a class="pright" href="/how-it-works">Watch the walkthrough</a>
      <a class="btn btn-primary btn-sm" href="/beta">Join the beta</a>
    </div>
    </div>
    <button class="burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="pnav-menu"><span></span><span></span><span></span></button>
  </div>
</header>'''

def cta_band(h, btn='Request beta access', sub=None):
    s = f'<p class="lede" style="margin-bottom:28px">{sub}</p>' if sub else ''
    return f'''<section class="cta-band" id="cta"><div class="wrap"><div class="inner">
  <h2>{h}</h2>{s}
  <a class="btn btn-light btn-lg" href="/beta">{btn}</a>
</div></div></section>'''

def footer():
    cols = [
      ('Get Started', [('Harvest overview', '/'), ('How it works', '/how-it-works'), ('Pricing', '/pricing'), ('Join the beta', '/beta')]),
      ('Products', [('Lucidchart', '#'), ('Lucidspark', '#'), ('Harvest (concept)', '/'), ('Integrations', '#')]),
      ('Solutions', [('Product &amp; UX', '#'), ('Engineering', '#'), ('AI transformation', '#'), ('New product development', '#')]),
      ('Company', [('About us', '#'), ('Newsroom', '#'), ('Careers', '#'), ('Accessibility', '#')]),
      ('Resources', [('Developers', '#'), ('MCP server', '#'), ('Security', '#'), ('Support', '#')]),
    ]
    html = ''.join(f'<div><h4>{h}</h4><ul>' + ''.join(f'<li><a href="{u}">{t}</a></li>' for t, u in items) + '</ul></div>' for h, items in cols)
    return f'''<footer class="footer">
  <div class="wrap">
    <div class="fcols">{html}</div>
    <div class="flegal">
      <a class="wordmark" href="/" aria-label="Lucid" style="font-size:18px">Lucid<span class="dot" aria-hidden="true"></span></a>
      <a href="#">Privacy</a><a href="#">Legal</a><a href="#">Cookie policy</a>
      <span class="mock">Concept mockup for pitch purposes.</span>
    </div>
  </div>
</footer>
<script src="/assets/site.js" defer></script>
</body>
</html>'''

def page(title, desc, active, body):
    return (head(title, desc) + '\n<body>\n' + nav(active) +
            '\n<main id="main">\n' + body + '\n</main>\n' + footer())
