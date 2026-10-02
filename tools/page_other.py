from icons import CAPTURE, REVIEW, HARVEST, SHIP, CHECK_BIG
from layout import cta_band

HOW = '''
<section class="hero hero-centered" id="top">
  <div class="wrap">
    <p class="eyebrow">How it works</p>
    <h1 class="h-xl h-wide">From prototype to pull request, one review cycle at a time</h1>
    <p class="lede" style="margin-top:24px">Harvest runs a repeatable loop around a Lucidchart board. Here&rsquo;s what happens in each cycle, using screens from our sample run.</p>
    <div class="cta-row"><a class="btn btn-primary btn-lg" href="/beta">Join the beta list</a><a class="btn btn-secondary btn-lg" href="#limits">What&rsquo;s not solved yet</a></div>
  </div>
</section>

<section class="bg-grey" id="stages" style="padding-top:24px">
  <div class="wrap">
    <div class="stage" id="capture"><div class="big">01</div><div>
      <span class="who ai">Harvest</span><h3>Capture: every screen, every step</h3>
      <p>You describe your key flows once (start page, the element to click, what to fill in). Harvest clicks through the prototype or staging app at desktop size and screenshots each step with the click drawn in as a large cursor. Each screenshot carries its route, page title, clicked element, commit and deploy URL. Screens are identified by route and title, so you don&rsquo;t add tracking attributes to your app.</p>
      <figure><img class="shot" src="/img/c4-vendor-detail.webp" width="1440" height="1024" alt="Captured screenshot of a vendor detail screen with a large cursor drawn on the Proceed button"><figcaption>A captured step: vendor detail, with the click on &ldquo;Proceed&rdquo; drawn in.</figcaption></figure>
    </div></div>
    <div class="stage" id="review"><div class="big">02</div><div>
      <span class="who people">Your team</span><h3>Review: stickies and sketches, right on the screen</h3>
      <p>Harvest builds a Lucidchart board with one page per flow and one large frame per screen, with a margin for notes. Designers, PMs, engineering leads and execs review it together and put stickies inside the frame they&rsquo;re about. They can also draw a mock directly on the screenshot.</p>
      <div class="legend" aria-label="Sticky legend"><span style="background:var(--sticky-red)">Red = must</span><span style="background:var(--sticky-yellow)">Yellow = try</span><span style="background:var(--sticky-blue)">Blue = maybe</span></div>
      <figure><img class="shot" src="/img/lucid-c4-vendor-detail.webp" width="888" height="1024" alt="Lucidchart frame for the vendor detail screen, with a cycle-3 before panel and a list of changes in this cycle"><figcaption>A frame from cycle 4 of the sample run, with the previous version and the list of changes above it.</figcaption></figure>
    </div></div>
    <div class="stage" id="harvest"><div class="big">03</div><div>
      <span class="who ai">Harvest</span> <span class="who people">You decide</span><h3>Harvest: collect, map and propose</h3>
      <p>Harvest reads the board through the Lucid MCP server. Lucidchart knows which items sit inside each frame, so every sticky maps to its exact screen. Priority comes from the sticky color or a leading &ldquo;must / try / maybe&rdquo;. Harvest proposes a change for every item and flags anything ambiguous, such as a sticky outside any frame or one that reverses an earlier decision. You approve the batch.</p>
      <p style="margin-top:12px">In the sample run, a reviewer drew a toast notification on a screenshot and wrote its copy. That copy shipped as written.</p>
    </div></div>
    <div class="stage" id="ship"><div class="big">04</div><div>
      <span class="who ai">Harvest + coding agent</span><h3>Ship: one PR with a preview and a paper trail</h3>
      <p>A coding agent implements the approved batch and opens a pull request with a deploy preview. The PR body lists every sticky verbatim next to the change and files touched, plus sections for judgment calls and reversals.</p>
      <figure><img class="shot" src="/img/c4-vendor-toast.webp" width="1440" height="1024" alt="Vendor list with a lower-left toast reading Helix LLM Gateway was updated"><figcaption>Shipped in PR #3: the reviewer-drawn toast, &ldquo;Helix LLM Gateway was updated.&rdquo;</figcaption></figure>
    </div></div>
    <div class="stage" id="repeat"><div class="big">&#8635;</div><div>
      <span class="who ai">Harvest</span><h3>Then repeat, with before and after</h3>
      <p>The next cycle captures the PR&rsquo;s preview. Every screen now has its previous version and a &ldquo;Changes in this cycle&rdquo; list beside it, so reviewers can check that their feedback landed before adding more.</p>
      <figure><img class="shot" src="/img/lucid-c4-vendor-strip.webp" width="1024" height="344" alt="Lucidchart page with four vendor-flow frames in a row, each with a before panel and changes list"><figcaption>The vendor flow in cycle 4: four screens, each with its before panel.</figcaption></figure>
    </div></div>
  </div>
</section>

<section id="needs">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">What you&rsquo;ll need</p><h2 class="h-lg">Fits the tools you already use</h2></div>
    <div class="cards">
      <div class="card"><h3>Lucidchart</h3><p>Reviewers work on a normal Lucidchart board. Harvest builds and reads it through the Lucid MCP server.</p></div>
      <div class="card"><h3>A prototype or staging app</h3><p>Anything reachable by URL. Deploy previews per pull request make the before/after loop work best.</p></div>
      <div class="card"><h3>A GitHub repository</h3><p>Pull requests carry the change, the preview link and the sticky-to-change table.</p></div>
    </div>
  </div>
</section>

<section class="bg-grey" id="limits">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Being upfront</p><h2 class="h-lg">What we haven&rsquo;t solved yet</h2></div>
    <div class="faq">
      <details open><summary>Screenshots need a reachable image host</summary><p>Captured screens are uploaded to an image host so the board can display them. Private hosting options are on the list.</p></details>
      <details><summary>Lucid comments aren&rsquo;t tied to a shape yet</summary><p>That&rsquo;s why Harvest uses the stickies-inside-frames convention. Comments are still collected and treated as general feedback.</p></details>
      <details><summary>Sticky authors aren&rsquo;t available to Harvest</summary><p>Harvest knows what each sticky says and where it is, but not who wrote it.</p></details>
      <details><summary>Reversals still need a person</summary><p>Harvest flags a sticky that undoes an earlier decision, but it won&rsquo;t pick a side. Someone on your team decides.</p></details>
      <details><summary>Is it cheaper than prompting in a chat?</summary><p>Not proven. We&rsquo;ve measured the Lucid side at roughly 5&ndash;6k tokens per feedback item; the head-to-head comparison is part of the beta.</p></details>
    </div>
  </div>
</section>
''' + cta_band('Want to try Harvest on your prototype?', 'Request beta access')

PRICING = '''
<section class="hero hero-centered" id="top">
  <div class="wrap">
    <p class="eyebrow">Pricing</p>
    <h1 class="h-xl h-wide">Pricing: coming soon</h1>
    <p class="lede" style="margin-top:24px">Harvest for Lucidchart is a concept in development. We&rsquo;ll share plans and pricing after the beta, once we&rsquo;ve measured what real review cycles cost.</p>
  </div>
</section>

<section class="bg-grey" id="plans" style="padding-top:56px">
  <div class="wrap">
    <div class="plans">
      <div class="plan feat"><span class="pill">Open for sign-ups</span><h3>Beta</h3><div class="price">Join the list<small>Pricing: coming soon</small></div>
        <ul><li>Pilot Harvest on one prototype with 3&ndash;5 reviewers</li><li>Two or three review cycles with us alongside</li><li>Help us measure token cost per feedback item</li></ul>
        <a class="btn btn-primary" href="/beta">Join the beta</a></div>
      <div class="plan"><span class="pill">Planned</span><h3>Team</h3><div class="price">Coming soon<small>Details after the beta</small></div>
        <ul><li>Unlimited flows and review cycles</li><li>Before/after boards for every cycle</li><li>Sticky-to-change tables in every PR</li></ul>
        <a class="btn btn-secondary" href="/beta">Get notified</a></div>
      <div class="plan"><span class="pill">Planned</span><h3>Enterprise</h3><div class="price">Coming soon<small>Details after the beta</small></div>
        <ul><li>Private screenshot hosting</li><li>Admin controls across the Lucid Suite</li><li>Help rolling the loop out across teams</li></ul>
        <a class="btn btn-secondary" href="/beta">Talk to us</a></div>
    </div>
    <p class="note center" style="margin-left:auto;margin-right:auto">Plan names and features are early ideas, not commitments.</p>
  </div>
</section>

<section id="pricing-faq">
  <div class="wrap">
    <div class="sec-head"><h2 class="h-lg">Pricing questions</h2></div>
    <div class="faq">
      <details open><summary>Will Harvest need a Lucid plan?</summary><p>Harvest is designed as a Lucid Suite add-on for Lucidchart. Plan requirements will be announced with pricing.</p></details>
      <details><summary>What drives the cost of a review cycle?</summary><p>Mostly AI tokens: building the board, reading the feedback and writing the code. We measured the Lucid side at roughly 5&ndash;6k tokens per feedback item. Capturing screenshots doesn&rsquo;t use the model at all.</p></details>
      <details><summary>Is there a cost to join the beta?</summary><p>We&rsquo;ll confirm beta terms with each team before anything starts.</p></details>
    </div>
  </div>
</section>
''' + cta_band('Help us shape Harvest', 'Request beta access')

BETA = '''
<div id="beta-root">
<section class="hero pre-success" id="top">
  <div class="wrap form-wrap">
    <div>
      <p class="eyebrow">Harvest beta</p>
      <h1 class="h-xl">Join the Harvest beta</h1>
      <p class="lede" style="margin-top:20px">We&rsquo;re looking for product teams who want to review a prototype together in Lucidchart and ship the feedback as pull requests.</p>
      <h2 class="h-md" style="margin-top:40px">What to expect</h2>
      <ul class="lede" style="font-size:17px;padding-left:20px">
        <li>A short call about your prototype and flows</li>
        <li>Two or three review cycles with 3&ndash;5 reviewers</li>
        <li>A paper trail for every sticky, in every PR</li>
      </ul>
    </div>
    <form class="form" id="beta-form" novalidate onsubmit="return false">
      <div class="row2">
        <div class="field"><label for="f-name">Full name</label><input id="f-name" name="name" autocomplete="name" required><span class="err">Please enter your name.</span></div>
        <div class="field"><label for="f-email">Work email</label><input id="f-email" name="email" type="email" autocomplete="email" required><span class="err">Please enter a valid work email.</span></div>
      </div>
      <div class="row2">
        <div class="field"><label for="f-company">Company</label><input id="f-company" name="company" autocomplete="organization"></div>
        <div class="field"><label for="f-role">Your role</label><select id="f-role" name="role"><option value="">Choose one</option><option>Product manager</option><option>Designer</option><option>Engineering lead</option><option>Engineer</option><option>Executive</option><option>Other</option></select></div>
      </div>
      <div class="field"><label for="f-reviewers">How many reviewers would join a cycle?</label><select id="f-reviewers" name="reviewers"><option value="">Choose one</option><option>1&ndash;2</option><option>3&ndash;5</option><option>6&ndash;10</option><option>More than 10</option></select></div>
      <div class="field"><label for="f-proto">What would you review first?</label><textarea id="f-proto" name="prototype" rows="3"></textarea><span class="hint">For example: &ldquo;Onboarding flow of our staging app&rdquo;</span></div>
      <fieldset class="checks"><legend class="sr">Options</legend>
        <label><input type="checkbox" name="lucid"> My team uses Lucidchart today</label>
        <label><input type="checkbox" name="previews"> We have deploy previews for pull requests</label>
      </fieldset>
      <button class="btn btn-primary btn-lg" type="submit" style="width:100%">Join the beta waitlist</button>
      <p class="fine">This page doesn&rsquo;t send or store anything.</p>
    </form>
  </div>
</section>
<section class="hero success" id="done">
  <div class="wrap">
    <div class="success-card">
      CHECK_BIG
      <h1 class="h-lg">You&rsquo;re on the beta list</h1>
      <p class="lede" style="margin-top:16px">Thanks<span id="s-name"></span>. Here&rsquo;s what happens next:</p>
      <ol class="lede" style="font-size:17px">
        <li>We&rsquo;ll reach out to set up a short call about your prototype.</li>
        <li>Together we&rsquo;ll pick two flows and capture your first Lucidchart board.</li>
        <li>Your reviewers leave stickies, and the first PR follows.</li>
      </ol>
      <div class="cta-row"><a class="btn btn-primary" href="/how-it-works">See how a cycle works</a><a class="btn btn-secondary" href="/">Back to overview</a></div>
      <p class="fine">Concept mockup: nothing was submitted.</p>
    </div>
  </div>
</section>
</div>
'''.replace('CHECK_BIG', CHECK_BIG)
