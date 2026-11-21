"""Print the ports page (_data/ports.yml) as a short phpBB/BBCode list for Stardot.

Run from the repository root:  python _tools/ports_bbcode.py
Newest first, matching https://bitshifters.github.io/ports.html.
Each name links to its Stardot thread, else its page, else its source.
"""
import sys
import yaml

sys.stdout.reconfigure(encoding="utf-8")

with open("_data/ports.yml", encoding="utf-8") as f:
    ports = yaml.safe_load(f)

ports.sort(key=lambda p: str(p.get("added", "")), reverse=True)

out = [
    "[b][size=150]Ports and more...[/size][/b]",
    "AI-assisted ports, remasters and new games for the BBC Micro. "
    "Full list with screenshots, downloads and Play links: "
    "[url=https://bitshifters.github.io/ports.html]bitshifters.github.io/ports.html[/url]",
    "",
    "[list]",
]
for p in ports:
    link = p.get("thread") or p.get("page") or p.get("source")
    if link and link.startswith("/"):
        link = "https://bitshifters.github.io" + link
    name = f"[url={link}]{p['name']}[/url]" if link else p["name"]
    kind = p.get("kind", "port")
    tags = [] if kind == "port" else [kind]
    if p.get("status"):
        tags.append(str(p["status"]))
    tag = f" [i]({', '.join(tags)})[/i]" if tags else ""
    origin = "" if kind == "original" or not p.get("from") else f", from {p['from']}"
    out.append(f"[*][b]{name}[/b]{tag} - {p['author']}{origin}")
out.append("[/list]")
out.append(f"[size=85]{len(ports)} entries.[/size]")

print("\n".join(out))
