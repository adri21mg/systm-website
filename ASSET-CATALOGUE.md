# Supplied asset catalogue

Reviewed the full initial repository (README, Git state, and every asset), then re-scanned before implementation. No existing website, instructions, dependency manifest, or Steam address was present. The skeleton GIF arrived during inspection and was also reviewed before the design was built. Originals remain untouched.

All still images were visually inspected. GIFs were inspected at beginning, middle, and end; the trailer was inspected through sampled frames across its 49-second duration and stream metadata. SVG logos were rendered for inspection while retaining vector originals.

| Original file under Assets/ | Dimensions / size | Material and decision |
| --- | --- | --- |
| Logos/SYSTM.svg | 4500 × 1050 canvas; 4 KB | White Systm wordmark and two offset squares. Main identity on every page. Tightened canvas in implementation copy only. |
| Logos/TRAPPIST-NEGRO.svg | 1350 × 371; 95 KB | Black game lockup, including supplied STELLACME detail. Kept as SVG and inverted with CSS. Embedded source shadow preserved. |
| Images/Adri.jpg | 400 × 400; 25 KB | Personal portrait. Used on About at a modest size, with a metadata-free WebP copy. |
| Images/HeaderSteamTRAPPIST-1.png | 462 × 174; 132 KB | Low-resolution store capsule with baked-in title. Not selected; too small for the homepage. |
| Images/SkeletonWithAKs.gif | 432 × 446; 4 frames; 136 KB | Absurd dancing skeleton with guns. Used small in the future-project teaser. Pause control and reduced-motion still included. |
| TRAPPIST-1PressStuff/Header.png | 1232 × 706; 1.21 MB | Composed game capsule. Inspected; separate title and gameplay image allow better responsive composition. |
| TRAPPIST-1PressStuff/Logo.png | 1280 × 390; 60 KB | White raster game lockup. Inspected; SVG preferred. |
| TRAPPIST-1PressStuff/Screenshot (1).png | 1920 × 1080; 1.24 MB | Cabin room overlooking the star. Trailer poster. |
| TRAPPIST-1PressStuff/Screenshot (2).png | 1920 × 1080; 1.29 MB | Star close-up. Strong alternative; source retained and web copy available. Homepage uses the more contextual extraction view. |
| TRAPPIST-1PressStuff/Screenshot (3).png | 1920 × 1080; 989 KB | Signal equipment. Alternative still; motion clip communicates the interaction better. |
| TRAPPIST-1PressStuff/Screenshot (4).png | 1920 × 1080; 974 KB | HEX control moves the cabin between nodes; the display on the left shows the cabin’s current energy level. Used in the thumbnail gallery. |
| TRAPPIST-1PressStuff/Screenshot (5).png | 1920 × 1080; 920 KB | Amber corridor. Hallway clip selected for this scene. |
| TRAPPIST-1PressStuff/Screenshot (6).png | 1920 × 1080; 2.15 MB | Station cooling area. The player visits when alarms indicate cooling problems. Used in the maintenance section and thumbnail gallery; opens at full size. |
| TRAPPIST-1PressStuff/Hallway.gif | 1280 × 720; 82 frames; 14.5 MB | Walking along the industrial corridor. Used as an optimized 640 × 360 looping GIF for Something is wrong. 10 fps; original clip duration retained. |
| TRAPPIST-1PressStuff/Signal.gif | 1280 × 720; 230 frames; 6.41 MB | Working signal controls and displays. Used as an optimized 640 × 360 looping GIF for Keep the colonies alive. 10 fps; original clip duration retained. |
| TRAPPIST-1PressStuff/StellarSucker.gif | 1280 × 720; 153 frames; 22.8 MB | Star and extraction machinery. First frame selected for the homepage. A ~4.7 MB web video copy is available for future iteration. |
| Videos/Trailer.mp4 | 1920 × 1080; 60 fps; 49.22 s; 432 MB | Gameplay trailer with AAC audio. Re-encoded to 1280 × 720, 30 fps, H.264/AAC, ~13.3 MB. User-initiated playback only. |

Game artwork and studio branding use supplied assets. No stock or generated imagery. Alternative web copies are game-related assets, not extra page content; they are available for subsequent visual iteration.

## Added during iteration

- `Images/TrappistHeroArt.png`: 1600 × 852, 2.08 MB. Inspected and used as the full-screen game-page artwork, with 800 px and 1600 px WebP copies. Original preserved.
- `TRAPPIST-1PressStuff/VerticalCapsule.png`: 600 × 900, 860 KB. Inspected; composed vertical capsule includes a baked-in title. Preserved as an alternative, not used for the full-screen hero because its logo is authored separately for the requested glitch.
- `Logos/TRAPPIST-1logo.af`: editable source artwork, retained outside the public site. The existing supplied SVG remains the implementation asset.
- All six supplied screenshots now also have 400 × 225 thumbnails for the bottom gallery, linking to their full-size optimized copies.
- `docs/media/steam.webp`: 196 × 60 transparent Steam icon and wordmark, downloaded from the user-requested [Katanaut reference asset](https://www.voidmaw.com/static/media/steam.3becf52f3e92d13ff286.webp). Used locally in both Steam buttons; no external image requests.

Visual direction: a charcoal page, the white Systm mark, quiet typography, very short copy, large gameplay imagery, and a small humorous interruption. Reference sites informed the simplicity and personal scale; their artwork, branding, layout, and copy were not copied.
