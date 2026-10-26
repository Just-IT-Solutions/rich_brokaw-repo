# Prayer for the Babies – Setup

Address: **/free_resources/prayer_for_the_babies/**. This is a child page of Free Resources.

## 1. Upload the PDF and thumbnail
Put both files from `files/` in the same folder as the other resources:
```bash
scp files/prayer-for-the-babies-in-nys.* user@server:/tmp/
ssh user@server "sudo mv /tmp/prayer-for-the-babies-in-nys.* /var/www/html/wp-content/uploads/resources/ && \
  sudo chown www-data:www-data /var/www/html/wp-content/uploads/resources/prayer-for-the-babies-in-nys.*"
```

## 2. Create the page as a child of Free Resources
1. Pages → Add New → title **Prayer for the Babies in New York State**.
2. In the right sidebar:
   - **Page → Parent** (older versions: **Page Attributes → Parent**) → choose **Free Resources**.
   - **Page → URL** → set the slug to `prayer_for_the_babies`. Type it by hand; WordPress would otherwise use hyphens.
3. Publish. The address should read `/free_resources/prayer_for_the_babies/`.
4. Edit with Elementor → insert `richard-brokaw-prayer-elementor.json` (import it under Templates → Saved Templates first). Page Settings: **Elementor Full Width**, Hide Title on.

## 3. Add it to the menu under Free Resources
Appearance → Menus → tick **Prayer for the Babies in New York State** under Pages → **Add to Menu**. Then drag it just below **Free Resources** and slightly to the right, so it sits indented as a sub-item. Change its **Navigation Label** to *Prayer for the Babies* and **Save Menu**.
The Hello theme shows sub-items as a dropdown on desktop and indented in the phone menu.

If you'd like visitors to be able to click through to the main Free Resources page from the dropdown, also add a Custom Link `/free_resources/` labeled *All Free Resources* as the first sub-item. (Clicking "Free Resources" itself still works too.)

## 4. Feature it on the Free Resources page
The updated `richard-brokaw-free-resources-elementor.json` has a **Featured · A Prayer** banner above the library that links to the new page. Either re-insert that template, or copy the banner section into your existing page (Elementor: right-click the section → Copy, then paste on the other page).

## 5. MailerLite (optional)
The "Stand With Us in Prayer" box takes a MailerLite form. Use a group such as **Prayer for NYS** so you can send prayer updates to just those people. Unlike the study library, the prayer and PDF are open to everyone; no signup is needed to read or print it.
