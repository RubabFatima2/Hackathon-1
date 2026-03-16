# Task: T-009

import sys
import io
from pathlib import Path

# Set UTF-8 encoding for Windows console
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Add src directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from todo.storage import Storage
from todo.cli import start_cli


def main():
    """Entry point for the Todo CLI application."""
    storage = Storage()
    start_cli(storage)


if __name__ == "__main__":
    main()
