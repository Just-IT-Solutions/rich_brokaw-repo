# Richard Brokaw – Homepage Setup (Elementor)

## 1. Prerequisites
- **Theme:** Hello Elementor (free). It's the lightest theme for Elementor and has a built-in header/footer you can configure without Elementor Pro.
- **Plugins:** Elementor (free), MailerLite – Signup forms (official).
- **Elementor → Settings → Features:** make sure **Flexbox Container** is *Active* (default on new installs). The template is built with containers.

## 2. Create the pages (so the links work)
Pages → Add New, publish each (content can be empty for now):

| Page | Slug |
|---|---|
| Home | `home` |
| Books | `books` |
| Why the Rapture Tarries | `why-the-rapture-tarries` |
| Free Resources | `free_resources` (type it by hand; see note below) |
| About Richard | `about-richard` |
| For Churches | `for-churches` |
| Reflections | `reflections` |
| Contact | `contact` |

**Free Resources address:** WordPress fills in `free-resources` (with a hyphen) from the title. To get `/free_resources/`, open the page, go to the right sidebar → **Page → URL** (or **Permalink**), change the slug to `free_resources`, and click **Update**. Keep the title as *Free Resources*; only the address changes.

Settings → Reading → **A static page** → Homepage: *Home*. (Set Posts page to *Reflections* if Reflections will be a blog.)

## 3. Import the homepage template
1. Templates → Saved Templates → **Import Templates** → upload `richard-brokaw-homepage-elementor.json`.
2. Edit the **Home** page with Elementor → click the folder icon (Add Template) → **My Templates** → insert "Richard Brokaw – Homepage".
3. Page Settings (gear icon): Page Layout = **Elementor Full Width**, Hide Title = on. Update.

## 4. Header: name, tagline, navigation
1. Settings → General: **Site Title** = `Richard Brokaw`, **Tagline** = `Author • Teacher • Disciple-Maker`.
2. Appearance → Menus → create "Main Menu", assign to the header location, add in order:
   Home | Books | Free Resources | About Richard | For Churches | Reflections | Contact
3. Add one more **Custom Link** at the end: URL `/free_resources/`, label `Free Resources`.
   Open **Screen Options** (top right) → tick **CSS Classes** → give that last item the class `nav-cta`.
   (Sub-menu items can be dragged under any item later, so the menu grows with the ministry.)
4. Elementor → Site Settings → **Hello Theme Header & Footer**: show Site Title, Tagline and Menu; set the header background to `#1F2A44`.

## 5. Site-wide CSS
Appearance → Customize → **Additional CSS**, paste:

```css
/* Fonts used across the site */
@import url('https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Playfair+Display:ital,wght@0,700;1,400&display=swap');

body { font-family: 'Lato', sans-serif; color: #2B2B2B; }

/* Header */
.site-header { background: #1F2A44; }
.site-header .site-title a,
.site-header .site-branding .site-title { font-family: 'Playfair Display', serif; color: #fff; letter-spacing: 2px; text-transform: uppercase; }
.site-header .site-description { color: #B8893B; font-size: 13px; letter-spacing: 2px; text-transform: uppercase; }
.site-navigation a { color: #fff; font-size: 13px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; }
.site-navigation a:hover { color: #B8893B; }

/* "Free Resources" button at far right of nav */
.site-navigation .nav-cta > a {
  background: #B8893B; color: #fff !important; padding: 10px 20px; border-radius: 2px; margin-left: 12px;
}
.site-navigation .nav-cta > a:hover { background: #fff; color: #1F2A44 !important; }

/* Smooth scroll for in-page links like #join */
html { scroll-behavior: smooth; }
```

## 6. Swap in the placeholders
| Placeholder | Where | Replace with |
|---|---|---|
| Grey image, hero | Hero, left | "Richard Headshot" photo (portrait, ~900×1100px) |
| Grey image, book cards | Two Books section | Both book covers |
| Grey image, featured | Featured Book section | *Why the Rapture Tarries* cover (large) |
| Dashed box "MailerLite signup form goes here" | Join the Mailing List | MailerLite form (see below) |
| Sample YouTube video | A Word From Richard | Richard's video URL |
| "Coming Soon" + note | Featured Book | "Available Now" + buy buttons at launch |

**MailerLite:** create a group (e.g. "Website Subscribers") and an embedded form with First Name + Email. Then either paste MailerLite's embed code into the HTML widget, or delete the HTML widget and add a **Shortcode** widget with the shortcode the MailerLite plugin gives you.

## 7. Link targets used on the homepage
- Explore the Books → `/books/` · Read About the Book → `/books/#my-letter-to-you` and `/why-the-rapture-tarries/`
- Free Resources buttons/cards → `/free_resources/`
- Read Richard's Story → `/about-richard/` · Discover the Message → `/about-richard/#the-message`
- Invite Richard to Speak → `/for-churches/#speaking`

Those anchors will be created when we build each page.
