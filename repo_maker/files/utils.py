from pathlib import Path

DATA_DIR = Path(__file__).parents[1] / "data"
if not DATA_DIR.exists():
    DATA_DIR.mkdir()
    print("Creating data dir.")
