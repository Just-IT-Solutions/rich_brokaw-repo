"""Builds the Free Resources + Resource Library demo pages (multi-file artifact alongside the homepage demo)."""
import re, html
from build_free_resources import GROUPS, COMING

home = open("richard-brokaw-demo.html").read()
css = re.search(r"<style>(.*?)</style>", home, re.S).group(1)

css += """
/* ---- free resources pages ---- */
.fr-hero { text-align: center; }
.fr-hero h1 { font-size: clamp(34px, 4.6vw, 50px); }
.fr-hero .lead { max-width: 60ch; margin: 0 auto; font-size: 19px; }
.steps { display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; margin-top: 30px; text-align: left; }
.step { border-top: 1px solid rgba(255,255,255,.18); padding-top: 18px; display: flex; flex-direction: column; gap: 6px; min-width: 0; }
.step b { font: 700 34px/1 var(--display); color: var(--gold); }
.step h3 { font-size: 20px; }
.step p { font-size: 16px; line-height: 1.6; }
.lib { background: var(--cream); }
.lib-head h2 { font-size: clamp(30px, 4vw, 40px); color: var(--navy); }
.group { display: flex; flex-direction: column; gap: 18px; }
.group + .group { margin-top: 44px; }
.group-head h2 { font-size: clamp(24px, 3vw, 30px); color: var(--navy); }
.group-head p { color: var(--muted); font-size: 16px; }
.rgrid { display: grid; grid-template-columns: repeat(var(--n, 3), 1fr); gap: 24px; }
.group-row { display: grid; grid-template-columns: 2fr 1fr; gap: 24px; margin-bottom: 44px; }
.group-row .group + .group { margin-top: 0; }
.res-card { background: var(--white); border: 1px solid var(--line); padding: 18px 18px 26px; display: flex; flex-direction: column; gap: 10px; min-width: 0; transition: box-shadow .2s, transform .2s; }
.res-card:hover { box-shadow: 0 14px 30px rgba(31,42,68,.12); transform: translateY(-2px); }
@media (prefers-reduced-motion: reduce) { .res-card, .res-card:hover { transition: none; transform: none; } }
.thumb { aspect-ratio: 4 / 3; overflow: hidden; border: 1px solid var(--line); background: var(--white); }
.thumb img { width: 100%; height: 100%; object-fit: cover; object-position: top center; display: block; }
.res-card .eyebrow { font-size: 12px; letter-spacing: 2px; }
.res-card h3 { font-size: 22px; color: var(--navy); }
.res-card p.desc { font-size: 16px; line-height: 1.6; }
.res-card .foot { margin-top: auto; padding-top: 6px; }
.res-card .btn { padding: 13px 22px; font-size: 13px; }
.unlock { background: var(--navy-dark); color: var(--on-dark); }
.unlock h2 { font-size: clamp(28px, 3.6vw, 38px); }
.unlock .lead { max-width: 60ch; font-size: 17px; }
.fine { font-size: 14px; color: var(--gold-soft); }
.coming h2 { font-size: clamp(26px, 3.4vw, 34px); color: var(--navy); }
.coming .sub { color: var(--muted); }
.cgrid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-top: 10px; text-align: left; }
.ccard { border: 1px dashed #C9BFA9; padding: 28px 26px; display: flex; flex-direction: column; gap: 8px; min-width: 0; }
.ccard h3 { font-size: 21px; color: var(--navy); }
.ccard p { color: var(--muted); font-size: 16px; line-height: 1.6; }
.ccard .eyebrow { color: var(--muted); font-size: 12px; margin-top: auto; padding-top: 4px; }
.group-cta { text-align: center; display: flex; flex-direction: column; align-items: center; gap: 12px; margin-top: 50px; }
.group-cta h3 { font-size: 24px; color: var(--navy); }
.group-cta p { color: var(--muted); }
@media (max-width: 900px) { .group-row { grid-template-columns: 1fr; gap: 44px; } .rgrid, .cgrid { grid-template-columns: 1fr 1fr; } .steps { grid-template-columns: 1fr; gap: 18px; } }
@media (max-width: 600px) { .rgrid, .cgrid { grid-template-columns: 1fr; } }
"""
open("demo/site.css", "w").write(css)

HEAD = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="claude:viewport-fit-sides" content="cover">
<title>{title}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,400;0,700;1,400&family=Playfair+Display:ital,wght@0,700;1,400&display=swap">
<link rel="stylesheet" href="site.css">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);color-scheme:light}} [hidden]{{display:none!important}} img{{max-width:100%}}</style>
</head><body>
<div class="demo-bar">{bar}</div>
<header>
  <div class="wrap head">
    <a class="brand" href="index.html"><b>Richard Brokaw</b><span>Author • Teacher • Disciple-Maker</span></a>
    <button class="menu-toggle" id="menu-toggle" aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav id="site-nav" aria-label="Main">
      <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="index.html#books">Books</a></li>
        <li><a href="free_resources.html">Free Resources</a></li>
        <li><a href="index.html#why-i-write">About Richard</a></li>
        <li><a href="index.html#ministry">For Churches</a></li>
        <li><a href="index.html#ekklesia">Reflections</a></li>
        <li><a href="index.html#join">Contact</a></li>
      </ul>
      <a class="btn" href="free_resources.html">Free Resources</a>
    </nav>
  </div>
</header>
<main>
"""

FOOT = """</main>
<footer><div class="wrap"><span><em>Listening to Jesus. Living Faithfully. Waiting for His Return.</em></span><span>© 2026 Richard Brokaw</span></div></footer>
<script>
(function () {
  var t = document.getElementById('menu-toggle'), n = document.getElementById('site-nav');
  t.addEventListener('click', function () { var o = n.classList.toggle('open'); t.setAttribute('aria-expanded', o ? 'true' : 'false'); t.textContent = o ? 'Close' : 'Menu'; });
  n.addEventListener('click', function (e) { if (e.target.tagName === 'A' && n.classList.contains('open')) t.click(); });
  var f = document.getElementById('signup');
  if (f) f.addEventListener('submit', function (e) {
    e.preventDefault();
    var note = document.getElementById('formnote');
    var email = document.getElementById('email').value.trim();
    if (!/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email)) { note.textContent = 'Enter a valid email address.'; return; }
    location.href = 'resource-library.html';
  });
})();
</script>
</body></html>
"""

esc = html.escape


def card(slug, title, tag, body, mode):
    foot = ('<a class="textlink" href="#unlock">Get It Free →</a>' if mode == "gated"
            else f'<a class="btn" href="pdfs/{slug}.pdf" target="_blank" rel="noopener">Download PDF</a>')
    return f"""<article class="res-card">
  <div class="thumb"><img src="thumbs/{slug}.png" alt="First page of {esc(title)}" loading="lazy"></div>
  <p class="eyebrow">{esc(tag)}</p>
  <h3>{esc(title)}</h3>
  <p class="desc">{esc(body)}</p>
  <div class="foot">{foot}</div>
</article>"""


def group(g, mode):
    name, blurb, items = g
    return f"""<div class="group">
  <div class="group-head"><h2>{esc(name)}</h2><p>{esc(blurb)}</p></div>
  <div class="rgrid" style="--n:{len(items)}">{''.join(card(*i, mode=mode) for i in items)}</div>
</div>"""


def groups(mode):
    found, mature, men = GROUPS
    return f'<div class="group-row">{group(found, mode)}{group(men, mode)}</div>' + group(mature, mode)


fr = HEAD.format(title="Free Resources · Richard Brokaw",
                 bar="Design preview of the Free Resources page. The signup form is a stand-in for MailerLite.") + f"""
<section class="dark fr-hero">
  <div class="wrap stack center" style="max-width:980px">
    <p class="eyebrow">Free Resources</p>
    <h1>Go Deeper in the Word</h1>
    <hr class="rule">
    <p class="lead">Bible studies, discipleship resources, teaching materials, and practical tools designed to help you move beyond simply reading Scripture to living it.</p>
    <div><a class="btn" href="#unlock">Get All Six Free</a></div>
    <div class="steps">
      <div class="step"><b>1</b><h3>Enter your name and email</h3><p>One short form below. It's free.</p></div>
      <div class="step"><b>2</b><h3>Open the resource library</h3><p>You go straight to a page with all six downloads.</p></div>
      <div class="step"><b>3</b><h3>Watch your inbox</h3><p>We'll also email you the link, plus new resources as they're released.</p></div>
    </div>
  </div>
</section>

<section class="lib" id="library">
  <div class="wrap">
    <div class="lib-head stack" style="margin-bottom:34px">
      <p class="eyebrow">The Library</p>
      <h2>Six Studies to Start With</h2>
      <hr class="rule">
    </div>
    {groups("gated")}
  </div>
</section>

<section class="unlock" id="unlock">
  <div class="wrap center stack" style="max-width:760px">
    <p class="eyebrow">Free Resource Library</p>
    <h2>Send Me the Resources</h2>
    <p class="lead">Enter your name and email to open all six downloads. You'll also receive occasional Bible teaching, new resources, ministry updates, and news about upcoming books.</p>
    <form class="signup" id="signup" novalidate>
      <label for="fname">First name</label>
      <input id="fname" name="fname" type="text" placeholder="First name" autocomplete="given-name">
      <label for="email">Email</label>
      <input id="email" name="email" type="email" placeholder="Email address" autocomplete="email">
      <button class="btn" type="submit">Send Me the Resources</button>
    </form>
    <p class="formnote" id="formnote" aria-live="polite"></p>
    <p class="fine">No cost. Unsubscribe anytime.</p>
  </div>
</section>

<section class="coming">
  <div class="wrap center stack">
    <p class="eyebrow">On the Way</p>
    <h2>More Resources Coming</h2>
    <p class="sub">Subscribers hear first when these are ready.</p>
    <div class="cgrid">
      {''.join(f'<div class="ccard"><h3>{esc(t)}</h3><p>{esc(b)}</p><p class="eyebrow">Coming Soon</p></div>' for t, b in COMING)}
    </div>
  </div>
</section>
""" + FOOT
open("demo/free_resources.html", "w").write(fr)

lib = HEAD.format(title="Resource Library · Richard Brokaw",
                  bar="Design preview of the page visitors see after signing up.") + f"""
<section class="dark fr-hero">
  <div class="wrap stack center" style="max-width:820px">
    <p class="eyebrow">Welcome</p>
    <h1>Your Free Resource Library</h1>
    <hr class="rule">
    <p class="lead">Thank you for joining. Download any of the studies below. A link to this page is also on its way to your inbox, so you can come back anytime.</p>
  </div>
</section>
<section class="lib">
  <div class="wrap">
    {groups("open")}
    <div class="group-cta">
      <h3>Studying with a group?</h3>
      <p>Richard teaches churches, men's groups, and small groups.</p>
      <a class="btn ghost" href="index.html#ministry">Invite Richard to Speak →</a>
    </div>
  </div>
</section>
""" + FOOT
open("demo/resource-library.html", "w").write(lib)
print("ok")
