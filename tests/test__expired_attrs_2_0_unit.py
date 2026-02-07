"""
Tests unitaires générés pour _expired_attrs_2_0
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _expired_attrs_2_0
except ImportError:
    pytest.skip(f"Module _expired_attrs_2_0 non importable")


if __name__ == "__main__":
    pytest.main([__file__])
