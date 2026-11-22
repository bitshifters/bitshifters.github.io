# Nothing to build: GitHub Pages builds this Jekyll site on push.
# GNU make runs recipes with cmd.exe here (no sh on PATH).
.PHONY: all help

all: help

help:
	@echo Nothing to build here: this is the bitshifters.github.io Jekyll site; GitHub Pages builds it on push.
	@echo To preview locally (needs Ruby + Jekyll, not installed on this machine): jekyll serve --watch
	@echo Ports list for Stardot: py -3 _tools\ports_bbcode.py   See START_HERE.md
