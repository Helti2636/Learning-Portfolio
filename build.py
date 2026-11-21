"""Builds the public website into /docs (served by GitHub Pages from main -> /docs).

index.html is the editable source. It has no <html>/<head> wrapper of its own
(the Claude preview adds one), so this script adds a proper document head and
copies the map data, the assets and the embedded workshop demo next to it.

Run:  python3 build.py
"""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "docs"

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<meta name="description" content="Learning portfolio of Robin Held: workshop tools, a JPO playbook, e-learnings and a master's thesis on e-learning.">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ccircle cx='50' cy='50' r='34' fill='%23c19a4f'/%3E%3C/svg%3E">
<style>html,body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
"""


def main() -> None:
    src = (ROOT / "index.html").read_text(encoding="utf-8")
    src = src.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "")
    marker = "</style>"
    cut = src.index(marker) + len(marker)
    page = HEAD + src[:cut] + "\n</head>\n<body>\n" + src[cut:].lstrip() + "\n</body>\n</html>\n"

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    (OUT / "index.html").write_text(page, encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    shutil.copy(ROOT / "countries-110m.json", OUT)
    shutil.copytree(ROOT / "assets", OUT / "assets")
    shutil.copytree(ROOT / "demo", OUT / "demo")
    print("Built", OUT)


if __name__ == "__main__":
    main()
