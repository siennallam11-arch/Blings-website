# Build tools

The site's HTML pages are generated. Edit these, not the `.html` files directly.

- `build.py` holds the content and layout for every page (nav, footer, Experience, Hobbies & Extracurriculars, Projects).
- `home.part` holds the home page body.
- `assets/style.css` holds all styling.

Rebuild the pages from the repo root:

    python3 tools/build.py . tools/home.part

Optional: make a single-file preview (all pages, images and the resume inlined), used for the claude.ai preview link:

    python3 tools/preview_bundle.py . /path/to/william-chang-site.html

Then run `git add -A`, commit, and push.
