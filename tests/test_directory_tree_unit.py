"""
Tests unitaires générés pour directory_tree
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import directory_tree
except ImportError:
    pytest.skip(f"Module directory_tree non importable")


if __name__ == "__main__":
    pytest.main([__file__])
