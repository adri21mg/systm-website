# Systm

A complete, build-free static studio website. Four pages, plain HTML/CSS/JavaScript, no runtime dependencies, external fonts, or analytics. Ko-fi uses one direct footer link per page, with a locally hosted GIF.

## View locally

From PowerShell:

```powershell
cd W:\Systm-Website
node tools/serve.mjs
```

Open **http://127.0.0.1:4173/**. The preview server binds only to your computer and serves only `docs/`. Stop it with Ctrl+C. `npm start` is equivalent; no `npm install` is needed. If the port is already in use, use the existing preview or set `$env:PORT = '4174'` before starting.

You can also open `docs/index.html` directly in a browser. The HTTP preview is preferable for video seeking and browser testing.

## Edit

- `docs/index.html`: homepage and future-project teaser.
- `docs/trappist-1.html`: full-screen illustrated cover, game description, trailer, three gameplay sections, Steam buttons, and six-image thumbnail gallery.
- `docs/about.html`: personal introduction and contact.
- `docs/styles.css`: shared design and responsive layouts.
- `docs/content.js`: official Steam URL for TRAPPIST-1 (app 4987640). Both Wishlist on Steam and On Steam link to the coming-soon store page. Update the purchase wording when the game actually launches.
- `docs/site.js`: Subtle cursor-follow movement, occasional horizontal logo glitch, screenshot viewer, trailer behavior, and current year.
- `docs/transitions.js`: short pixel-block transitions between pages. A temporary sessionStorage entry carries the transition across navigation; no cookies or tracking. Modified clicks, external links, same-page anchors, and reduced-motion settings keep normal navigation.
- `docs/media/`: optimized public copies of supplied assets.
- `Assets/`: untouched original source assets. These are not served by the preview.
- `ASSET-CATALOGUE.md`: all supplied material and first-pass selection decisions.

All links are relative, so the site can later run under a GitHub Pages repository subpath. Only `docs/` is the public website. A future Pages setup should publish that directory alone, not the whole repository. There is no deployment workflow, hosting configuration, or automatic publishing. Nothing has been pushed or deployed.

## Media

Responsive WebP copies retain image proportions. The homepage uses an intentional cover crop; all game media retains its full 16:9 frame. Both logos remain SVG; Systm's implementation copy has a tighter canvas, and the game logo is inverted with CSS. The small favicon reuses the two-square Systm mark.

The game cover uses optimized copies of `TrappistHeroArt.png` edge-to-edge, with a deliberate responsive cover crop. The logo stays still between 240 ms horizontal-cut glitches, spaced randomly 6.5–12.5 seconds apart; no glitch when reduced motion is requested or the tab is hidden. The six small gallery thumbnails open full-size WebP screenshots in a native dialog; use Previous/Next, arrow keys, Close, or Escape. Without JavaScript, thumbnails remain direct image links.

The 432 MB source trailer has a ~13.3 MB H.264/AAC, 720p, 30 fps web copy with fast-start metadata and native controls (`preload="none"`). Signal and corridor gameplay use actual 640 × 360 GIFs at 10 fps with continuous looping, the original clip duration, and lazy loading. They animate as soon as loaded, without pressing play. GIFs loop continuously without pause controls or still-image substitutions. Reduced-motion settings still disable the navigation wipe, logo glitch, and cursor motion. Images are stripped of original metadata when re-encoded.

For asset regeneration only, install Pillow and provide an FFmpeg executable:

```powershell
python tools/prepare_assets.py --ffmpeg C:\path\to\ffmpeg.exe
```

Omit `--ffmpeg` to regenerate stills and logo copies, retaining optimized GIFs (or copying source GIFs if none exist). This tooling is optional; all ready-to-use media is already in `docs/media/`.

## Copy decisions

The About page credits **Blades of Fire** and **Metroid Ravenous**, as specified by the owner. No release date, store availability, price, or additional gameplay mechanics have been invented.

## Local LMMS-Collab proposal (not published)

`docs/lmms-collab.html` is a local presentation prototype. The demo area is explicitly a placeholder; replace it with real Song Editor footage. Additional short demonstrations can go between the main demo and GitHub section once supplied. The GitHub button links to https://github.com/adri21mg/lmms-collab, with an inline GitHub mark and the site’s accent color on hover or keyboard focus.

Studio navigation uses restrained rectangular hover targets. The TRAPPIST-1 cover navigation and existing media are unchanged. All footers use one branded link to https://ko-fi.com/systmstudio, with the supplied `Assets/ko-fi/Sparkle mug.gif` copied unchanged to `docs/media/kofi-sparkle.gif`. The image loads lazily and loops as provided. The original stays intact. There is no floating widget, embedded payment panel, separate support section, or external Ko-fi script. Payment takes place on Ko-fi after following the footer link.

## YouTube trailer

TRAPPIST-1 now embeds the supplied YouTube video `rQwITmcYSuk` using youtube-nocookie.com, lazy loading, a responsive 16:9 frame, fullscreen support, and a direct YouTube fallback link. Playback requires access to YouTube. The original local MP4 remains preserved but is no longer loaded by the page. Changes are local only.

## LMMS-Collab identity and support

The supplied `Assets/Logos/LMMS-Collab.svg` is copied unchanged into `docs/media/lmms-collab.svg` and used on Home and the tool page. LMMS-Collab has a centered closing support section, with `Support me 3.gif` as the clickable Ko-fi invitation. This replaces the short message above the footer button. The shared footer button remains on every page; no floating widget is loaded.
