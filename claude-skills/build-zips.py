"""Build claude.ai upload zips for each skill.

Run from anywhere:  python claude-skills/build-zips.py
Writes downloads/<skill>.zip, each containing <skill>/SKILL.md.
Rerun this after editing a skill so the downloads stay in sync.
"""
import pathlib
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent
SKILLS = ROOT / "skills"
OUT = ROOT / "downloads"
OUT.mkdir(exist_ok=True)

for skill in sorted(p for p in SKILLS.iterdir() if (p / "SKILL.md").is_file()):
    target = OUT / f"{skill.name}.zip"
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(skill.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(SKILLS).as_posix())
    print(f"built {target.relative_to(ROOT.parent)}")
