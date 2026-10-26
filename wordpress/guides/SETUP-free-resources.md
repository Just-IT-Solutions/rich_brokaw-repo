# Free Resources – Setup Guide

How it works: a visitor fills in the MailerLite form on **/free_resources/**. MailerLite adds them to the list and sends them to **/resource-library/**, where all six PDFs can be downloaded. A welcome email sends the same link so they can come back later.

## 0. Set the page address to /free_resources/
WordPress creates the address from the title, so "Free Resources" becomes `free-resources` with a hyphen. To change it:
1. Pages → edit **Free Resources** (in the WordPress editor, not Elementor).
2. In the right sidebar, open **Page** → **URL** (older versions call it **Permalink**), and set the slug to `free_resources`.
3. Click **Update**, then open `https://YOURDOMAIN/free_resources/` to confirm it loads.
4. If you created the page earlier with the hyphen, also update the nav menu: Appearance → Menus. Edit the **Free Resources** button (Custom Link) and set its URL to `/free_resources/`. Menu items linked to the page itself update on their own.

The page title stays *Free Resources*. Only the address changes.

## 1. Put the PDFs and thumbnails on the server
The templates expect the files at `/wp-content/uploads/resources/`. From the folder that holds `pdfs/` and `thumbs/`:

```bash
# adjust user@server and the WordPress path to match your install
ssh user@server "sudo mkdir -p /var/www/html/wp-content/uploads/resources"
scp pdfs/*.pdf thumbs/*.png user@server:/tmp/
ssh user@server "sudo mv /tmp/*.pdf /tmp/*.png /var/www/html/wp-content/uploads/resources/ && \
  sudo chown -R www-data:www-data /var/www/html/wp-content/uploads/resources"
```

Check it worked by opening `https://YOURDOMAIN/wp-content/uploads/resources/becoming-a-man.pdf` in a browser.

| File | Resource |
|---|---|
| jesus-christ-our-foundation.pdf / .png | Jesus Christ, Our Foundation |
| the-imperative-of-knowing-god.pdf / .png | The Imperative of Knowing God |
| stages-of-maturity-in-christ.pdf / .png | Stages of Maturity in Christ |
| the-parable-of-the-sower.pdf / .png | The Parable of the Sower |
| our-inheritance-from-god.pdf / .png | Our Inheritance from God |
| becoming-a-man.pdf / .png | Becoming a Man |

## 2. Create the Resource Library page
Pages → Add New → title **Resource Library**, slug `resource-library`. Publish it, but **don't add it to the menu**.
If you use Yoast or Rank Math, set this page to *noindex* so it doesn't show up in Google.
Note: the page is hidden, not locked. Anyone who has the link can open it, which is normal for free resources.

## 3. Import the two templates
Templates → Saved Templates → Import Templates, then upload both:
- `richard-brokaw-free-resources-elementor.json` → insert into the **Free Resources** page
- `richard-brokaw-resource-library-elementor.json` → insert into the **Resource Library** page

On each page, open Page Settings: Page Layout = **Elementor Full Width**, Hide Title = on.

## 4. MailerLite
1. **Subscribers → Groups** → create group **Resource Library**.
2. **Forms → Embedded forms** → create **Resource Library**, add First name + Email, put it in the group above, and set the button text to *Send Me the Resources*.
3. In the form's **Success page** settings, choose **Redirect to URL** → `https://YOURDOMAIN/resource-library/`.
4. On the Free Resources page in Elementor, find the dashed "MailerLite form goes here" box (HTML widget, *Send Me the Resources* section). Paste the form's embed code into it, or delete it and add a **Shortcode** widget with the MailerLite plugin shortcode.
5. **Automations** → new automation, trigger *When subscriber joins group → Resource Library*, step: send the email below.

**Suggested welcome email**

> **Subject:** Your free resources are ready
>
> Hi {$name},
>
> Thank you for joining. Your six free studies are waiting for you here:
>
> **[Open the Resource Library →]** (link to https://YOURDOMAIN/resource-library/)
>
> If you're not sure where to start, begin with *Jesus Christ, Our Foundation*. It's a one-page declaration meant to be read each morning when you wake.
>
> I'll write occasionally with Bible teaching, new resources, and news about *Why the Rapture Tarries*.
>
> Listening to Jesus. Living faithfully. Waiting for His return.
>
> Richard Brokaw

If the homepage mailing-list form uses a different MailerLite form, that's fine. Both groups go to the same subscriber list.

## 5. Adding a new resource later
1. Upload the PDF to `/wp-content/uploads/resources/`. For a thumbnail, export page 1 as a PNG about 600px wide.
2. In Elementor, duplicate an existing card on **both** pages. Change the image, title, tag line and description. On the Resource Library card, also change the PDF link.
3. When the Seven Letters Study or Waiting for Christ is ready, move it out of "More Resources Coming."

## 6. Recommended Sites (links to other sites)
The bottom of the Free Resources page has a **Recommended Sites** section with cards for Capital Church and Students for Life of America. Each card's **Visit Site** button opens the other site in a new tab.

To add another site: in Elementor, right-click one of the cards → **Duplicate**. Then change the label (e.g. *Church*), the name, the web address shown under the name, the description, and the button link. Keep "Open in new window" ticked on the button. If you end up with an odd number of cards, the last one centers on its own row.
