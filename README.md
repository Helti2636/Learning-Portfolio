# Learning Portfolio — Robin Held

Four stations, four learning products: a master's thesis on e-learning
(Friedrichshafen), two e-learnings for the City of Graz, a JPO playbook and
digital book shelf (Turin) and self-built online workshop tools (New York).

**Live:** https://helti2636.github.io/Learning-Portfolio/

## How it is built

A single static page, no server and no build tools beyond one small script.

- `index.html` — the page: texts, design and the map (edit here)
- `assets/` — screenshots, videos and the thesis PDF, one folder per station
- `demo/` — a copy of the built [workshop tools demo](https://github.com/Helti2636/workshop-tools-demo), played in the New York section
- `countries-110m.json` — world map data
- `build.py` — writes the publishable site to `docs/`

## Changing something

```
python3 build.py
```

Then commit and push. GitHub Pages publishes `main` → `/docs` within a minute or two.

When the workshop demo changes, rebuild it there and copy its `docs/` folder into `demo/` here.

---

Concept and design: Robin Held · Workshop tool content generalised for demonstration.
