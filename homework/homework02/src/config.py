# TODO: implement minimal helpers here or in src/config.py. In both for this submission.
import os
from pathlib import Path

def get_key(name: str, default=None):
    return os.getenv(name, default)

PROJECT_ROOT = Path.cwd()
DATA_DIR = PROJECT_ROOT / "data"
print(PROJECT_ROOT, DATA_DIR)