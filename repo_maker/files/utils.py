from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
if not DATA_DIR.exists():
    DATA_DIR.mkdir()
    print("Creating data dir.")
