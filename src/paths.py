from pathlib2 import Path

ROOT_DIR = Path(__file__).parent.parent.absolute()
OUTPUT_FILE = ROOT_DIR / "output" / "output.txt"
OUTPUT_FILE_HTML = ROOT_DIR / "output" / "index.html"
CONFIG_FILE = ROOT_DIR / "config" / "config.json"