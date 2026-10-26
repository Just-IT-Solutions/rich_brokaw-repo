"""Elementor templates for /free_resources/ (signup-gated) and /resource-library/ (downloads after signup)."""
import json
from elementor_lib import *

BASE = "/wp-content/uploads/resources"

GROUPS = [
    ("Foundations", "Where every disciple begins: who God is, and the ground we stand on.", [
        ("jesus-christ-our-foundation", "Jesus Christ, Our Foundation", "Daily Declaration · 1 page",
         "A one-page declaration built on 1 Corinthians 3:11. Read it each morning to rest your faith on what "
         "Christ has finished, not on anything you can produce."),
        ("the-imperative-of-knowing-god", "The Imperative of Knowing God", "Teaching · 1 page",
         "Every life is shaped by one question: who do you believe God is? A short teaching on why knowing God "
         "determines the quality of your life."),
    ]),
    ("Growing to Maturity", "Studies for believers who want to move from milk to meat.", [
        ("stages-of-maturity-in-christ", "Stages of Maturity in Christ", "Word Study · 1 page",
         "Five New Testament Greek words that trace spiritual growth, from brephos, the newborn babe, to "
         "huiothesia, the son placed with full authority."),
        ("the-parable-of-the-sower", "The Parable of the Sower", "Study Chart · 1 page",
         "A chart of Matthew 13 and Mark 4 that matches each soil to its enemy, what it targets, and how long the "
         "Word survives there, with Scriptures for each."),
        ("our-inheritance-from-god", "Our Inheritance from God", "Meditation · 2 pages",
         "A meditation on Ephesians 1 and Romans 8: what the Father has given His children in Christ, and why no "
         "believer should leave it on the table."),
    ]),
    ("For Men", "From over 15 years of discipling men.", [
        ("becoming-a-man", "Becoming a Man", "For Men · 1 page",
         "Drawing on Daniel 3 and 1 Corinthians 11:1, a challenge to set aside the world's idea of manhood and "
         "become the man God planned."),
    ]),
]

COMING = [
    ("Seven Letters Study", "A free introduction to the Seven Letters of Revelation and their message to the Ekklesia."),
    ("Waiting for Christ", "A study on what Scripture teaches about living faithfully while we await Christ's return."),
    ("Small Group Resources", "Leader and participant guides for churches, men's groups, and small groups."),
]


def thumb(slug, title):
    s = {"image": {"url": f"{BASE}/{slug}.png", "id": "", "alt": f"First page of {title}", "source": "url"},
         "image_size": "full", "align": "center",
         "width": {"unit": "%", "size": 100, "sizes": []},
         "height": {"unit": "px", "size": 220, "sizes": []},
         "object-fit": "cover", "object-position": "top center",
         "image_border_border": "solid",
         "image_border_width": {"unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": True},
         "image_border_color": "#E3DCCD"}
    return widget("image", s)


def card(slug, title, tag, body, mode, width=31):
    kids = [
        thumb(slug, title),
        eyebrow(tag, align="left"),
        heading(title, tag="h3", size=22, mobile=20, align="left"),
        text(f"<p>{body}</p>", align="left", size=16, lh=1.6),
    ]
    if mode == "gated":
        kids.append(link_text("Get It Free →", "#unlock"))
    else:
        kids.append(button("Download PDF", f"{BASE}/{slug}.pdf", align="left"))
    c = container(kids, width=width, align="flex-start", gap=10, inner=True, bg=WHITE,
                  padding=pad(18, 18, 28, 18),
                  extra={"border_border": "solid",
                         "border_width": {"unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1",
                                          "isLinked": True},
                         "border_color": "#E3DCCD",
                         "width_tablet": {"unit": "%", "size": 47, "sizes": []}})
    if mode != "gated":
        # make the button open the PDF in a new tab
        kids[-1]["settings"]["link"]["is_external"] = "on"
    return c


def group_block(name, blurb, items, mode, width=None):
    w = {"width": {"unit": "%", "size": width, "sizes": []}, "width_mobile": {"unit": "%", "size": 100, "sizes": []}} if width else {}
    return container([
        container([
            heading(name, tag="h2", size=30, mobile=24, align="left"),
            text(f"<p>{blurb}</p>", color=MUTED, size=16, align="left"),
        ], inner=True, align="flex-start", gap=4, boxed=False),
        container([card(*i, mode=mode, width=card_w(len(items))) for i in items], direction="row", gap=24, inner=True, boxed=False,
                  align="stretch", justify="flex-start"),
    ], inner=True, align="stretch", gap=18, boxed=False, extra=w)


def card_w(n):
    return {1: 100, 2: 48, 3: 31}[n]


def all_groups(mode):
    found, mature, men = GROUPS
    row = container([group_block(*found, mode, width=64), group_block(*men, mode, width=32)],
                    direction="row", gap=24, inner=True, boxed=False, align="flex-start")
    return [row, group_block(*mature, mode)]


signup_html = """<div class="rb-signup-placeholder" style="max-width:620px;margin:0 auto;padding:28px;border:2px dashed #B8893B;border-radius:4px;background:#fff;text-align:center;font-family:Lato,sans-serif;color:#5A6070;">
<!-- REPLACE with the MailerLite "Resource Library" form (embed code, or the plugin shortcode in a Shortcode widget).
     In MailerLite set the form's success action to redirect to /resource-library/ -->
<strong style="color:#1F2A44;">MailerLite "Resource Library" form goes here</strong><br>
<span style="font-size:14px;">First name + Email + "Send Me the Resources" button</span>
</div>"""


def steps():
    def step(n, t, b):
        return container([
            heading(str(n), tag="p", size=34, mobile=30, color=GOLD, align="left"),
            heading(t, tag="h3", size=20, mobile=19, align="left", color=WHITE),
            text(f"<p>{b}</p>", color="#D9DCE3", size=16, align="left", lh=1.6),
        ], width=31, inner=True, align="flex-start", gap=6,
            extra={"border_border": "solid",
                   "border_width": {"unit": "px", "top": "1", "right": "0", "bottom": "0", "left": "0",
                                    "isLinked": False},
                   "border_color": "rgba(255,255,255,0.18)", "padding": pad(18, 0, 0, 0)})
    return container([
        step(1, "Enter your name and email", "One short form below. It's free."),
        step(2, "Open the resource library", "You go straight to a page with all six downloads."),
        step(3, "Watch your inbox", "We'll also email you the link, plus new resources as they're released."),
    ], direction="row", gap=30, inner=True, boxed=False, align="stretch")


# ---------------- FREE RESOURCES PAGE ----------------
hero = container([
    eyebrow("Free Resources"),
    heading("Go Deeper in the Word", tag="h1", color=WHITE, size=50, mobile=34),
    divider(),
    text("<p>Bible studies, discipleship resources, teaching materials, and practical tools designed to help you "
         "move beyond simply reading Scripture to living it.</p>", color="#D9DCE3", size=19),
    button("Get All Six Free", "#unlock"),
    spacer(20),
    steps(),
], bg=NAVY, padding=pad(90, 20, 80, 20), gap=18, css_id="top", extra={"boxed_width": px(980)})

library = container(
    [eyebrow("The Library", align="left"),
     heading("Six Studies to Start With", size=40, mobile=30, align="left"),
     divider(align="left"), spacer(10)]
    + all_groups("gated"),
    bg=CREAM, padding=pad(90, 20, 90, 20), gap=36, align="stretch", css_id="library")

unlock = container([
    eyebrow("Free Resource Library"),
    heading("Send Me the Resources", color=WHITE, size=38, mobile=28),
    text("<p>Enter your name and email to open all six downloads. You'll also receive occasional Bible teaching, "
         "new resources, ministry updates, and news about upcoming books.</p>", color="#D9DCE3", size=17),
    widget("html", {"html": signup_html}),
    text("<p>No cost. Unsubscribe anytime.</p>", color="#D4AE6B", size=14),
], bg=NAVY_DARK, padding=pad(80, 20, 80, 20), gap=14, css_id="unlock", extra={"boxed_width": px(760)})


def coming_card(t, b):
    return container([
        heading(t, tag="h3", size=21, mobile=19, align="left"),
        text(f"<p>{b}</p>", align="left", size=16, lh=1.6, color=MUTED),
        eyebrow("Coming Soon", color=MUTED, align="left"),
    ], width=31, inner=True, align="flex-start", gap=8, padding=pad(28, 26, 28, 26),
        extra={"border_border": "dashed",
               "border_width": {"unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": True},
               "border_color": "#C9BFA9"})

coming = container([
    eyebrow("On the Way"),
    heading("More Resources Coming", size=34, mobile=26),
    text("<p>Subscribers hear first when these are ready.</p>", color=MUTED, size=17),
    container([coming_card(*c) for c in COMING], direction="row", gap=24, inner=True, boxed=False,
              align="stretch", justify="center"),
], bg=WHITE, padding=pad(80, 20, 90, 20), gap=14, css_id="coming-soon")

fr_template = {
    "content": [hero, library, unlock, coming],
    "page_settings": {"hide_title": "yes", "template": "elementor_header_footer"},
    "version": "0.4", "title": "Richard Brokaw – Free Resources", "type": "page",
}

# ---------------- RESOURCE LIBRARY (after signup) ----------------
lib_hero = container([
    eyebrow("Welcome"),
    heading("Your Free Resource Library", tag="h1", color=WHITE, size=46, mobile=32),
    divider(),
    text("<p>Thank you for joining. Download any of the studies below. A link to this page is also on its way to "
         "your inbox, so you can come back anytime.</p>", color="#D9DCE3", size=18),
], bg=NAVY, padding=pad(80, 20, 70, 20), gap=16, extra={"boxed_width": px(820)})

lib_body = container(
    all_groups("open")
    + [container([
        heading("Studying with a group?", tag="h3", size=24, mobile=22),
        text("<p>Richard teaches churches, men's groups, and small groups.</p>", color=MUTED, size=17),
        button("Invite Richard to Speak →", "/for-churches/#speaking", primary=False),
    ], inner=True, gap=12, padding=pad(30, 20, 0, 20))],
    bg=CREAM, padding=pad(80, 20, 90, 20), gap=40, align="stretch")

lib_template = {
    "content": [lib_hero, lib_body],
    "page_settings": {"hide_title": "yes", "template": "elementor_header_footer"},
    "version": "0.4", "title": "Richard Brokaw – Resource Library", "type": "page",
}

for name, t in [("richard-brokaw-free-resources-elementor.json", fr_template),
                ("richard-brokaw-resource-library-elementor.json", lib_template)]:
    with open(name, "w") as f:
        json.dump(t, f, indent=1, ensure_ascii=False)
    print("wrote", name)
