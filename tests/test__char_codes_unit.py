"""
Tests unitaires générés pour _char_codes
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _char_codes
except ImportError:
    pytest.skip(f"Module _char_codes non importable")


if __name__ == "__main__":
    pytest.main([__file__])
