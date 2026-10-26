"""About Richard page: Elementor template + demo page. Richard's text is used verbatim."""
import json, html, re
from elementor_lib import *

P_OPEN = ("I am a disciple of Christ and do not call myself a Christian. A Christian can mean many things today, "
          "but a disciple of Christ can mean one thing: you follow Jesus Christ. That is who I am.")
P_LISTEN = ("Because that is true, I listen to what the Holy Spirit tells me, and I do it. That has got me into some "
            "conflicts with people, and yet, when I stood my ground on what the Holy Spirit told me, it caused a shift "
            "in my soul. I no longer sought to please man, but to please God.")
P_DESTINY = ("This has led me in the past decade into a new realm of my destiny. I wrote my first book in January "
             "2025, <em>My Letter to You</em>, based on the Seven Letters to the Churches. This has been after over "
             "45 years of teaching the Word of God. Then, I finished my second book in September 2026, <em>Why the "
             "Rapture Tarries</em>. I sense there is more to come, and so I will continue this journey with the Lord "
             "to do what He tells me to do.")
P_MEN = ("For nearly twenty years, I have been discipling men coming from prison and drug rehabilitation. This "
         "experience has marked me as I have witnessed miraculous transformations in men who came in one way and, "
         "six to nine months later, went out another way—men who now have life, hope, and love. Many are walking "
         "out their destiny.")
P_GOAL = ("This has deeply affected the direction of my life. I have no other goal in life than to see the fruit of "
          "believers coming into the fullness of Christ through discipleship. As Paul wrote in Colossians 1:25-29, "
          "it bears witness in my soul.")
COL_1 = ("Of this Ekklesia, I have been made a disciple maker, according to the stewardship from God bestowed on me, "
         "for your benefit, so that I might fully carry out the teaching of God's Word, that is, the mystery that has "
         "been hidden in past ages and generations, but has now been manifest in the saints. To whom God willed to "
         "make known the riches of the glory of this mystery, which is Christ in you, the hope of Glory! We proclaim "
         "Christ!")
COL_2 = ("Admonishing every man, teaching every man in wisdom, so that we present every man fully grown in Christ. "
         "For this purpose, I labor, striving according to His power that works mightily in me.")
PULL = "Men who came in one way and, six to nine months later, went out another way."

MILESTONES = [
    ("45+ years", "teaching the Word of God"),
    ("Nearly 20 years", "discipling men from prison and drug rehabilitation"),
    ("January 2025", "<em>My Letter to You</em>"),
    ("September 2026", "<em>Why the Rapture Tarries</em> completed"),
]

# ---------------- ELEMENTOR ----------------
hero = container([
    container([image("Richard Brokaw portrait", 100)], width=38, inner=True),
    container([
        eyebrow("About Richard", align="left"),
        heading("A Disciple of Christ", tag="h1", color=WHITE, size=52, mobile=36, align="left"),
        divider(align="left"),
        text(f"<p>{P_OPEN}</p>", color=WHITE, size=22, align="left", lh=1.6),
        eyebrow("Author • Teacher • Disciple-Maker", color="#D4AE6B", align="left"),
    ], width=56, inner=True, align="flex-start", gap=18),
], direction="row", bg=NAVY, padding=pad(90, 20, 90, 20), gap=60)


def milestone(big, small):
    return container([
        heading(big, tag="p", size=26, mobile=24, align="left", color=NAVY),
        text(f"<p>{small}</p>", color=MUTED, size=15, align="left", lh=1.5),
    ], width=23, inner=True, align="flex-start", gap=4,
        extra={"border_border": "solid",
               "border_width": {"unit": "px", "top": "2", "right": "0", "bottom": "0", "left": "0", "isLinked": False},
               "border_color": GOLD, "padding": pad(14, 0, 0, 0),
               "width_tablet": {"unit": "%", "size": 47, "sizes": []}})

milestones = container([milestone(*m) for m in MILESTONES], direction="row", gap=24, bg=WHITE,
                       padding=pad(50, 20, 50, 20), align="flex-start")

story = container([
    eyebrow("Pleasing God, Not Man", align="left"),
    text(f"<p>{P_LISTEN}</p>", align="left", size=19, lh=1.8),
    spacer(16),
    eyebrow("A New Realm of Destiny", align="left"),
    text(f"<p>{P_DESTINY}</p>", align="left", size=19, lh=1.8),
], bg=CREAM, padding=pad(80, 20, 80, 20), gap=14, align="flex-start", extra={"boxed_width": px(760)})

men = container([
    container([
        eyebrow("Discipling Men", align="left"),
        heading("Life, Hope, and Love", size=38, mobile=28, align="left"),
        divider(align="left"),
        text(f"<p>{P_MEN}</p>", align="left", size=19, lh=1.8),
    ], width=56, inner=True, align="flex-start", gap=14),
    container([
        heading(f"“{PULL}”", tag="p", size=28, mobile=22, weight="400", style="italic", align="left", lh=1.4),
    ], width=38, inner=True, align="flex-start",
        extra={"border_border": "solid",
               "border_width": {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "3", "isLinked": False},
               "border_color": GOLD, "padding": pad(6, 0, 6, 28)}),
], direction="row", bg=WHITE, padding=pad(90, 20, 90, 20), gap=60, align="center")

message = container([
    eyebrow("The Message"),
    heading("Christ in You, the Hope of Glory", color=WHITE, size=42, mobile=30),
    divider(),
    text(f"<p>{P_GOAL}</p>", color="#D9DCE3", size=19),
    spacer(10),
    text(f"<p>“{COL_1}</p><p>{COL_2}”</p>", color=WHITE, size=21, lh=1.75, style="italic"),
    eyebrow("Colossians 1:25-29", color="#D4AE6B"),
], bg=NAVY_DARK, padding=pad(100, 20, 100, 20), gap=16, css_id="the-message", extra={"boxed_width": px(820)})

next_steps = container([
    eyebrow("Continue"),
    heading("Read, Study, or Invite Richard", size=36, mobile=28),
    divider(),
    container([
        button("Explore the Books", "/books/"),
        button("Free Resources", "/free_resources/", primary=False),
        button("Invite Richard to Speak", "/for-churches/#speaking", primary=False),
    ], direction="row", gap=16, inner=True, boxed=False, justify="center"),
], bg=CREAM, padding=pad(80, 20, 90, 20), gap=16)

template = {
    "content": [hero, milestones, story, men, message, next_steps],
    "page_settings": {"hide_title": "yes", "template": "elementor_header_footer"},
    "version": "0.4", "title": "Richard Brokaw – About Richard", "type": "page",
}
with open("richard-brokaw-about-elementor.json", "w") as f:
    json.dump(template, f, indent=1, ensure_ascii=False)

# ---------------- DEMO PAGE ----------------
import build_demo_pages as d

css = """
.ab-hero .grid { display: grid; grid-template-columns: 4fr 5.6fr; gap: 60px; align-items: center; }
.ab-hero .photo { aspect-ratio: 4 / 5; }
.ab-hero h1 { font-size: clamp(36px, 4.8vw, 52px); }
.ab-hero .open { font: 400 clamp(19px, 2vw, 22px)/1.6 var(--display); color: var(--white); max-width: 34ch; }
.miles { padding-block: 50px; }
.miles .wrap { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; }
.mile { border-top: 2px solid var(--gold); padding-top: 14px; min-width: 0; }
.mile b { display: block; font: 700 26px/1.2 var(--display); color: var(--navy); }
.mile span { display: block; color: var(--muted); font-size: 15px; line-height: 1.5; margin-top: 4px; }
.story { background: var(--cream); }
.story .wrap { max-width: 760px; display: flex; flex-direction: column; gap: 14px; }
.story p:not(.eyebrow) { font-size: 19px; line-height: 1.8; }
.story .eyebrow + p { margin-bottom: 22px; }
.men .grid { display: grid; grid-template-columns: 5.6fr 4fr; gap: 60px; align-items: center; }
.men h2 { font-size: clamp(28px, 3.6vw, 38px); color: var(--navy); }
.men .copy { display: flex; flex-direction: column; gap: 14px; }
.men .copy p:not(.eyebrow) { font-size: 19px; line-height: 1.8; }
.men blockquote { margin: 0; border-left: 3px solid var(--gold); padding: 6px 0 6px 28px; font: italic 400 clamp(22px, 2.6vw, 28px)/1.4 var(--display); color: var(--navy); }
.msg { background: var(--navy-dark); }
.msg h2 { font-size: clamp(30px, 4vw, 42px); }
.msg .goal { font-size: 19px; max-width: 62ch; }
.msg blockquote { margin: 18px 0 0; font: italic 400 clamp(19px, 2.1vw, 21px)/1.75 var(--display); color: var(--white); max-width: 62ch; display: flex; flex-direction: column; gap: 14px; }
.msg cite { font: 700 14px var(--body); letter-spacing: 3px; text-transform: uppercase; color: var(--gold-soft); font-style: normal; }
.next h2 { font-size: clamp(28px, 3.4vw, 36px); color: var(--navy); }
.next { background: var(--cream); }
@media (max-width: 900px) {
  .ab-hero .grid, .men .grid { grid-template-columns: 1fr; gap: 40px; }
  .ab-hero .photo { max-width: 400px; width: 100%; margin: 0 auto; }
  .miles .wrap { grid-template-columns: 1fr 1fr; }
}
@media (max-width: 480px) { .miles .wrap { grid-template-columns: 1fr; } }
"""
with open("demo/site.css", "a") as f:
    f.write(css)

page = d.HEAD.format(title="About Richard · Richard Brokaw",
                     bar="Design preview of the About Richard page. The portrait is a placeholder.") + f"""
<section class="dark ab-hero">
  <div class="wrap grid">
    <div class="ph photo">Richard Headshot<small>Portrait goes here</small></div>
    <div class="stack">
      <p class="eyebrow">About Richard</p>
      <h1>A Disciple of Christ</h1>
      <hr class="rule">
      <p class="open">{P_OPEN}</p>
      <p class="eyebrow" style="color:var(--gold-soft)">Author • Teacher • Disciple-Maker</p>
    </div>
  </div>
</section>

<section class="miles" aria-label="Milestones">
  <div class="wrap">
    {''.join(f'<div class="mile"><b>{b}</b><span>{s}</span></div>' for b, s in MILESTONES)}
  </div>
</section>

<section class="story">
  <div class="wrap">
    <p class="eyebrow">Pleasing God, Not Man</p>
    <p>{P_LISTEN}</p>
    <p class="eyebrow">A New Realm of Destiny</p>
    <p>{P_DESTINY}</p>
  </div>
</section>

<section class="men">
  <div class="wrap grid">
    <div class="copy">
      <p class="eyebrow">Discipling Men</p>
      <h2>Life, Hope, and Love</h2>
      <hr class="rule">
      <p>{P_MEN}</p>
    </div>
    <blockquote>“{PULL}”</blockquote>
  </div>
</section>

<section class="dark msg" id="the-message">
  <div class="wrap narrow center stack">
    <p class="eyebrow">The Message</p>
    <h2>Christ in You, the Hope of Glory</h2>
    <hr class="rule">
    <p class="goal">{P_GOAL}</p>
    <blockquote><p>“{COL_1}</p><p>{COL_2}”</p></blockquote>
    <cite>Colossians 1:25-29</cite>
  </div>
</section>

<section class="next">
  <div class="wrap center stack">
    <p class="eyebrow">Continue</p>
    <h2>Read, Study, or Invite Richard</h2>
    <hr class="rule">
    <div class="btn-row" style="justify-content:center">
      <a class="btn" href="index.html#books">Explore the Books</a>
      <a class="btn ghost" href="free_resources.html">Free Resources</a>
      <a class="btn ghost" href="index.html#ministry">Invite Richard to Speak</a>
    </div>
  </div>
</section>
""" + d.FOOT
open("demo/about-richard.html", "w").write(page)

# point "About Richard" links at the new page everywhere
for p in ["richard-brokaw-demo.html", "demo/free_resources.html", "demo/resource-library.html", "demo/about-richard.html"]:
    s = open(p).read()
    s = s.replace('<a href="#why-i-write">About Richard</a>', '<a href="about-richard.html">About Richard</a>')
    s = s.replace('<a href="index.html#why-i-write">About Richard</a>', '<a href="about-richard.html">About Richard</a>')
    s = s.replace('href="#top">Learn More About Richard', 'href="about-richard.html">Learn More About Richard')
    s = s.replace('href="#top">Discover the Message', 'href="about-richard.html#the-message">Discover the Message')
    open(p, "w").write(s)
print("ok")
