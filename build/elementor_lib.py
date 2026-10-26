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

