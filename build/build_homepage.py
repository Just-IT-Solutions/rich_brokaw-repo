"""Generates an Elementor (flexbox container) page template for the Richard Brokaw homepage."""
import json, secrets

NAVY = "#1F2A44"
NAVY_DARK = "#151D30"
GOLD = "#B8893B"
CREAM = "#F7F3EC"
WHITE = "#FFFFFF"
TEXT = "#2B2B2B"
MUTED = "#5A6070"
HEAD_FONT = "Playfair Display"
BODY_FONT = "Lato"
PLACEHOLDER = "/wp-content/plugins/elementor/assets/images/placeholder.png"


def uid():
    return secrets.token_hex(4)[:7]


def px(v):
    return {"unit": "px", "size": v, "sizes": []}


def pad(t, r, b, l):
    return {"unit": "px", "top": str(t), "right": str(r), "bottom": str(b), "left": str(l), "isLinked": False}


def typo(family, size, weight="400", mobile=None, ls=None, transform=None, lh=None, style=None):
    d = {
        "typography_typography": "custom",
        "typography_font_family": family,
        "typography_font_size": px(size),
        "typography_font_weight": weight,
    }
    if mobile:
        d["typography_font_size_mobile"] = px(mobile)
    if ls is not None:
        d["typography_letter_spacing"] = px(ls)
    if transform:
        d["typography_text_transform"] = transform
    if lh:
        d["typography_line_height"] = {"unit": "em", "size": lh, "sizes": []}
    if style:
        d["typography_font_style"] = style
    return d


def container(children, direction="column", bg=None, padding=None, width=None, boxed=True,
              align="center", justify="flex-start", gap=20, css_id=None, extra=None, inner=False):
    s = {
        "content_width": "boxed" if boxed else "full",
        "flex_direction": direction,
        "flex_align_items": align,
        "flex_justify_content": justify,
        "flex_gap": {"unit": "px", "size": gap, "column": str(gap), "row": str(gap), "isLinked": True},
    }
    if boxed and not inner:
        s["boxed_width"] = px(1140)
    if direction == "row":
        s["flex_direction_mobile"] = "column"
        s["flex_wrap"] = "wrap"
    if bg:
        s["background_background"] = "classic"
        s["background_color"] = bg
    if padding:
        s["padding"] = padding
        s["padding_mobile"] = pad(48, 20, 48, 20) if not inner else padding
    if width:
        s["width"] = {"unit": "%", "size": width, "sizes": []}
        s["width_mobile"] = {"unit": "%", "size": 100, "sizes": []}
    if css_id:
        s["_element_id"] = css_id
    if extra:
        s.update(extra)
    return {"id": uid(), "elType": "container", "settings": s, "elements": children, "isInner": inner}


def widget(wtype, settings):
    return {"id": uid(), "elType": "widget", "settings": settings, "elements": [], "widgetType": wtype}


def heading(text, tag="h2", color=NAVY, size=40, mobile=30, align="center", family=HEAD_FONT,
            weight="700", ls=None, transform=None, lh=1.2, style=None):
    s = {"title": text, "header_size": tag, "align": align, "title_color": color}
    s.update(typo(family, size, weight, mobile, ls, transform, lh, style))
    return widget("heading", s)


def eyebrow(text, color=GOLD, align="center"):
    return heading(text, tag="p", color=color, size=14, mobile=13, align=align, family=BODY_FONT,
                   weight="700", ls=3, transform="uppercase", lh=1.4)


def text(html, color=TEXT, size=18, align="center", lh=1.7, style=None):
    s = {"editor": html, "align": align, "text_color": color}
    s.update(typo(BODY_FONT, size, "400", 16, None, None, lh, style))
    return widget("text-editor", s)


def button(label, url, primary=True, align="center", on_dark=False):
    if primary:
        bg, fg, border, hbg, hfg = GOLD, WHITE, GOLD, NAVY_DARK if not on_dark else WHITE, WHITE if not on_dark else NAVY
    else:
        bg, fg = "rgba(0,0,0,0)", (WHITE if on_dark else NAVY)
        border = WHITE if on_dark else NAVY
        hbg, hfg = (WHITE, NAVY) if on_dark else (NAVY, WHITE)
    s = {
        "text": label,
        "link": {"url": url, "is_external": "", "nofollow": "", "custom_attributes": ""},
        "align": align,
        "align_mobile": "center",
        "background_color": bg,
        "button_text_color": fg,
        "button_background_hover_color": hbg,
        "hover_color": hfg,
        "border_border": "solid",
        "border_width": {"unit": "px", "top": "2", "right": "2", "bottom": "2", "left": "2", "isLinked": True},
        "border_color": border,
        "button_hover_border_color": hbg,
        "border_radius": {"unit": "px", "top": "2", "right": "2", "bottom": "2", "left": "2", "isLinked": True},
        "text_padding": pad(16, 32, 16, 32),
    }
    s.update(typo(BODY_FONT, 14, "700", 13, 2, "uppercase"))
    return widget("button", s)


def link_text(label, url, color=GOLD, align="left"):
    return text(f'<p><a href="{url}" style="color:{color};font-weight:700;letter-spacing:2px;'
                f'text-transform:uppercase;font-size:14px;text-decoration:none;">{label}</a></p>',
                color=color, size=14, align=align)


def image(alt, width_pct=100, shadow=True):
    s = {"image": {"url": PLACEHOLDER, "id": "", "alt": alt, "source": "library"},
         "image_size": "full", "align": "center",
         "width": {"unit": "%", "size": width_pct, "sizes": []}}
    if shadow:
        s.update({"image_box_shadow_box_shadow_type": "yes",
                  "image_box_shadow_box_shadow": {"horizontal": 0, "vertical": 20, "blur": 40, "spread": -10,
                                                  "color": "rgba(0,0,0,0.35)"}})
    return widget("image", s)


def divider(color=GOLD, width=80, align="center"):
    return widget("divider", {"color": color, "weight": px(2), "width": {"unit": "px", "size": width, "sizes": []},
                              "align": align, "gap": px(6)})


def spacer(h):
    return widget("spacer", {"space": px(h)})


# ---------- SECTION 2: HERO ----------
hero_text = container([
    eyebrow("Richard Brokaw", align="left"),
    heading("Listening to Jesus.<br>Living Faithfully.<br>Waiting for His Return.", tag="h1", color=WHITE,
            size=50, mobile=34, align="left", lh=1.15),
    divider(align="left"),
    text("<p>Teaching the Word of God. Making disciples. Helping believers hear what Christ is saying to His "
         "Ekklesia and live faithfully in His purposes.</p>", color="#D9DCE3", align="left"),
    eyebrow("Author of", color="#D9DCE3", align="left"),
    container([
        container([
            heading("My Letter to You", tag="h3", color=WHITE, size=22, mobile=20, align="left"),
            text("<p>What Jesus Is Saying to His Ekklesia</p>", color=GOLD, size=16, align="left", lh=1.4,
                 style="italic"),
        ], width=48, align="flex-start", gap=4, inner=True,
            extra={"border_border": "solid", "border_width": {"unit": "px", "top": "0", "right": "0", "bottom": "0",
                                                              "left": "3", "isLinked": False},
                   "border_color": GOLD, "padding": pad(0, 0, 0, 16)}),
        container([
            heading("Why the Rapture Tarries", tag="h3", color=WHITE, size=22, mobile=20, align="left"),
            text("<p>What God Is Doing While We Wait for Christ's Return</p>", color=GOLD, size=16, align="left",
                 lh=1.4, style="italic"),
        ], width=48, align="flex-start", gap=4, inner=True,
            extra={"border_border": "solid", "border_width": {"unit": "px", "top": "0", "right": "0", "bottom": "0",
                                                              "left": "3", "isLinked": False},
                   "border_color": GOLD, "padding": pad(0, 0, 0, 16)}),
    ], direction="row", align="flex-start", gap=24, inner=True, boxed=False),
    spacer(8),
    container([
        button("Explore the Books", "/books/", align="left"),
        button("Free Resources", "/free_resources/", primary=False, on_dark=True, align="left"),
    ], direction="row", gap=16, inner=True, boxed=False, align="center"),
], width=55, align="flex-start", gap=18, inner=True)

hero = container([
    container([image("Richard Brokaw headshot", 100)], width=40, inner=True),
    hero_text,
], direction="row", bg=NAVY, padding=pad(90, 20, 90, 20), gap=60, css_id="hero")

# ---------- SECTION 3: WHY I WRITE ----------
why = container([
    eyebrow("Why I Write"),
    heading("More Than Information About God", size=36, mobile=28),
    divider(),
    text("<p>For more than 45 years, I have had the privilege of teaching the Word of God. For more than 15 years, "
         "I have also had the privilege of discipling men coming from prison and drug rehabilitation.</p>"
         "<p>Those years have taught me something important: people don't simply need more information about God. "
         "They need to discover what it means to follow Jesus Christ, grow in spiritual maturity, and live out the "
         "purposes of God.</p>"
         "<p><strong>That conviction is at the heart of my writing and ministry.</strong></p>"),
    button("Learn More About Richard", "/about-richard/", primary=False),
], bg=CREAM, padding=pad(90, 20, 90, 20), gap=18, css_id="why-i-write",
    extra={"boxed_width": px(780)})

# ---------- SECTION 4: TWO BOOKS. ONE BURDEN. ----------
def book_card(title, question, body_html, url):
    return container([
        image(f"{title} book cover", 70),
        eyebrow(question, align="left"),
        heading(title, tag="h3", size=30, mobile=26, align="left"),
        text(body_html, align="left", size=17),
        link_text("Read About the Book →", url),
    ], width=46, align="flex-start", gap=12, inner=True, bg=WHITE, padding=pad(40, 36, 40, 36),
        extra={"border_border": "solid",
               "border_width": {"unit": "px", "top": "4", "right": "0", "bottom": "0", "left": "0",
                                "isLinked": False},
               "border_color": GOLD,
               "box_shadow_box_shadow_type": "yes",
               "box_shadow_box_shadow": {"horizontal": 0, "vertical": 10, "blur": 30, "spread": 0,
                                         "color": "rgba(31,42,68,0.10)"}})

two_books = container([
    eyebrow("The Books"),
    heading("Two Books. One Burden.", size=42, mobile=30),
    divider(),
    container([
        book_card("My Letter to You", "What is Jesus saying to His Ekklesia?",
                  "<p>The Seven Letters of Revelation are the words of Jesus Christ to His people.</p>"
                  "<p><em>My Letter to You</em> invites us to listen carefully to what Jesus said to the seven "
                  "churches, and to consider what He is saying to His Ekklesia today.</p>",
                  "/books/#my-letter-to-you"),
        book_card("Why the Rapture Tarries", "What is God doing while we wait?",
                  "<p>Christ promised that He would return. But what if the waiting itself has a purpose?</p>"
                  "<p><em>Why the Rapture Tarries</em> explores what God is accomplishing in His Ekklesia while we "
                  "wait for Christ's return.</p>",
                  "/why-the-rapture-tarries/"),
    ], direction="row", gap=40, inner=True, boxed=False, align="stretch", justify="center"),
    spacer(10),
    container([
        heading("One book asks us to listen to what Jesus is saying.<br>"
                "The other asks us to consider what God is accomplishing while we wait.",
                tag="p", size=24, mobile=20, weight="400", style="italic", lh=1.5),
        divider(width=120),
        text("<p>Together they call the Ekklesia to <strong>hear</strong> Christ and to <strong>persevere</strong> "
             "until He comes.</p>", color=MUTED, size=17),
    ], inner=True, gap=14, padding=pad(10, 20, 0, 20)),
], bg="#EEF0F4", padding=pad(90, 20, 90, 20), gap=24, css_id="books")

# ---------- SECTION 5: THE EKKLESIA ----------
ekklesia = container([
    eyebrow("The Ekklesia"),
    heading("Called. Formed. Matured. Sent.", color=WHITE, size=44, mobile=30),
    divider(),
    text("<p>The Ekklesia is more than a gathering in a building. It is the people God has called to Himself, "
         "formed through His Word, matured through discipleship, and sent to live out His purposes.</p>"
         "<p>My teaching and writing are centered on helping believers understand what it means to follow Christ, "
         "mature in Him, and faithfully participate in what God is doing in the earth.</p>",
         color="#D9DCE3", size=19),
    button("Discover the Message →", "/about-richard/#the-message", primary=True),
], bg=NAVY_DARK, padding=pad(100, 20, 100, 20), gap=20, css_id="ekklesia",
    extra={"boxed_width": px(820)})

# ---------- SECTION 6: FEATURED BOOK ----------
featured = container([
    container([image("Why the Rapture Tarries book cover", 80)], width=40, inner=True),
    container([
        eyebrow("New Book", align="left"),
        heading("Why the Rapture Tarries", tag="h2", size=42, mobile=30, align="left"),
        heading("The Rapture Is Not Delayed.<br>God Is Finishing What He Started.", tag="h3", color=GOLD,
                size=20, mobile=18, align="left", family=BODY_FONT, weight="700", ls=1.5, transform="uppercase",
                lh=1.4),
        divider(align="left"),
        text("<p>Christians have waited generations for Christ's return. But what if the question isn't simply "
             "<em>when</em> He will return? What if the waiting itself has a purpose?</p>"
             "<p><em>Why the Rapture Tarries</em> explores what God is accomplishing in His Ekklesia while we wait "
             "for Christ's return.</p>", align="left"),
        button("Discover Why the Rapture Tarries", "/why-the-rapture-tarries/", align="left"),
        spacer(6),
        eyebrow("Coming Soon", color=NAVY, align="left"),
        text("<p>Purchase options will be listed here at release. "
             "<a href=\"#join\" style=\"color:#B8893B;font-weight:700;\">Join the mailing list</a> "
             "to be notified the day it's available.</p>", color=MUTED, size=16, align="left"),
    ], width=55, align="flex-start", gap=14, inner=True),
], direction="row", bg=WHITE, padding=pad(100, 20, 100, 20), gap=60, css_id="featured-book")

# ---------- SECTION 7: FREE RESOURCES + MAILING LIST ----------
def resource_card(title, body, label, url, soon=False):
    kids = [
        heading(title, tag="h3", size=22, mobile=20, align="left"),
        divider(width=50, align="left"),
        text(f"<p>{body}</p>", align="left", size=16),
    ]
    kids.append(eyebrow("Coming Soon", color=MUTED, align="left") if soon else link_text(label, url))
    return container(kids, width=31, align="flex-start", gap=10, inner=True, bg=WHITE,
                     padding=pad(36, 30, 36, 30),
                     extra={"border_border": "solid",
                            "border_width": {"unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1",
                                             "isLinked": True},
                            "border_color": "#E3DCCD"})

signup_html = """<div class="rb-signup-placeholder" style="max-width:560px;margin:0 auto;padding:28px;border:2px dashed #B8893B;border-radius:4px;background:#fff;text-align:center;font-family:Lato,sans-serif;color:#5A6070;">
<!-- REPLACE THIS WHOLE BLOCK with your MailerLite embedded form code (or the shortcode from the MailerLite plugin in a Shortcode widget). -->
<strong style="color:#1F2A44;">MailerLite signup form goes here</strong><br>
<span style="font-size:14px;">First name + Email + "Join the List" button</span>
</div>"""

resources = container([
    eyebrow("Free Resources"),
    heading("Go Deeper in the Word", size=42, mobile=30),
    divider(),
    text("<p>Bible studies, discipleship resources, teaching materials, and practical tools designed to help you "
         "move beyond simply reading Scripture to living it.</p>", color=MUTED),
    container([
        resource_card("Seven Letters Study",
                      "A free introduction to the Seven Letters of Revelation and their message to the Ekklesia.",
                      "Download Free →", "/free_resources/#seven-letters"),
        resource_card("Waiting for Christ",
                      "A free study exploring what Scripture teaches about living faithfully while we await "
                      "Christ's return.", "Download Free →", "/free_resources/#waiting-for-christ"),
        resource_card("Small Group Resources",
                      "Leader and participant resources for churches, men's groups, and small groups.",
                      "Explore Resources →", "/free_resources/#small-groups", soon=True),
    ], direction="row", gap=30, inner=True, boxed=False, align="stretch", justify="center"),
    spacer(30),
    container([
        heading("Join the Mailing List", size=32, mobile=26, color=WHITE),
        text("<p>Receive occasional Bible teaching, new resources, ministry updates, and information about "
             "upcoming books.</p>", color="#D9DCE3", size=17),
        widget("html", {"html": signup_html}),
    ], inner=True, bg=NAVY, padding=pad(50, 30, 50, 30), gap=14, css_id="join",
        extra={"border_radius": {"unit": "px", "top": "4", "right": "4", "bottom": "4", "left": "4",
                                 "isLinked": True}}),
], bg=CREAM, padding=pad(90, 20, 90, 20), gap=20, css_id="free-resources")

# ---------- SECTION 8: DISCIPLESHIP / MINISTRY ----------
def ministry_item(icon, title, body):
    s = {"selected_icon": {"value": icon, "library": "fa-solid"}, "title_text": title, "description_text": body,
         "position": "top", "title_size": "h3", "primary_color": GOLD, "title_color": NAVY,
         "description_color": TEXT, "icon_size": px(38), "text_align": "center",
         "title_typography_typography": "custom", "title_typography_font_family": HEAD_FONT,
         "title_typography_font_size": px(22), "title_typography_font_weight": "700",
         "description_typography_typography": "custom", "description_typography_font_family": BODY_FONT,
         "description_typography_font_size": px(16),
         "description_typography_line_height": {"unit": "em", "size": 1.6, "sizes": []}}
    return container([widget("icon-box", s)], width=23, inner=True, padding=pad(20, 10, 20, 10),
                     extra={"width_tablet": {"unit": "%", "size": 47, "sizes": []}})

ministry = container([
    eyebrow("The Heart of My Ministry"),
    heading("Discipleship", size=44, mobile=32),
    divider(),
    text("<p>Helping believers grow in spiritual maturity.</p>", color=MUTED, size=19, style="italic"),
    container([
        ministry_item("fas fa-hands-helping", "Men",
                      "Walking alongside men who are seeking a new direction and a deeper relationship with Christ."),
        ministry_item("fas fa-book-open", "Teaching",
                      "Opening Scripture and helping people understand how God's Word applies to their lives."),
        ministry_item("fas fa-users", "Small Groups",
                      "Equipping leaders and groups to study Scripture and grow together."),
        ministry_item("fas fa-microphone", "Speaking",
                      "Teaching churches, men's groups, and Christian organizations."),
    ], direction="row", gap=20, inner=True, boxed=False, align="flex-start", justify="center"),
    button("Invite Richard to Speak →", "/for-churches/#speaking"),
], bg=WHITE, padding=pad(90, 20, 90, 20), gap=20, css_id="ministry")

# ---------- SECTION 9: VIDEO ----------
video = container([
    eyebrow("A Word From Richard"),
    heading("A Word From Richard", tag="h2", size=38, mobile=28, color=WHITE),
    divider(),
    widget("video", {"video_type": "youtube", "youtube_url": "https://www.youtube.com/watch?v=XHOmBV4js_E",
                     "aspect_ratio": "169", "modestbranding": "yes", "rel": "", "show_image_overlay": "",
                     "_border_radius": {"unit": "px", "top": "4", "right": "4", "bottom": "4", "left": "4",
                                        "isLinked": True}}),
], bg=NAVY, padding=pad(90, 20, 90, 20), gap=18, css_id="video",
    extra={"boxed_width": px(900)})
# eyebrow + heading say the same thing; drop the eyebrow
video["elements"].pop(0)

template = {
    "content": [hero, why, two_books, ekklesia, featured, resources, ministry, video],
    "page_settings": {"hide_title": "yes", "template": "elementor_header_footer"},
    "version": "0.4",
    "title": "Richard Brokaw – Homepage",
    "type": "page",
}

with open("richard-brokaw-homepage-elementor.json", "w") as f:
    json.dump(template, f, indent=1, ensure_ascii=False)
print("ok", sum(1 for _ in json.dumps(template)))
