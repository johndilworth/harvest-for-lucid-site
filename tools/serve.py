#!/usr/bin/env python3
"""Local preview with Netlify-style pretty URLs (/beta -> beta.html). python3 tools/serve.py [port]"""
import http.server, os, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'site')
class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k): super().__init__(*a, directory=ROOT, **k)
    def translate_path(self, path):
        p = super().translate_path(path)
        if not os.path.exists(p) and os.path.exists(p + '.html'): return p + '.html'
        return p
    def log_message(self, *a): pass
http.server.ThreadingHTTPServer(('127.0.0.1', int(sys.argv[1]) if len(sys.argv) > 1 else 8765), H).serve_forever()
