# Richard Brokaw – Author & Ministry Website

*Listening to Jesus. Living Faithfully. Waiting for His Return.*

WordPress + Elementor site for author Richard Brokaw (*My Letter to You*, *Why the Rapture Tarries*), hosted on a local Ubuntu server.

## What's here

| Folder | Contents |
|---|---|
| `demo/` | Static, clickable preview of the site. Open `demo/index.html` in any browser (no server needed). |
| `wordpress/templates/` | Elementor page templates (`.json`) to import under **Templates → Saved Templates → Import**. |
| `wordpress/uploads/` | Files the templates expect on the server: `resources/` (free PDFs + thumbnails) → `/wp-content/uploads/resources/`, `site-images/` (headshot, covers) → `/wp-content/uploads/site-images/`. |
| `wordpress/guides/` | Step-by-step setup for each page (theme, plugins, MailerLite, menus, image uploads). |
| `build/` | Python scripts that generated the templates and demo, plus the interactive book reader (`books/rb-book.*`). |

## Pages and addresses

| Page | WordPress address | Template |
|---|---|---|
| Home | `/` | `richard-brokaw-homepage-elementor.json` |
| Books | `/books/` | `richard-brokaw-books-elementor.json` |
| About Richard | `/about-richard/` | `richard-brokaw-about-elementor.json` |
| Free Resources | `/free_resources/` | `richard-brokaw-free-resources-elementor.json` |
| Prayer for the Babies (child of Free Resources) | `/free_resources/prayer_for_the_babies/` | `richard-brokaw-prayer-elementor.json` |
| Resource Library (after signup, not in menu) | `/resource-library/` | `richard-brokaw-resource-library-elementor.json` |

Stack: Hello Elementor theme, Elementor (free), MailerLite – Signup forms.

## Still to do
- Sample text for both books (Books page placeholders), exact Amazon link for *My Letter to You*.
- Richard's video for "A Word From Richard" on the homepage.
- MailerLite forms (homepage, Free Resources, prayer page).
- Pages not yet built: *Why the Rapture Tarries* landing page, For Churches & Leaders, Reflections, Contact.
- Open questions: 15 vs. nearly 20 years discipling men; book subtitles (cover vs. shorter versions); "Ecclesia" vs. "Ekklesia"; possible typo in *Our Inheritance from God* (II Timothy 3:15 → 2:15).
