from pathlib import Path
import os


ROOT_DIR = Path(os.path.dirname(os.path.realpath(__file__)))
DATA_DIR = Path.resolve(ROOT_DIR / "data")
