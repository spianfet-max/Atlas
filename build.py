"""Build Atlas.

python build.py  ->  index.html     self-contained page for work: the Excel reader (SheetJS 0.18.5) is inlined from vendor/,
                                     so it opens from a local file or GitHub Pages with no internet beyond Keel (optional)
                 ->  artifact.html  the same page for claude.ai, loading SheetJS from cdnjs
"""
import json
from pathlib import Path

root = Path(__file__).parent
src = root / "src"
page = (src / "atlas.src.html").read_text(encoding="utf-8")
page = (page.replace("/*CORE_CSS*/", (src / "core.css").read_text(encoding="utf-8"))
            .replace("/*CORE_JS*/", (src / "core.js").read_text(encoding="utf-8"))
            .replace("/*SAMPLE*/", json.dumps(json.loads((src / "sample.json").read_text(encoding="utf-8")), separators=(",", ":"))))
cdn = '<script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>'
vendor = root / "vendor" / "xlsx.full.min.js"
inline = "<script>" + vendor.read_text(encoding="utf-8") + "</script>" if vendor.exists() else cdn
head = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body>')
(root / "index.html").write_text(head + page.replace("<!--XLSX-->", inline) + "</body></html>", encoding="utf-8")
(root / "artifact.html").write_text(page.replace("<!--XLSX-->", cdn), encoding="utf-8")
print("index.html", (root / "index.html").stat().st_size, "artifact.html", (root / "artifact.html").stat().st_size)
