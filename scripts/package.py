"""Build the two upload packages from one canonical skill."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

root = Path(__file__).resolve().parents[1]
output = root / "dist"
output.mkdir(exist_ok=True)
skill = root / "skills/carrychapter/SKILL.md"

with ZipFile(output / "carrychapter-claude.zip", "w", ZIP_DEFLATED) as archive:
    archive.write(skill, "carrychapter/SKILL.md")

with ZipFile(output / "carrychapter-openai.zip", "w", ZIP_DEFLATED) as archive:
    archive.write(root / "plugin.json", "plugin.json")
    archive.write(skill, "skills/carrychapter/SKILL.md")

print(*(path.name for path in sorted(output.glob("*.zip"))), sep="\n")
