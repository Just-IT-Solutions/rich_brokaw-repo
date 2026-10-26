"""'Recommended Sites' section for the main Free Resources page (demo + Elementor)."""
import json
from elementor_lib import *

SITES = [
    dict(name="Capital Church", url="https://capitalchurchny.org/", domain="capitalchurchny.org",
         kind="Church",
         desc="A church for the Capital Region, meeting in person and online. Their invitation to everyone: “You’re welcome here.”"),
    dict(name="Students for Life of America", url="https://studentsforlife.org/", domain="studentsforlife.org",
         kind="Pro-Life Organization",
         desc="A national pro-life organization working through campus groups, advocate training, and outreach. Their focus: “Save Babies. Empower Women.”"),
]
HEAD = ("Beyond This Site", "Recommended Sites",
        "Churches and organizations Richard recommends for further encouragement and involvement.")
CSS = """
.ext { background: var(--cream); border-top: 1px solid var(--line); }
.ext h2 { font-size: clamp(28px, 3.4vw, 36px); color: var(--navy); }
.ext .sub { color: var(--muted); max-width: 56ch; }
.xgrid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px; margin-top: 10px; text-align: left; width: 100%; max-width: 900px; }
.xcard { background: var(--white); border: 1px solid var(--line); border-left: 4px solid var(--gold); padding: 26px 28px; display: flex; flex-direction: column; gap: 8px; text-decoration: none; color: inherit; min-width: 0; transition: box-shadow .2s, transform .2s; }
.xcard:hover { box-shadow: 0 14px 30px rgba(31,42,68,.12); transform: translateY(-2px); }
.xcard:focus-visible { outline: 3px solid var(--gold-soft); outline-offset: 3px; }
.xcard .eyebrow { font-size: 12px; letter-spacing: 2px; }
.xcard h3 { font-size: 23px; color: var(--navy); }
.xcard .dom { font-size: 14px; color: var(--muted); overflow-wrap: anywhere; }
.xcard p.d { font-size: 16px; line-height: 1.6; }
.xcard .go { margin-top: auto; padding-top: 6px; color: var(--gold); font: 700 13px/1.4 var(--body); letter-spacing: 2px; text-transform: uppercase; }
.ext .fine2 { font-size: 13px; color: var(--muted); }
@media (prefers-reduced-motion: reduce) { .xcard, .xcard:hover { transition: none; transform: none; } }
@media (max-width: 700px) { .xgrid { grid-template-columns: 1fr; } }
"""


def demo():
    cards = "".join(
        f'<a class="xcard" href="{s["url"]}" target="_blank" rel="noopener">'
        f'<p class="eyebrow">{s["kind"]}</p><h3>{s["name"]}</h3><span class="dom">{s["domain"]}</span>'
        f'<p class="d">{s["desc"]}</p><span class="go">Visit Site ↗</span></a>' for s in SITES)
    sec = f"""
<section class="ext" id="recommended-sites">
  <div class="wrap center stack">
    <p class="eyebrow">{HEAD[0]}</p>
    <h2>{HEAD[1]}</h2>
    <hr class="rule">
    <p class="sub">{HEAD[2]}</p>
    <div class="xgrid">{cards}</div>
    <p class="fine2">These links open the other site in a new tab.</p>
  </div>
</section>
"""
    p = "demo/free_resources.html"; s = open(p).read()
    if 'id="recommended-sites"' not in s:
        s = s.replace("</main>", sec + "</main>", 1); open(p, "w").write(s)
    c = open("demo/site.css").read()
    if ".xcard {" not in c: open("demo/site.css", "a").write(CSS)


def elementor():
    def card(s):
        b = button("Visit Site ↗", s["url"], primary=False, align="left")
        b["settings"]["link"]["is_external"] = "on"
        return container([
            eyebrow(s["kind"], align="left"),
            heading(s["name"], tag="h3", size=23, mobile=21, align="left"),
            text(f'<p>{s["domain"]}</p>', color=MUTED, size=14, align="left"),
            text(f'<p>{s["desc"]}</p>', align="left", size=16, lh=1.6),
            b,
        ], width=48, inner=True, bg=WHITE, align="flex-start", gap=8, padding=pad(26, 28, 26, 28),
            extra={"border_border": "solid",
                   "border_width": {"unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "4", "isLinked": False},
                   "border_color": "#E3DCCD"})
    sec = container([
        eyebrow(HEAD[0]), heading(HEAD[1], size=36, mobile=28), divider(),
        text(f"<p>{HEAD[2]}</p>", color=MUTED, size=17),
        container([card(s) for s in SITES], direction="row", gap=24, inner=True, boxed=False, align="stretch", justify="center"),
        text("<p>These links open the other site in a new tab.</p>", color=MUTED, size=13),
    ], bg=CREAM, padding=pad(80, 20, 90, 20), gap=14, css_id="recommended-sites", extra={"boxed_width": px(960)})
    p = "richard-brokaw-free-resources-elementor.json"; d = json.load(open(p))
    d["content"] = [c for c in d["content"] if c["settings"].get("_element_id") != "recommended-sites"] + [sec]
    json.dump(d, open(p, "w"), indent=1, ensure_ascii=False)


if __name__ == "__main__":
    demo(); elementor(); print("ok")
