from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
TEMPLATES_DIRS = BASE_DIR / 'templates'

print(BASE_DIR)
print(TEMPLATES_DIRS)
