# Site Images – Setup

| File | Used on |
|---|---|
| richard-headshot.jpg | Homepage hero, About Richard hero |
| my-letter-to-you-cover.jpg | Homepage "Two Books. One Burden." |
| why-the-rapture-tarries-cover.jpg | Homepage "Two Books" card and the featured New Book section |

The images are already sized for the web (covers 800px wide, headshot cropped to 4:5 portrait at 900px wide).

## Option A: re-import the updated templates (fastest if you haven't edited the pages yet)
1. Copy the three images to the server:
   ```bash
   ssh user@server "sudo mkdir -p /var/www/html/wp-content/uploads/site-images"
   scp *.jpg user@server:/tmp/
   ssh user@server "sudo mv /tmp/richard-headshot.jpg /tmp/*-cover.jpg /var/www/html/wp-content/uploads/site-images/ && \
     sudo chown -R www-data:www-data /var/www/html/wp-content/uploads/site-images"
   ```
2. Import `richard-brokaw-homepage-elementor.json` and `richard-brokaw-about-elementor.json` again (Templates → Saved Templates → Import).
3. On each page, delete the old sections and insert the new template.

## Option B: swap them in Elementor (if you've already made edits on the pages)
1. Media → Add New → upload the three .jpg files.
2. Edit the page with Elementor and click each grey placeholder image. Under **Choose Image**, pick the matching file from the Media Library and click **Update**.
   - Homepage: hero photo, both book cards, and the large featured cover (4 images)
   - About Richard: hero photo (1 image)
3. Add alt text in the Media Library: "Richard Brokaw", "My Letter to You by Richard Brokaw, book cover", "Why the Rapture Tarries by Richard Brokaw, book cover".
