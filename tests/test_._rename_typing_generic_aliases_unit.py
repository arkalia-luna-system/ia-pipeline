"""
Tests unitaires générés pour ._rename_typing_generic_aliases
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ._rename_typing_generic_aliases
except ImportError:
    pytest.skip(f"Module ._rename_typing_generic_aliases non importable")


if __name__ == "__main__":
    pytest.main([__file__])
