---
layout: prods_post
category: [posts, prods]
tags: nova
rank: 
title: ArchieKlang Announcetro
img: bs-archieklang.png
alt: image-alt
authors: Kieran^Bitshifters, Virgill^Alcatraz, Rhino^Torment
team: Bitshifters & Alcatraz & Torment
year: 2024
type: Intro
platform: Acorn Archimedes
emuboot: autoboot=desktop%20hostfs::hostfs.$.!AKlang&soundfilter=2&preset=a3010
download: bs-archieklang,ddc
source: https://github.com/bitshifters/aklang
pouet: 
video: 

---

**ArchieKlang Announcetro**

A cheeky 28kb intro for the Acorn Archimedes released at NOVA 2024 in the Oldschool Demo Compo. This is the first production on the Archimedes to use Virgill's AmigaKlang soft synth - it generates 280+kb of sample data from just a few kb of code!

You can [download the AmigaKlangGUI](https://www.pouet.net/prod.php?which=85351) and [see the other demos using it](https://www.pouet.net/lists.php?which=186) on Pouet. Find the Archimedes [source code on GitHub](https://github.com/kieranhj/archieklang).

The released intro is designed for ARM250+ machines but this time we remembered to make an [ARM2 version](../../content/bs-aklang-arm2,ddc). The demo should work on 2Mb machines, if you get a 'No writeable memory at this address' error, you might need to reboot, sorry!

Run on real Archimedes hardware with RISC OS 3.1, or if running under emulation, use [Arculator v2.1+](http://b-em.bbcmicro.com/arculator/). For best emulated experience, emulate an A3010 and select sound output filter -> more reduced.

For best audio quality on real Archimedes hardware we recommend removing the hardware low-pass filter by following the instructions on this [thread](https://stardot.org.uk/forums/viewtopic.php?f=16&t=13630).

Powered by [TinyQTM](http://www.pi-star.co.uk/qtm/) MOD player. Special thanks Blueberry^Loonies for Shrinkler.
