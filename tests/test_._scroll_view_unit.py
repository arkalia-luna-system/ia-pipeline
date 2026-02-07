"""
Tests unitaires générés pour ._scroll_view
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ._scroll_view
except ImportError:
    pytest.skip(f"Module ._scroll_view non importable")


if __name__ == "__main__":
    pytest.main([__file__])
