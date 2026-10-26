"""Prayer for the Babies in NYS: demo page, Elementor template, Free Resources feature banner."""
import json, re, html
from build_prayer_text import *
from elementor_lib import *

SLUG = "prayer_for_the_babies"
WP_URL = "/free_resources/prayer_for_the_babies/"
DEMO_FILE = "prayer_for_the_babies.html"
PDF = "prayer-for-the-babies-in-nys.pdf"
LEAD = ("A prayer written by Richard Brokaw for believers to pray, alone or together, "
        "for the babies and for the people of New York State.")
WAYS = [
    ("Pray it daily", "Read it aloud each morning, or set a time each week to pray it with your family."),
    ("Pray it together", "Print the one-page PDF for your church, prayer meeting, men's group, or small group."),
    ("Share it", "Send this page to other believers so more voices come into agreement."),
]

PAGE_CSS = """
.pr-hero { background: var(--navy-dark); text-align: center; }
.pr-hero h1 { font-size: clamp(32px, 4.6vw, 50px); max-width: 20ch; margin-inline: auto; }
.pr-hero .lead { max-width: 56ch; margin: 0 auto; font-size: 19px; }
.pr-text { background: var(--cream); }
.pr-text .wrap { max-width: 980px; }
.pr-body { display: flex; flex-direction: column; gap: 26px; margin-top: 10px; }
.pr-row { display: grid; grid-template-columns: 220px 1fr; gap: 36px; align-items: start; }
.pr-label { font: 700 12px/1.5 var(--body); letter-spacing: 2px; text-transform: uppercase; color: var(--gold); padding-top: 6px; border-top: 2px solid var(--gold); }
.pr-row p.pr-p { font: 400 clamp(18px, 1.9vw, 20px)/1.85 var(--display); color: var(--ink); max-width: 64ch; min-width: 0; }
.pr-sal { font: italic 400 24px/1.4 var(--display); color: var(--navy); }
.pr-amen { text-align: center; margin-top: 34px; display: flex; flex-direction: column; align-items: center; gap: 12px; }
.pr-ways h2 { font-size: clamp(28px, 3.6vw, 38px); color: var(--navy); }
.ways { display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; margin-top: 14px; text-align: left; }
.way { border-top: 2px solid var(--gold); padding-top: 16px; display: flex; flex-direction: column; gap: 8px; min-width: 0; }
.way h3 { font-size: 21px; color: var(--navy); }
.way p { font-size: 16px; line-height: 1.6; color: var(--ink); }
.share { display: flex; flex-wrap: wrap; gap: 10px; align-items: center; margin-top: 6px; }
.share input { flex: 1 1 200px; min-width: 0; font: 14px var(--body); padding: 11px 12px; border: 1px solid var(--line); background: var(--white); color: var(--ink); border-radius: 2px; }
.share button { cursor: pointer; padding: 12px 18px; font-size: 12px; }
.share-note { font-size: 13px; color: var(--muted); min-height: 1.4em; }
.pr-join { background: var(--navy); }
.pr-join h2 { font-size: clamp(28px, 3.6vw, 36px); }
.pr-join .lead { max-width: 56ch; font-size: 17px; }
.feat-prayer { background: var(--white); border: 1px solid var(--line); border-top: 4px solid var(--gold); display: grid; grid-template-columns: 200px 1fr; gap: 30px; align-items: center; padding: 26px; margin-bottom: 50px; text-align: left; }
.feat-prayer .thumb { aspect-ratio: 4 / 3; }
.feat-prayer h2 { font-size: clamp(24px, 2.8vw, 30px); color: var(--navy); }
.feat-prayer p.d { font-size: 16px; line-height: 1.6; color: var(--ink); max-width: 60ch; }
.feat-prayer .txt { display: flex; flex-direction: column; gap: 10px; align-items: flex-start; min-width: 0; }
@media (max-width: 900px) {
  .pr-row { grid-template-columns: 1fr; gap: 10px; }
  .pr-label { border-top: 0; padding-top: 0; }
  .ways { grid-template-columns: 1fr; gap: 22px; }
  .feat-prayer { grid-template-columns: 1fr; }
  .feat-prayer .thumb { max-width: 320px; }
}
"""


def demo():
    a = open("demo/about-richard.html").read()
    head = a[:a.index("<main>") + len("<main>\n")]
    head = re.sub(r"<title>.*?</title>", "<title>Prayer for the Babies · Richard Brokaw</title>", head)
    head = re.sub(r'<div class="demo-bar">.*?</div>',
                  '<div class="demo-bar">Design preview of the prayer page. The signup form is a stand-in for MailerLite.</div>', head)
    foot = a[a.index("</main>"):]
    rows = [f'<div class="pr-row"><span></span><p class="pr-sal">{SALUTATION}</p></div>']
    for lab, p in zip(LABELS, PARAS):
        rows.append(f'<div class="pr-row"><p class="pr-label">{lab}</p><p class="pr-p">{p}</p></div>')
    page = head + f"""
<section class="dark pr-hero">
  <div class="wrap stack center" style="max-width:900px">
    <p class="eyebrow">Free Resource · A Prayer</p>
    <h1>{TITLE}</h1>
    <hr class="rule">
    <p class="lead">{LEAD}</p>
    <div class="btn-row" style="justify-content:center">
      <a class="btn" href="#prayer">Pray the Prayer</a>
      <a class="btn ghost" href="pdfs/{PDF}" target="_blank" rel="noopener">Download Printable PDF</a>
    </div>
  </div>
</section>

<section class="pr-text" id="prayer">
  <div class="wrap">
    <div class="pr-body">
      {''.join(rows)}
    </div>
    <div class="pr-amen">
      <hr class="rule">
      <p class="eyebrow">Richard Brokaw</p>
      <a class="btn ghost" href="pdfs/{PDF}" target="_blank" rel="noopener">Download Printable PDF</a>
    </div>
  </div>
</section>

<section class="pr-ways">
  <div class="wrap center stack">
    <p class="eyebrow">Pray It With Others</p>
    <h2>Carry This Prayer Further</h2>
    <hr class="rule">
    <div class="ways">
      {''.join(f'<div class="way"><h3>{t}</h3><p>{d}</p>' + ('''<div class="share"><label class="rb-sr" for="share-url">Link to this page</label><input id="share-url" type="text" readonly><button class="btn" type="button" id="copy-link">Copy Link</button></div><p class="share-note" id="share-note" aria-live="polite"></p>''' if t == "Share it" else "") + '</div>' for t, d in WAYS)}
    </div>
  </div>
</section>

<section class="pr-join dark" id="join">
  <div class="wrap center stack" style="max-width:760px">
    <p class="eyebrow">Stand With Us in Prayer</p>
    <h2>Join the Mailing List</h2>
    <p class="lead">Receive this prayer and others like it, along with Bible teaching, new resources, and ministry updates.</p>
    <form class="signup" id="signup" novalidate>
      <label for="fname">First name</label>
      <input id="fname" name="fname" type="text" placeholder="First name" autocomplete="given-name">
      <label for="email">Email</label>
      <input id="email" name="email" type="email" placeholder="Email address" autocomplete="email">
      <button class="btn" type="submit">Count Me In</button>
    </form>
    <p class="formnote" id="formnote" aria-live="polite"></p>
    <p class="fine">No cost. Unsubscribe anytime.</p>
  </div>
</section>

<section class="bk-close" style="background:var(--cream)">
  <div class="wrap stack center">
    <p class="eyebrow">Go Deeper</p>
    <h2 style="font-size:clamp(26px,3.4vw,34px);color:var(--navy)">More Free Resources</h2>
    <p style="max-width:56ch;color:var(--muted)">Six free studies on knowing God, maturity in Christ, and discipleship.</p>
    <a class="btn" href="free_resources.html">Free Resources</a>
  </div>
</section>
""" + foot
    share_js = """<script>
(function () {
  var u = document.getElementById('share-url'), b = document.getElementById('copy-link'), n = document.getElementById('share-note');
  if (!u) return;
  u.value = location.href.split('#')[0];
  b.addEventListener('click', function () {
    function fallback() { u.focus(); u.select(); n.textContent = 'Link selected. Press Ctrl+C (or Cmd+C) to copy.'; }
    try { navigator.clipboard.writeText(u.value).then(function () { n.textContent = 'Link copied.'; }, fallback); } catch (e) { fallback(); }
  });
  var f = document.getElementById('signup');
  if (f) f.addEventListener('submit', function (e) {
    e.preventDefault();
    var note = document.getElementById('formnote'), email = document.getElementById('email').value.trim();
    note.textContent = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email) ? 'Demo only. On the live site this adds you to the MailerLite list.' : 'Enter a valid email address.';
  }, true);
})();
</script>
</body>"""
    # the shared footer script redirects signups to the library; stop that on this page
    page = page.replace("</body>", share_js, 1)
    page = page.replace("if (f) f.addEventListener('submit', function (e) {\n    e.preventDefault();\n    var note = document.getElementById('formnote');",
                        "if (f && !document.getElementById('share-url')) f.addEventListener('submit', function (e) {\n    e.preventDefault();\n    var note = document.getElementById('formnote');")
    open("demo/" + DEMO_FILE, "w").write(page)

    s = open("demo/site.css").read()
    if ".pr-hero {" not in s:
        open("demo/site.css", "a").write(PAGE_CSS)

    # feature banner on Free Resources
    fr = open("demo/free_resources.html").read()
    if "feat-prayer" not in fr:
        banner = f"""<a id="prayer-feature"></a>
    <div class="feat-prayer">
      <div class="thumb"><img src="thumbs/prayer-for-the-babies-in-nys.png" alt="First page of {TITLE}"></div>
      <div class="txt">
        <p class="eyebrow">Featured · A Prayer</p>
        <h2>{TITLE}</h2>
        <p class="d">{LEAD} Read it on the page or print the one-page PDF. No signup needed.</p>
        <a class="btn" href="{DEMO_FILE}">Read and Pray</a>
      </div>
    </div>
    """
        marker = '<div class="lib-head stack"'
        assert marker in fr
        fr = fr.replace(marker, banner + marker, 1)
        open("demo/free_resources.html", "w").write(fr)


def elementor():
    rows = [text(f'<p style="font-style:italic;font-size:24px;color:#1F2A44;font-family:Playfair Display,Georgia,serif">{SALUTATION}</p>', align="left")]
    for lab, p in zip(LABELS, PARAS):
        rows.append(container([
            container([eyebrow(lab, align="left")], width=24, inner=True, align="flex-start",
                      extra={"border_border": "solid",
                             "border_width": {"unit": "px", "top": "2", "right": "0", "bottom": "0", "left": "0", "isLinked": False},
                             "border_color": GOLD, "padding": pad(6, 0, 0, 0)}),
            container([text(f"<p>{p}</p>", align="left", size=20, lh=1.85)], width=72, inner=True, align="flex-start",
                      extra={"_css": ""}),
        ], direction="row", gap=36, inner=True, boxed=False, align="flex-start"))
    for r in rows[1:]:
        r["elements"][1]["elements"][0]["settings"]["typography_font_family"] = HEAD_FONT

    pdf_url = f"/wp-content/uploads/resources/{PDF}"
    def pdf_btn(primary, on_dark=False):
        b = button("Download Printable PDF", pdf_url, primary=primary, on_dark=on_dark)
        b["settings"]["link"]["is_external"] = "on"
        return b

    hero = container([
        eyebrow("Free Resource · A Prayer"),
        heading(TITLE, tag="h1", color=WHITE, size=50, mobile=32),
        divider(),
        text(f"<p>{LEAD}</p>", color="#D9DCE3", size=19),
        container([button("Pray the Prayer", "#prayer"), pdf_btn(False, True)],
                  direction="row", gap=14, inner=True, boxed=False, justify="center"),
    ], bg=NAVY_DARK, padding=pad(90, 20, 80, 20), gap=16, extra={"boxed_width": px(900)})

    prayer = container(rows + [spacer(10), divider(), eyebrow("Richard Brokaw"), pdf_btn(False)],
                       bg=CREAM, padding=pad(80, 20, 90, 20), gap=24, align="stretch", css_id="prayer",
                       extra={"boxed_width": px(980)})
    prayer["elements"][-3]["settings"]["align"] = "center"

    def way(t, d_):
        kids = [heading(t, tag="h3", size=21, mobile=20, align="left"), text(f"<p>{d_}</p>", align="left", size=16, lh=1.6)]
        if t == "Share it":
            kids.append(widget("html", {"html": """<div style="display:flex;gap:10px;flex-wrap:wrap"><input id="pr-share" readonly style="flex:1 1 200px;min-width:0;padding:11px 12px;border:1px solid #E3DCCD;font:14px Lato,sans-serif"><button type="button" id="pr-copy" style="cursor:pointer;background:#B8893B;color:#fff;border:2px solid #B8893B;padding:11px 18px;font:700 12px Lato,sans-serif;letter-spacing:2px;text-transform:uppercase">Copy Link</button></div><p id="pr-note" style="font:13px Lato,sans-serif;color:#5A6070;min-height:1.4em"></p>
<script>(function(){var u=document.getElementById('pr-share'),b=document.getElementById('pr-copy'),n=document.getElementById('pr-note');u.value=location.href.split('#')[0];b.onclick=function(){function f(){u.focus();u.select();n.textContent='Link selected. Press Ctrl+C (or Cmd+C) to copy.';}try{navigator.clipboard.writeText(u.value).then(function(){n.textContent='Link copied.';},f);}catch(e){f();}};})();</script>"""}))
        return container(kids, width=31, inner=True, align="flex-start", gap=8,
                         extra={"border_border": "solid",
                                "border_width": {"unit": "px", "top": "2", "right": "0", "bottom": "0", "left": "0", "isLinked": False},
                                "border_color": GOLD, "padding": pad(16, 0, 0, 0)})

    ways = container([
        eyebrow("Pray It With Others"), heading("Carry This Prayer Further", size=38, mobile=28), divider(),
        container([way(*w) for w in WAYS], direction="row", gap=30, inner=True, boxed=False, align="flex-start"),
    ], bg=WHITE, padding=pad(90, 20, 90, 20), gap=16)

    signup = """<div style="max-width:620px;margin:0 auto;padding:28px;border:2px dashed #B8893B;border-radius:4px;background:#fff;text-align:center;font-family:Lato,sans-serif;color:#5A6070;">
<!-- REPLACE with the MailerLite "Prayer" form (embed code or plugin shortcode). Put signups in a group such as "Prayer for NYS". -->
<strong style="color:#1F2A44;">MailerLite signup form goes here</strong><br><span style="font-size:14px;">First name + Email + "Count Me In" button</span></div>"""
    join = container([
        eyebrow("Stand With Us in Prayer"), heading("Join the Mailing List", color=WHITE, size=36, mobile=28),
        text("<p>Receive this prayer and others like it, along with Bible teaching, new resources, and ministry updates.</p>", color="#D9DCE3", size=17),
        widget("html", {"html": signup}), text("<p>No cost. Unsubscribe anytime.</p>", color="#D4AE6B", size=14),
    ], bg=NAVY, padding=pad(80, 20, 80, 20), gap=14, css_id="join", extra={"boxed_width": px(760)})

    more = container([
        eyebrow("Go Deeper"), heading("More Free Resources", size=34, mobile=26),
        text("<p>Six free studies on knowing God, maturity in Christ, and discipleship.</p>", color=MUTED),
        button("Free Resources", "/free_resources/"),
    ], bg=CREAM, padding=pad(80, 20, 90, 20), gap=14)

    t = {"content": [hero, prayer, ways, join, more],
         "page_settings": {"hide_title": "yes", "template": "elementor_header_footer"},
         "version": "0.4", "title": "Richard Brokaw – Prayer for the Babies in NYS", "type": "page"}
    json.dump(t, open("richard-brokaw-prayer-elementor.json", "w"), indent=1, ensure_ascii=False)

    # feature banner inside the Free Resources template, right after the hero
    fp = "richard-brokaw-free-resources-elementor.json"
    fr = json.load(open(fp))
    if not any(c["settings"].get("_element_id") == "prayer-feature" for c in fr["content"]):
        img = {"image": {"url": "/wp-content/uploads/resources/prayer-for-the-babies-in-nys.png", "id": "", "alt": f"First page of {TITLE}", "source": "url"},
               "image_size": "full", "width": {"unit": "%", "size": 100, "sizes": []},
               "image_border_border": "solid", "image_border_width": {"unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": True},
               "image_border_color": "#E3DCCD"}
        banner = container([
            container([widget("image", img)], width=24, inner=True),
            container([eyebrow("Featured · A Prayer", align="left"),
                       heading(TITLE, size=30, mobile=24, align="left"),
                       text(f"<p>{LEAD} Read it on the page or print the one-page PDF. No signup needed.</p>", align="left", size=16, lh=1.6),
                       button("Read and Pray", WP_URL, align="left")], width=70, inner=True, align="flex-start", gap=10),
        ], direction="row", gap=30, bg=CREAM, padding=pad(50, 20, 10, 20), align="center", css_id="prayer-feature")
        fr["content"].insert(1, banner)
        json.dump(fr, open(fp, "w"), indent=1, ensure_ascii=False)


if __name__ == "__main__":
    demo(); elementor(); print("ok")
