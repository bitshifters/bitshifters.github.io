# bitshifters.github.io: start here

The Bitshifters demo group's website: a Jekyll site served by GitHub Pages at https://bitshifters.github.io. It also hosts downloadable disc images and WIP builds that the site and emulator links point at.

| | |
|---|---|
| GitHub | https://github.com/bitshifters/bitshifters.github.io (public) |
| Local path | D:\beeb\mine\bitshifters.github.io (moved from OneDrive\BEEB\Repos\bitshifters.github.io on 2026-11-22) |
| Branch | master (only branch) |
| Last commit | 2026-11-21: Create p15k4v_cream_v6.ssd |

## What's in here
- `_posts/` - one post per entry: `prods/`, `compos/`, `archives/`, `support/` (see README.md "Site structure").
- `_data/` - YAML lists: `ports.yml` (the Ports page), `ports_sources.yml`, `greets.yml`, `links.yml`, `team.yml`.
- `_layouts/`, `_includes/`, `css/`, `js/`, `img/` - templates and assets; top-level `*.html` / `ports.md` are the pages.
- `content/` - downloads: disc images, screenshots, zips; `content/wip/` holds shared WIP builds (the `publish-wip` skill writes here).
- `arclive/` - Archimedes emulator files (arculator.data, nspark) used for in-browser Archimedes links.
- `_tools/ports_bbcode.py` - prints the ports list as BBCode for Stardot (`py -3 _tools\ports_bbcode.py`, needs PyYAML).
- `notes.md` - 2021 site revamp ideas.

## Build and run
- `make`: prints that there is nothing to build (GitHub Pages builds the site on push) and how to preview locally.
- Local preview needs Ruby + Jekyll (`jekyll serve --watch`); neither is installed on this machine.
- To publish: commit and push to master; the live site updates in a minute or two.

## Local changes
- None: working tree clean at the 2026-11 tidy, no stashes, no snapshot branches.

## Status and next steps
- Live and actively updated (1,100+ commits since 2016; several WIP and Ports updates on 2026-11-21).
- jsbeeb links now point at bbc.xania.org; NuLA gallery links use the `jsbeebflags` front matter.
- `notes.md` has an old (2021) revamp wishlist; no other TODO found.

## See also
- README.md (Jekyll structure and how to add posts).
- D:\beeb\mine\jsbeeb-kieranhj (the emulator the site's "Emulate" links used to target).
