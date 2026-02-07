"""
Tests unitaires générés pour ._intelligent_memory
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ._intelligent_memory
except ImportError:
    pytest.skip(f"Module ._intelligent_memory non importable")


if __name__ == "__main__":
    pytest.main([__file__])
