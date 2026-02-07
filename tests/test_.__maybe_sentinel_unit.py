"""
Tests unitaires générés pour .__maybe_sentinel
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import .__maybe_sentinel
except ImportError:
    pytest.skip(f"Module .__maybe_sentinel non importable")


if __name__ == "__main__":
    pytest.main([__file__])
