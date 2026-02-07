"""
Tests unitaires générés pour ._convert_union_to_or
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ._convert_union_to_or
except ImportError:
    pytest.skip(f"Module ._convert_union_to_or non importable")


if __name__ == "__main__":
    pytest.main([__file__])
