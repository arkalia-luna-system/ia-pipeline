"""
Tests unitaires générés pour digraphs
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import digraphs
except ImportError:
    pytest.skip(f"Module digraphs non importable")


if __name__ == "__main__":
    pytest.main([__file__])
