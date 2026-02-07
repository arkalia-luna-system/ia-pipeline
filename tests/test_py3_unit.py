"""
Tests unitaires générés pour py3
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import py3
except ImportError:
    pytest.skip(f"Module py3 non importable")


if __name__ == "__main__":
    pytest.main([__file__])
