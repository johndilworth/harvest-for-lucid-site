from icons import REVIEW, HARVEST, SHIP, REPEAT, YES, NO, ico
from layout import cta_band

TRAIL = [
  ('1', 'must', 'Needs to be centered on page vertically like other screens.', 'home-00-landing', 'Landing content centered with the same layout rule as the signup cards.', 'done', 'Implemented'),
  ('7', 'try', 'Move Create Workspace button to left side', 'signup-03-goals', 'Create workspace is now the first (left) button, Back follows it.', 'rev', 'Reversal flagged'),
  ('9', 'must', 'Improve design of these cards, so it\u2019s not just looking like a table. Make this look like a sheet of paper\u2026', 'vendor-02-detail', '\u201cSheet of paper\u201d vendor record, status and risk chips, annual-spend panel with bars.', 'done', 'Implemented'),
  ('10', 'must', 'make the \u201cApprove\u201d button green', 'vendor-03-review', 'New success button style (#1d7a3d, white text). Reject stays red.', 'done', 'Implemented'),
  ('12', 'must', 'Remove this screen - instead of landing on this page, return to vendor page, and show a Growl type button in the lower left corner.', 'vendor-04-approved', 'Success screen removed. Approve returns to the vendor list with a lower-left toast, copy taken from the reviewer\u2019s drawn mock.', 'done', 'Implemented'),
  ('13', 'try', 'Growl message like this should have an x button to dismiss, or it should remove itself after 3 seconds.', 'vendor-04-approved', 'Both: a dismiss button and a 3-second auto-dismiss.', 'done', 'Implemented'),
]

def trail_rows():
    return ''.join(f'<tr><td>{n}</td><td><span class="pri {p}">{p}</span></td><td>\u201c{s}\u201d</td><td><code>{k}</code></td><td>{c}</td>'
                   f'<td><span class="status {st}">{lbl}</span></td></tr>' for n, p, s, k, c, st, lbl in TRAIL)

BODY = f'''
<section class="hero" id="top">
  <div class="wrap hero-grid">
    <div>
      <h1 class="h-xl">Every sticky note becomes a change</h1>
      <p class="lede">Your whole team reviews a running prototype together in Lucidchart, leaving color-coded stickies and quick sketches right on each screen. Harvest turns that feedback into code changes your agents ship as one pull request with a live preview, and every sticky is linked to the change it caused.</p>
      <div class="cta-row">
        <a class="btn btn-primary btn-lg" href="#how">See how it works</a>
        <a class="btn btn-secondary btn-lg" href="#benefits">Why teams use it</a>
      </div>
    </div>
    <div>
      <div class="canvas" role="img" aria-label="A Lucidchart frame holding a prototype screenshot, with a red 'must' sticky and a yellow 'try' sticky, and the pull request that implemented them">
        <span class="ftitle">vendor-03-review &middot; /vendors/:id/review</span>
        <div class="frame"><img src="/img/c3-vendor-review.webp" width="1440" height="1024" alt=""></div>
        <div class="sticky red s1"><b>must</b>make the &ldquo;Approve&rdquo; button green</div>
        <div class="sticky yellow s2"><b>try</b>Add a modal after &ldquo;Reject&rdquo; that requires a second confirmation</div>
        <div class="prcard"><div class="t">PR #3 <span class="open">Open</span></div>
          <ul><li><i style="background:var(--sticky-red)"></i>#10 Approve button is green</li><li><i style="background:var(--sticky-yellow)"></i>#11 Reject asks to confirm</li><li><i style="background:#dfe3e8"></i>Deploy preview ready</li></ul></div>
      </div>
      <p class="caption">From our sample run: a cycle-3 screen with two of the stickies reviewers left on it (recreated here), and the PR that shipped them.</p>
    </div>
  </div>
</section>

<section class="bg-orange" id="problem">
  <div class="wrap">
    <div class="sec-head"><h2 class="h-lg">Prototyping with AI shouldn&rsquo;t be a one-person chat</h2>
      <p class="lede">AI makes prototypes fast. But the review still runs through one person typing into one chat window, and everyone else&rsquo;s feedback gets retyped, summarized or lost.</p></div>
    <div class="cards">
      <div class="card">{ico('people', '#cc4e00')}<h3>Only one voice reaches the AI</h3><p>PMs, designers, engineering leads and execs have opinions that matter, but their feedback lands in Slack threads and meeting notes the agent never sees.</p></div>
      <div class="card">{ico('pin', '#cc4e00')}<h3>Feedback gets lost in translation</h3><p>&ldquo;The button on the third screen. No, the other one.&rdquo; Every comment has to be turned into a prompt before a model can act on it.</p></div>
      <div class="card">{ico('trail', '#cc4e00')}<h3>Decisions vanish with the chat</h3><p>Once the chat scrolls away, nobody can tell which requests were built, which were dropped and which quietly undid an earlier decision.</p></div>
    </div>
  </div>
</section>

<section class="bg-teal" id="how">
  <div class="wrap">
    <div class="sec-head"><h2 class="h-lg">Review. Harvest. Ship. Repeat.</h2>
      <p class="lede">Each review cycle runs the same loop. People do the reviewing and deciding; Harvest and your coding agents do the rest.</p></div>
    <div class="steps">
      <div class="step">{REVIEW}<div class="num">01</div><h3>Review</h3><p>Harvest clicks through your key flows and builds a Lucidchart board with one frame per screen. Reviewers put stickies inside a screen&rsquo;s frame (red = must, yellow = try, blue = consider) or sketch a mock right on the screenshot.</p></div>
      <div class="step">{HARVEST}<div class="num">02</div><h3>Harvest</h3><p>Harvest reads the board through the Lucid MCP server, maps each sticky to its exact screen and proposes a change for every item. Anything unclear or risky is flagged for a person.</p></div>
      <div class="step">{SHIP}<div class="num">03</div><h3>Ship</h3><p>A coding agent applies the batch and opens one pull request with a deploy preview. The PR lists every sticky, verbatim, next to the change it caused.</p></div>
      <div class="step">{REPEAT}<div class="num">04</div><h3>Repeat</h3><p>The next board shows each screen before and after, with a list of what changed, so reviewers check that their feedback landed and add the next round.</p></div>
    </div>
  </div>
</section>

<section id="benefits">
  <div class="wrap">
    <div class="sec-head"><h2 class="h-lg">Design with your whole team, not just a chat window</h2></div>
    <div class="cards">
      <div class="card">{ico('people', '#1071e5')}<h3>Multi-party, collaborative design</h3><p>Everyone reviews the same board in Lucidchart, and each cycle brings in input from every reviewer at once.</p><p class="quote">&ldquo;It evolves the prototype collaboratively instead of one person typing in a chat.&rdquo;</p></div>
      <div class="card">{ico('pin', '#1071e5')}<h3>Feedback in context</h3><p>Reviewers point at the screen instead of describing it. Stickies sit inside the frame they&rsquo;re about, and a drawn rectangle says more than a paragraph of prompt.</p></div>
      <div class="card">{ico('trail', '#1071e5')}<h3>A paper trail beside the PR</h3><p>Every pull request maps each sticky, verbatim, to the change and the files it touched. Stakeholders can see what was implemented, reverted or not acted on.</p></div>
      <div class="card">{ico('batch', '#1071e5')}<h3>Batched, not drip-fed</h3><p>A whole cycle of feedback is harvested together and shipped as one PR, instead of one prompt per comment.</p></div>
      <div class="card">{ico('flag', '#1071e5')}<h3>Reversals surfaced, not buried</h3><p>When a sticky undoes an earlier decision, Harvest flags it in the PR for a person to confirm, instead of letting changes silently overwrite each other.</p></div>
      <div class="card accent">{ico('chart', '#cc4e00')}<h3>Proven on a real loop</h3><p>3 review cycles, 32 feedback items and 3 PRs in one evening on a sample app.</p><a class="link-arrow" href="#results">See the numbers</a></div>
    </div>
  </div>
</section>

<section class="bg-grey" id="agents">
  <div class="wrap">
    <div class="sec-head"><h2 class="h-lg">Works with your agents</h2>
      <p class="lede">Harvest plugs into the coding agents you already run. Everyone else contributes from a Lucidchart board, so you don&rsquo;t add an AI license or usage for every person who weighs in.</p></div>
    <div class="cards">
      <div class="card">{ico('people', '#1071e5')}<h3>No AI seat per reviewer</h3><p>PMs, designers and execs leave stickies in Lucidchart. They shape the prototype without their own AI subscription, prompts or usage.</p></div>
      <div class="card">{ico('batch', '#1071e5')}<h3>One agent run per cycle</h3><p>Your agent picks up the whole batch of feedback at once, instead of a stream of one-off prompts from different people.</p></div>
      <div class="card">{ico('flag', '#1071e5')}<h3>People stay in charge</h3><p>Agents do the typing; your team decides what to build. Every change is reviewable in the pull request before it merges.</p></div>
    </div>
  </div>
</section>

<section id="evolution">
  <div class="wrap">
    <div class="sec-head"><h2 class="h-lg">See every cycle, side by side</h2>
      <p class="lede">The next cycle&rsquo;s board shows each screen next to its previous version, with a short list of what changed. Here&rsquo;s how the sample app evolved.</p></div>
    <div class="ba" data-tabs>
      <div class="ba-tabs" role="tablist" aria-label="Before and after examples">
        <button role="tab" id="tab-review" aria-controls="pan-review" aria-selected="true">Vendor review</button>
        <button role="tab" id="tab-detail" aria-controls="pan-detail" aria-selected="false" tabindex="-1">Vendor detail</button>
        <button role="tab" id="tab-all" aria-controls="pan-all" aria-selected="false" tabindex="-1">All cycles</button>
      </div>
      <div class="ba-panel" role="tabpanel" id="pan-review" aria-labelledby="tab-review">
        <div class="ba-pair">
          <figure><span class="tag before">Cycle 3 &middot; before</span><img src="/img/c3-vendor-review.webp" width="1440" height="1024" alt="Cycle 3 vendor review screen with red Reject and red Approve buttons"><figcaption>Stickies: &ldquo;make the Approve button green&rdquo; (must) and &ldquo;add a modal after Reject&rdquo; (try).</figcaption></figure>
          <figure><span class="tag after">Cycle 4 &middot; after PR #3</span><img src="/img/c4-vendor-review.webp" width="1440" height="1024" alt="Cycle 4 vendor review screen in dark mode with a green Approve button"><figcaption>Approve is green; Reject now asks for confirmation. Dark mode and the new font came from other stickies.</figcaption></figure>
        </div>
      </div>
      <div class="ba-panel" role="tabpanel" id="pan-detail" aria-labelledby="tab-detail" hidden>
        <div class="ba-pair">
          <figure><span class="tag before">Cycle 1 &middot; before</span><img src="/img/c1-vendor-detail.webp" width="1440" height="1024" alt="Cycle 1 vendor detail screen: a plain table of fields"><figcaption>The first build: a plain table of vendor fields.</figcaption></figure>
          <figure><span class="tag after">Cycle 4 &middot; after three PRs</span><img src="/img/c4-vendor-detail.webp" width="1440" height="1024" alt="Cycle 4 vendor detail screen: a vendor record with status chips and an annual spend panel"><figcaption>&ldquo;Make this look like a sheet of paper&rdquo;: status chips and an annual-spend panel.</figcaption></figure>
        </div>
      </div>
      <div class="ba-panel" role="tabpanel" id="pan-all" aria-labelledby="tab-all" hidden>
        <img src="/img/evolution-c1-c4.webp" width="1024" height="991" alt="Lucidchart board comparing five screens across cycles 1 to 4" style="max-width:860px;margin:0 auto">
        <p class="caption center">Lucidchart export: five screens across cycles 1&ndash;4 (0, 11, 8 and 13 feedback items applied by the PR behind each build).</p>
      </div>
    </div>
  </div>
</section>

<section class="bg-grey" id="paper-trail">
  <div class="wrap">
    <div class="sec-head"><h2 class="h-lg">A paper trail beside every pull request</h2>
      <p class="lede">Each PR body maps every sticky, verbatim, to its screen, the change and the files touched. Judgment calls and reversals get their own section marked &ldquo;please confirm&rdquo;.</p></div>
    <div class="table-scroll">
      <table class="trail">
        <thead><tr><th>#</th><th>Priority</th><th>Sticky (verbatim)</th><th>Screen</th><th>Change</th><th>Status</th></tr></thead>
        <tbody>{trail_rows()}</tbody>
      </table>
    </div>
    <p class="note">Excerpt: 6 of the 13 rows in PR #3 of our sample run. Row 7 reversed two earlier stickies (the button had moved right in cycles 1 and 2), so the PR flagged it for a person to confirm.</p>
  </div>
</section>

<section class="bg-indigo" id="results">
  <div class="wrap">
    <div class="sec-head"><h2 class="h-lg">Three review cycles in one evening</h2>
      <p class="lede">We ran Harvest on a small two-flow sample app (signup and vendor approval). Cycle 1 was captured at 10:56 PM MT and the third PR opened at 12:42 AM MT.</p></div>
    <div class="stats">
      <div class="stat"><div class="n">3</div><div class="l">review cycles</div></div>
      <div class="stat"><div class="n">32</div><div class="l">feedback items (11 must, 21 try)</div></div>
      <div class="stat"><div class="n">3</div><div class="l">pull requests, each with a deploy preview</div></div>
      <div class="stat"><div class="n">32/32</div><div class="l">items mapped to a change in the next PR&rsquo;s table</div></div>
    </div>
    <p class="note">&ldquo;Mapped&rdquo; means the item appears in the PR&rsquo;s sticky-to-change table, not that every reviewer signed off. One sample app, one team. Your results will vary.</p>
  </div>
</section>

<section id="compare">
  <div class="wrap">
    <div class="sec-head"><h2 class="h-lg">Where Harvest fits</h2>
      <p class="lede">Design-file comments and chat-based prototyping are both great at what they do. Harvest is built for reviewing a running prototype with a group, and getting the result back into code.</p></div>
    <div class="table-scroll">
      <table class="compare">
        <thead><tr><th scope="col"></th><th scope="col">Chat-only AI prototyping</th><th scope="col">Comments on design files (e.g. Figma)</th><th scope="col" class="us">Harvest</th></tr></thead>
        <tbody>
          <tr><th scope="row">What reviewers look at</th><td><span class="mk no">{NO}</span>Only what one person describes</td><td><span class="mk no">{NO}</span>Static mockups, not the running app</td><td class="us"><span class="mk yes">{YES}</span>Screenshots of the running app, every step of each flow</td></tr>
          <tr><th scope="row">Who contributes</th><td><span class="mk no">{NO}</span>Usually one person</td><td><span class="mk no">{NO}</span>Designers in the file; the rest rarely</td><td class="us"><span class="mk yes">{YES}</span>The whole team, in the same cycle</td></tr>
          <tr><th scope="row">How feedback is given</th><td><span class="mk no">{NO}</span>Typed descriptions of the UI</td><td><span class="mk no">{NO}</span>Comment threads, no priority</td><td class="us"><span class="mk yes">{YES}</span>Prioritized stickies and sketches on each screen</td></tr>
          <tr><th scope="row">From feedback to code</th><td><span class="mk no">{NO}</span>One prompt per comment</td><td><span class="mk no">{NO}</span>A separate manual handoff</td><td class="us"><span class="mk yes">{YES}</span>One PR per cycle, with a deploy preview</td></tr>
          <tr><th scope="row">Record of what happened</th><td><span class="mk no">{NO}</span>Lost in chat history</td><td><span class="mk no">{NO}</span>Resolved threads, not linked to code</td><td class="us"><span class="mk yes">{YES}</span>Every sticky mapped to its change in the PR</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="bg-grey" id="suite">
  <div class="wrap split">
    <div>
      <h2 class="h-lg">Built on the Lucidchart your team already uses</h2>
      <p class="lede">Harvest works with Lucidchart frames, sticky notes and shapes, and reads boards through the Lucid MCP server. There&rsquo;s nothing new for reviewers to learn and no tracking code to add to your app.</p>
    </div>
    <figure style="margin:0"><img class="shot" src="/img/lucid-c4-landing.webp" width="1024" height="805" alt="Lucidchart page from the sample run: review legend, before panel, changes list and a frame holding the landing page screenshot"><figcaption class="caption">A cycle-4 review page from the sample run, exported from Lucidchart.</figcaption></figure>
  </div>
</section>
''' + cta_band('Bring your next prototype review into Lucidchart',
               sub='Harvest is a concept. We&rsquo;re looking for product teams with a prototype or staging app and 3&ndash;5 reviewers to pilot it over two or three cycles.')
