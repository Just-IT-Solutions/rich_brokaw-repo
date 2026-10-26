"""Books page: demo (demo/books.html) + Elementor template. Sample pages are placeholders until Richard sends text."""
import json, html
from elementor_lib import *

AMAZON_MLTY = "https://www.amazon.com/s?k=9798765260692"   # replace with the exact product link when available

BOOKS = [
    dict(slug="my-letter-to-you", title="My Letter to You",
         subtitle="What Jesus' Seven Letters Reveal About Your Walk, Your Purpose, and Your Spiritual Authority",
         question="What is Jesus saying to His Ekklesia?",
         cover="my-letter-to-you-cover.jpg", alt="My Letter to You by Richard Brokaw, book cover",
         desc=["The Seven Letters of Revelation are the words of Jesus Christ to His people.",
               "<em>My Letter to You</em> invites us to listen carefully to what Jesus said to the seven churches, "
               "and to consider what He is saying to His Ekklesia today."],
         details=[("Format", "Paperback"), ("ISBN-13", "979-8765260692")],
         status="available", buy=AMAZON_MLTY),
    dict(slug="why-the-rapture-tarries", title="Why the Rapture Tarries",
         subtitle="What If Jesus Isn't Waiting to Take His Church Out But Waiting to Finish What He Started?",
         question="What is God doing while we wait?",
         cover="why-the-rapture-tarries-cover.jpg", alt="Why the Rapture Tarries by Richard Brokaw, book cover",
         desc=["Christians have waited generations for Christ's return. But what if the question isn't simply "
               "<em>when</em> He will return? What if the waiting itself has a purpose?",
               "<em>Why the Rapture Tarries</em> explores what God is accomplishing in His Ekklesia while we wait for "
               "Christ's return."],
         details=[("Status", "Coming soon")],
         status="soon", buy=None),
]


def sample_pages(b, img_base, join_url):
    t = html.escape(b["title"])
    end_link = (f'<a href="{b["buy"]}" target="_blank" rel="noopener">Buy on Amazon</a>' if b["buy"]
                else f'<a href="{join_url}">Get Notified</a>')
    end_text = ("Enjoyed the sample? Continue reading the full book." if b["buy"]
                else "The full book is coming soon. Join the mailing list to hear the day it's available.")
    ph = lambda n: (f'<div class="rb-ph">Sample text, page {n}.<br>About 170 words fit on each page.</div>'
                    '')
    pages = [
        ("title", f'<h4>A Free Sample</h4><h3>{t}</h3><hr><p class="sub">{html.escape(b["subtitle"])}</p><p>Richard Brokaw</p>'),
        ("", f'<h4>Chapter One</h4><h3>Chapter Title</h3>{ph(1)}'),
        ("", ph(2)), ("", ph(3)), ("", ph(4)),
        ("end", f'<h4>End of Sample</h4><h3>Keep Reading</h3><p>{end_text}</p>{end_link}'),
    ]
    body = "\n".join(f'    <section class="rb-page" data-kind="{k}">{h}</section>' for k, h in pages)
    return (f'<div class="rb-book" data-title="{t}" data-cover="{img_base}/{b["cover"]}" data-cover-alt="{html.escape(b["alt"])}">\n'
            f'  <div class="rb-src">\n{body}\n  </div>\n</div>')


def buy_html(b, join_url, wp=False):
    if b["buy"]:
        return (f'<a class="btn rb-buy" href="{b["buy"]}" target="_blank" rel="noopener">Buy on Amazon</a>'
                f'<p class="rb-note">Opens Amazon in a new tab</p>')
    return (f'<span class="btn rb-buy is-soon" aria-disabled="true">Coming Soon to Amazon</span>'
            f'<p class="rb-note"><a href="{join_url}">Join the mailing list</a> to hear the day it\'s available.</p>')


def details_html(b):
    return '<dl class="rb-details">' + "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in b["details"]) + "</dl>"


PAGE_CSS = """
.bk-hero { text-align: center; }
.bk-hero h1 { font-size: clamp(34px, 4.6vw, 50px); }
.bk-hero blockquote { margin: 0 auto; max-width: 40ch; font: italic 400 clamp(19px, 2.2vw, 22px)/1.5 var(--display); color: var(--on-dark); }
.bk-jump { display: flex; flex-wrap: wrap; gap: 14px; justify-content: center; margin-top: 8px; }
.bk { padding-block: 80px 90px; }
.bk.alt { background: var(--cream); }
.bk-head { text-align: center; display: flex; flex-direction: column; align-items: center; gap: 10px; margin-bottom: 26px; }
.bk-head h2 { font-size: clamp(30px, 4vw, 42px); color: var(--navy); }
.bk-head .sub { font: italic 400 clamp(17px, 2vw, 20px)/1.45 var(--display); color: var(--muted); max-width: 46ch; }
.bk-body { max-width: 680px; margin: 30px auto 0; display: flex; flex-direction: column; align-items: center; gap: 16px; text-align: center; }
.bk-body .copy { display: flex; flex-direction: column; gap: 14px; }
.rb-buy { min-width: 260px; text-align: center; }
.rb-buy.is-soon { background: transparent; color: var(--muted); border-color: #C9BFA9; cursor: default; }
.rb-buy.is-soon:hover { background: transparent; border-color: #C9BFA9; }
.rb-note { font-size: 14px; color: var(--muted); }
.rb-note a { color: var(--gold); font-weight: 700; }
.rb-details { display: flex; flex-wrap: wrap; justify-content: center; gap: 8px 28px; margin: 4px 0 0; font-size: 14px; color: var(--muted); }
.rb-details div { display: flex; gap: 8px; }
.rb-details dt { font-weight: 700; color: var(--navy); }
.rb-details dd { margin: 0; font-variant-numeric: tabular-nums; }
.bk-close { text-align: center; }
.bk-close h2 { font-size: clamp(26px, 3.4vw, 34px); color: var(--navy); }
"""

if __name__ == "__main__":
    import re, types
    _a = open("demo/about-richard.html").read()
    _head = _a[:_a.index("<main>") + len("<main>\n")]
    _head = re.sub(r"<title>.*?</title>", "<title>{title}</title>", _head)
    _head = re.sub(r'<div class="demo-bar">.*?</div>', '<div class="demo-bar">{bar}</div>', _head)
    _head = _head.replace("{", "{{").replace("}", "}}").replace("{{title}}", "{title}").replace("{{bar}}", "{bar}")
    d = types.SimpleNamespace(HEAD=_head, FOOT=_a[_a.index("</main>"):])
    # ---------- DEMO ----------
    def book_section(b, alt):
        soon = '<p class="eyebrow">New · Coming Soon</p>' if b["status"] == "soon" else '<p class="eyebrow">Available Now</p>'
        return f"""
<section class="bk{' alt' if alt else ''}" id="{b['slug']}">
  <div class="wrap">
    <div class="bk-head">
      {soon}
      <h2>{b['title']}</h2>
      <p class="sub">{b['subtitle']}</p>
      <hr class="rule">
    </div>
    {sample_pages(b, 'images', 'index.html#join')}
    <div class="bk-body">
      <p class="eyebrow">{b['question']}</p>
      <div class="copy">{''.join(f'<p>{p}</p>' for p in b['desc'])}</div>
      {buy_html(b, 'index.html#join')}
      {details_html(b)}
    </div>
  </div>
</section>"""

    page = d.HEAD.format(title="Books · Richard Brokaw",
                         bar="Design preview of the Books page. Sample pages are placeholders until the text arrives.")
    page = page.replace('<link rel="stylesheet" href="site.css">',
                        '<link rel="stylesheet" href="site.css">\n<link rel="stylesheet" href="rb-book.css">')
    page += f"""
<section class="dark bk-hero">
  <div class="wrap stack center" style="max-width:860px">
    <p class="eyebrow">Books</p>
    <h1>Two Books. One Burden.</h1>
    <hr class="rule">
    <blockquote>One book asks us to listen to what Jesus is saying. The other asks us to consider what God is accomplishing while we wait.</blockquote>
    <div class="bk-jump">
      <a class="btn ghost" href="#my-letter-to-you">My Letter to You</a>
      <a class="btn ghost" href="#why-the-rapture-tarries">Why the Rapture Tarries</a>
    </div>
  </div>
</section>
{book_section(BOOKS[0], True)}
{book_section(BOOKS[1], False)}
<section class="bk-close alt" style="background:var(--cream)">
  <div class="wrap stack center">
    <p class="eyebrow">Go Deeper</p>
    <h2>Free Studies While You Read</h2>
    <p style="max-width:56ch;color:var(--muted)">Six free studies on knowing God, maturity in Christ, and discipleship.</p>
    <a class="btn" href="free_resources.html">Free Resources</a>
  </div>
</section>
""" + d.FOOT.replace("</body>", '<script src="rb-book.js"></script>\n</body>')
    open("demo/books.html", "w").write(page)
    with open("demo/site.css", "a") as f:
        f.write(PAGE_CSS)

    # ---------- ELEMENTOR ----------
    IMG = "/wp-content/uploads/site-images"
    css = open("books/rb-book.css").read()
    js = open("books/rb-book.js").read()
    assets = widget("html", {"html": f"<style>\n{css}\n{PAGE_CSS.replace('var(--cream)', '#F7F3EC').replace('var(--navy)', '#1F2A44').replace('var(--muted)', '#5A6070').replace('var(--gold)', '#B8893B').replace('var(--display)', 'Playfair Display, Georgia, serif').replace('var(--on-dark)', '#D9DCE3')}\n</style>\n<script>\n{js}\n</script>"})

    hero = container([
        assets,
        eyebrow("Books"),
        heading("Two Books. One Burden.", tag="h1", color=WHITE, size=50, mobile=34),
        divider(),
        heading("One book asks us to listen to what Jesus is saying. The other asks us to consider what God is "
                "accomplishing while we wait.", tag="p", size=22, mobile=19, weight="400", style="italic",
                color="#D9DCE3", lh=1.5),
        container([button("My Letter to You", "#my-letter-to-you", primary=False, on_dark=True),
                   button("Why the Rapture Tarries", "#why-the-rapture-tarries", primary=False, on_dark=True)],
                  direction="row", gap=14, inner=True, boxed=False, justify="center"),
    ], bg=NAVY, padding=pad(90, 20, 80, 20), gap=16, extra={"boxed_width": px(860)})

    def el_book(b, bg):
        buy = (button("Buy on Amazon", b["buy"]) if b["buy"]
               else heading("Coming Soon to Amazon", tag="p", size=14, family=BODY_FONT, weight="700", ls=2,
                            transform="uppercase", color=MUTED))
        if b["buy"]:
            buy["settings"]["link"]["is_external"] = "on"
            buy["settings"]["link"]["nofollow"] = "on"
        kids = [
            eyebrow("Available Now" if b["status"] == "available" else "New · Coming Soon"),
            heading(b["title"], size=42, mobile=30),
            heading(b["subtitle"], tag="p", size=20, mobile=17, weight="400", style="italic", color=MUTED, lh=1.45),
            divider(),
            widget("html", {"html": sample_pages(b, IMG, "/#join")}),
            eyebrow(b["question"]),
            text("".join(f"<p>{p}</p>" for p in b["desc"]), size=18),
            buy,
        ]
        if b["buy"]:
            kids.append(text("<p>Opens Amazon in a new tab</p>", color=MUTED, size=14))
        else:
            kids.append(text('<p><a href="/#join" style="color:#B8893B;font-weight:700">Join the mailing list</a> '
                             "to hear the day it's available.</p>", color=MUTED, size=14))
        kids.append(text(" · ".join(f"<strong>{k}</strong> {v}" for k, v in b["details"]), color=MUTED, size=14))
        return container(kids, bg=bg, padding=pad(80, 20, 90, 20), gap=14, css_id=b["slug"],
                         extra={"boxed_width": px(760)})

    close = container([
        eyebrow("Go Deeper"),
        heading("Free Studies While You Read", size=34, mobile=26),
        text("<p>Six free studies on knowing God, maturity in Christ, and discipleship.</p>", color=MUTED),
        button("Free Resources", "/free_resources/"),
    ], bg=CREAM, padding=pad(80, 20, 90, 20), gap=14)

    template = {"content": [hero, el_book(BOOKS[0], CREAM), el_book(BOOKS[1], WHITE), close],
                "page_settings": {"hide_title": "yes", "template": "elementor_header_footer"},
                "version": "0.4", "title": "Richard Brokaw – Books", "type": "page"}
    json.dump(template, open("richard-brokaw-books-elementor.json", "w"), indent=1, ensure_ascii=False)
    print("ok")
