# Books Page – Setup

## 1. Create the page and import the template
1. Pages → Add New → **Books**, slug `books`. Publish.
2. Templates → Saved Templates → Import → `richard-brokaw-books-elementor.json`.
3. Edit **Books** with Elementor, insert the template, then set Page Layout = **Elementor Full Width** and Hide Title = on.
4. The covers use the same image files as the homepage (`/wp-content/uploads/site-images/`). If you added the images through the Media Library instead, click each book's HTML widget and change the `data-cover="…"` address to the Media Library URL.

The page-turning reader is built into the page itself (the HTML widget at the top of the hero holds its styles and script). It needs no plugin.

## 2. Replace the sample text (when it's ready)
Each book has an **HTML widget** that holds its sample. Open it and you'll see one block per page:

```html
<section class="rb-page" data-kind="title">…title page…</section>
<section class="rb-page" data-kind=""><h4>Chapter One</h4><h3>Chapter Title</h3><div class="rb-ph">…placeholder…</div></section>
<section class="rb-page" data-kind=""><div class="rb-ph">…placeholder…</div></section>
…
<section class="rb-page" data-kind="end">…"Keep Reading" + Amazon button…</section>
```

- Replace each `<div class="rb-ph">…</div>` with paragraphs, for example `<p>First paragraph…</p><p>Second paragraph…</p>`.
- About **170 words fit on a page**. Text past that gets cut off, so split long passages into more `<section class="rb-page" data-kind="">` blocks.
- You can add or remove pages freely. Keep the title page first and the "end" page last.
- Easiest option: send me the sample text and I'll split it into pages for you.

## 3. Amazon links
- *My Letter to You* currently links to an Amazon **search** for its ISBN (9798765260692). That finds the book, but the exact product link is better. Open the book on Amazon, copy the address up to the `/dp/XXXXXXXXXX` part, and replace the link in two places: the **Buy on Amazon** button, and the button on the sample's last page (inside the HTML widget).
- *Why the Rapture Tarries* shows **Coming Soon to Amazon**. At launch, replace that line with a Button widget (text "Buy on Amazon", link to the product page, "Open in new window" on). Then change "New · Coming Soon" to "Available Now" and swap the last sample page's "Get Notified" link for the Amazon link.

## How the reader behaves
- **Desktop:** hovering lifts the cover slightly. Clicking opens the book into a two-page spread. Readers can click the pages, use Previous/Next, or use the arrow keys. **Close Book** or Esc closes it.
- **Phones:** tapping opens the book one page at a time. Readers can swipe or use the buttons.
- If a visitor's device is set to reduce motion, pages change without the animation.
