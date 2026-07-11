from pathlib import Path
import sys


PACKAGE_PARENT = Path(__file__).resolve().parents[3]

if str(PACKAGE_PARENT) not in sys.path:
    sys.path.insert(0, str(PACKAGE_PARENT))
