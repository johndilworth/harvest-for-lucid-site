#!/usr/bin/env python3
"""Cycle 1 board state as fetched 2026-10-02 ~12:00 MDT (Lucid fetch page_index 1-4 of 58ff5647-...).
Lean transcription: every generated shape (frame-/img-/hdr-/legend-/doc-title-/arrow-) as returned by the fetch
is listed in FETCHED below by its observed BoundingBox; reviewer-added stickies are transcribed verbatim with
their fill, bbox and parent (childrenIds). Writes board-state.json, harvest-compatible fetch-p<N>.json and
board-diff.json (fetched generated shapes vs ../lucid-spec.json)."""
import json, os
H = os.path.dirname(os.path.abspath(__file__)); C1 = os.path.dirname(H)
spec = json.load(open(os.path.join(C1, 'lucid-spec.json')))
STAMP = '2026-10-02 ~12:00 MDT'
# Observed frame order/x per page (frames 2240x1684 @ y=0; hdr = x+400,y40,1440x200; img = x+400,y260,1440x1024 for every
# frame; legend-box 0,-560,2600x360; legend-must/try/maybe x 2700/3020/3340 y-530 260x300; doc-title 0,-860,4400x200).
# All fetched values matched these exactly (checked item by item in the four fetch responses).
FETCHED_FRAMES = {
 'p1': ['home-01-hero','home-02-problem','home-03-how','home-04-benefits','home-05-before-after','home-06-paper-trail',
        'home-07-results','home-08-cost','home-09-compare','home-10-suite','home-11-cta-footer'],
 'p2': ['beta-01-home-cta','beta-02-form','beta-03-form-filled','beta-04-success'],
 'p3': ['how-01-top','how-02-review','how-03-harvest-ship','how-04-repeat','how-05-limits'],
 'p4': ['pricing-01-plans','pricing-02-faq'],
}
ARROWS = {'p1': 10, 'p2': 3, 'p3': 4, 'p4': 1}  # all connect frame i -> i+1, endpoints at frame edge y=757.72 (0.45)
STICKIES = [  # (page, id, parentId per childrenIds, fill, bbox, text) verbatim from fetch
 ('p1', '.lFzLThJV9Vd', 'frame-home-01-hero', '#ffe342ff', (245.93418000346128, 166.01413116067874, 160, 160),
  'Simplify this into a single header menu \u2014 don\'t need Lucid menu and Harvest menu. For now remove the "Lucid menu" at top, and focus on Harvest only. \n\nRemove "for Lucidchart" and let\'s just call it Harvest.'),
 ('p1', '~iFzEJJhMQKR', 'frame-home-01-hero', '#e81313ff', (282.8110326834859, 393.4673973321726, 160, 160),
  "Remove the get on the list banner. It's unnecessary"),
 ('p1', 'LkFzw70dU4RM', 'img-home-01-hero', '#ffe342ff', (866.9565920874644, 497.09109187480794, 160, 160),
  'Don\'t use the all caps eyebrow titles in the design \u2014 they are unecessary \u2014 remove "HARVEST FOR LUCIDCHART - LUCID SUITE ADD-ON (CONCEPT) here.'),
 ('p1', 'ynFz04DO.ydA', 'frame-home-01-hero', '#e81313ff', (405.9341800034613, 1137.0734080888146, 160, 160),
  'remove caption text below buttons, also unecessary  \u2014 keep focus simple.'),
 ('p1', '_nFzKjsd~dpT', 'frame-home-02-problem', '#ffe342ff', (2940, 342.25378217816956, 160, 160),
  'remove eyebrow titles such as "THE PROBLEM"  wherever possible, headlines can stand on their own.'),
 ('p4', 'LVGz2Ua1UQLs', 'frame-pricing-01-plans', '#ffe342ff', (213.35714285714278, 1124, 160, 160), ''),
]
bb = lambda x, y, w, h: 'x: %s, y: %s, w: %s, h: %s' % (x, y, w, h)
fetched = {}
for pid, keys in FETCHED_FRAMES.items():
    n = pid[1:]
    fetched[pid] = {'doc-title-%s' % pid: (0, -860, 4400, 200), 'legend-box-%s' % pid: (0, -560, 2600, 360),
                    'legend-must-%s' % pid: (2700, -530, 260, 300), 'legend-try-%s' % pid: (3020, -530, 260, 300),
                    'legend-maybe-%s' % pid: (3340, -530, 260, 300)}
    for i, k in enumerate(keys):
        x = 2720 * i
        fetched[pid]['frame-' + k] = (x, 0, 2240, 1684)
        fetched[pid]['hdr-' + k] = (x + 400, 40, 1440, 200)
        fetched[pid]['img-' + k] = (x + 400, 260, 1440, 1024)
# ---- diff vs spec
diff = {'_note': 'Fetched generated shapes vs lucid-spec.json (%s)' % STAMP, 'pages': {}}
total = 0
for p in spec['pages']:
    pid = p['id']; f = fetched[pid]; sp = {s['id']: s['boundingBox'] for s in p['shapes']}
    moved = [{'id': i, 'spec': sp[i], 'board': dict(zip('xywh', f[i]))} for i in sp if i in f and tuple(sp[i][k] for k in 'xywh') != f[i]]
    d = {'specShapes': len(sp), 'boardGenerated': len(f), 'missing': sorted(set(sp) - set(f)), 'extraGenerated': sorted(set(f) - set(sp)),
         'moved/resized': moved, 'specLines': len(p['lines']), 'boardLines': ARROWS[pid],
         'reviewerAdded': [s[1] for s in STICKIES if s[0] == pid], 'styleChanges': []}
    total += len(d['missing']) + len(d['extraGenerated']) + len(moved) + (len(p['lines']) != ARROWS[pid])
    diff['pages'][pid] = d
diff['directLayoutEdits'] = total
diff['summary'] = ('No direct layout edits: every generated shape and arrow is where lucid-spec.json/lucid-layout.json put it; '
                   'only additions are 6 sticky notes (5 on p1, 1 empty on p4).') if total == 0 else '%d differences' % total
json.dump(diff, open(os.path.join(H, 'board-diff.json'), 'w'), indent=1, ensure_ascii=False)
# ---- harvest-compatible fetch files
state = {'_note': 'Cycle 1 board state %s' % STAMP, 'pages': {}}
for p in spec['pages']:
    pid = p['id']; items = []
    kids = {}
    for s in STICKIES:
        if s[0] == pid: kids.setdefault(s[2], []).append(s[1])
    for i, b in fetched[pid].items():
        it = {'id': i, 'properties': {'BlockClass': 'SparkFrameBlock' if i.startswith('frame-') else 'UserImage2Block' if i.startswith('img-') else 'DefaultTextBlockNew', 'BoundingBox': bb(*b)}}
        if i.startswith('frame-'):
            k = i[6:]; it['shapeType'] = 'Frame'; it['properties']['TextAreas'] = [{'key': 'FrameTitle', 'text': next(s['title'] for s in p['shapes'] if s['id'] == i)}]
            it['childrenIds'] = ['img-' + k, 'hdr-' + k] + kids.get(i, [])
        if i.startswith('img-') and kids.get(i): it['childrenIds'] = kids[i]
        items.append(it)
    for s in STICKIES:
        if s[0] != pid: continue
        tas = [{'key': 'Text', 'text': s[5]}] if s[5] else []
        items.append({'id': s[1], 'shapeType': 'Sticky note', 'properties': {'BlockClass': 'StickiesStickyNoteBlock', 'BoundingBox': bb(*s[4]), 'FillColor': s[3], 'TextAreas': tas}, 'attribution': 'John Dilworth'})
    page = {'pageId': pid, 'pageTitle': p['title'], 'items': items}
    json.dump({'_note': 'Condensed from Lucid fetch(page_index=%s) %s via board-state.py' % (pid[1:], STAMP), 'pages': [page]},
              open(os.path.join(H, 'fetch-%s.json' % pid), 'w'), indent=1, ensure_ascii=False)
    state['pages'][pid] = {'title': p['title'], 'generated': len(fetched[pid]), 'arrows': ARROWS[pid], 'stickies': [s[1] for s in STICKIES if s[0] == pid]}
json.dump(state, open(os.path.join(H, 'board-state.json'), 'w'), indent=1, ensure_ascii=False)
print(diff['summary'])
