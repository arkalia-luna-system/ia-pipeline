"""
Tests unitaires générés pour v0_5
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import v0_5
except ImportError:
    pytest.skip(f"Module v0_5 non importable")


if __name__ == "__main__":
    pytest.main([__file__])
