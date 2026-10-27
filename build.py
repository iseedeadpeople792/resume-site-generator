"""Генератор одностраничного резюме-сайта из data.json.
Запуск: python build.py data.json index.html
"""
import html
import json
import sys

PAGE = """<!doctype html>
<html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{name} — резюме</title>
<style>body{{font:16px/1.6 system-ui,sans-serif;max-width:720px;margin:0 auto;padding:32px 16px;color:#1a1d21}}
h1{{margin:0}}h2{{margin-top:32px;border-bottom:2px solid #e3e6ea;padding-bottom:4px}}.role{{color:#5b6570}}
.tag{{display:inline-block;background:#eef2ff;border-radius:8px;padding:2px 10px;margin:2px}}a{{color:#2f5bea}}
@media(prefers-color-scheme:dark){{body{{background:#14171a;color:#e8eaed}}h2{{border-color:#2c3238}}.tag{{background:#232a45}}a{{color:#8fa8ff}}}}</style>
</head><body>
<h1>{name}</h1><div class="role">{role}</div><p>{about}</p>
<h2>Навыки</h2><p>{skills}</p>
<h2>Опыт</h2>{jobs}
<h2>Контакты</h2><p>{contacts}</p>
</body></html>
"""


def esc(s):
    return html.escape(str(s))


def render(d):
    skills = "".join(f'<span class="tag">{esc(s)}</span>' for s in d.get("skills", []))
    jobs = "".join(
        f'<p><b>{esc(j["title"])}</b>, {esc(j["company"])} <span class="role">({esc(j["years"])})</span><br>{esc(j.get("text", ""))}</p>'
        for j in d.get("jobs", [])
    )
    contacts = " · ".join(f'<a href="{esc(url)}">{esc(label)}</a>' for label, url in d.get("contacts", {}).items())
    return PAGE.format(name=esc(d["name"]), role=esc(d.get("role", "")), about=esc(d.get("about", "")),
                       skills=skills, jobs=jobs, contacts=contacts)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    with open(sys.argv[1], encoding="utf-8") as f:
        page = render(json.load(f))
    with open(sys.argv[2], "w", encoding="utf-8") as f:
        f.write(page)
    print("Готово:", sys.argv[2])
