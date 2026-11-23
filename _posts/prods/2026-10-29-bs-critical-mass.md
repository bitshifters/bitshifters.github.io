---
layout: prods_post
category: [posts, prods]
tags: 

title: Critical Mass
img: bs-critical-mass.png
alt: image-alt
authors: By Rich Talbot-Watkins using Claude Code. From Marble Merger by Eli Piilonen (PICO-8).
team: Bitshifters
year: 2026
type: Game
platform: BBC Model B
jsbeebmodel: B-DFS1.2
download: bs-critical-mass.ssd
source: https://github.com/waitingforvsync/criticalmass
pouet:
video:
ai_text: true



---

## **About**

**Critical Mass** is a BBC Micro version of Eli Piilonen's PICO-8 game [Marble Merger](https://www.lexaloffle.com/bbs/?pid=136646), for a stock **BBC Model B**.

Drop balls into the well. Two balls of the same size that touch merge into one of the next size up, and the pile rolls and settles under real physics. There are 12 sizes; you're only ever handed the five smallest, so the big ones have to be built.

The BBC version adds the twist behind its name: merge two of the largest balls and the result reaches **critical mass**. It turns white, the game drops into slow motion, and it bursts into a shower of smaller balls for a big bonus.

## **How to Play**

Move the ball along the top of the well and drop it. **NEXT** shows the ball you'll get after this one. The game is over when the pile reaches the dotted blue line at the top of the well.

### Scoring

* **A merge** scores the size of the ball it makes.
* **Chain reactions** double with every link: a merge set off within a second of the last scores twice its size, the next four times, then eight, and so on.
* **Critical mass** scores a bonus of 1,000, and the pieces it throws out can start chains of their own.

### Game Controls

* `Z` - Left
* `X` - Right
* `SHIFT` - Hold to move slowly
* `RETURN` - Drop the ball / start a new game

## **How it works**

The game runs in MODE 2 at a steady 25 frames a second, on a single screen with no second buffer to draw into. Each ball is a flat, dithered circle, and only the pixels that change between one frame and the next are drawn, so nothing flickers. The whole game, its tables and its screen load as one compressed file.

It's written in 6502 with Baron, Rich's own assembler. The physics was designed first as a Python model in the same integer arithmetic as the 6502, and the tests run the two side by side, frame by frame, to check that every ball and every byte of the screen match.

Needs a **BBC Model B**. No joystick support: keyboard only.
