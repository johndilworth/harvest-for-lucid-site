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
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="pnav" id="pnav">
  <div class="wrap">
    <a class="pmark" href="/">{HARVEST_MARK}Harvest</a>
    <div class="pnav-menu" id="pnav-menu">
    <ul class="pnav-links">
      <li><a href="#how">How it works</a></li>
      <li><a href="#benefits">Why Harvest</a></li>
      <li><a href="#agents">Your agents</a></li>
      <li><a href="#compare">Compare</a></li>
    </ul>
    <div class="pnav-right">
      <a class="btn btn-primary btn-sm" href="#how">See how it works</a>
    </div>
    </div>
    <button class="burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="pnav-menu"><span></span><span></span><span></span></button>
  </div>
</header>'''

def cta_band(h, btn=None, sub=None, href='#how'):
    s = f'<p class="lede">{sub}</p>' if sub else ''
    b = f'<a class="btn btn-light btn-lg" style="margin-top:28px" href="{href}">{btn}</a>' if btn else ''
    return f'''<section class="cta-band" id="cta"><div class="wrap"><div class="inner">
  <h2>{h}</h2>{s}{b}
</div></div></section>'''

def footer():
    return '''<footer class="footer">
  <div class="wrap">
    <div class="flegal">
      <a class="wordmark" href="/" aria-label="Lucid" style="font-size:18px">Lucid<span class="dot" aria-hidden="true"></span></a>
      <span class="mock">Concept mockup for internal pitch purposes.</span>
    </div>
  </div>
</footer>
<script src="/assets/site.js" defer></script>
</body>
</html>'''

def page(title, desc, active, body):
    return (head(title, desc) + '\n<body>\n' + nav(active) +
            '\n<main id="main">\n' + body + '\n</main>\n' + footer())
