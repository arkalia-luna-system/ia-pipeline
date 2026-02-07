"""
Tests unitaires générés pour .__project_data
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import .__project_data
except ImportError:
    pytest.skip(f"Module .__project_data non importable")


if __name__ == "__main__":
    pytest.main([__file__])
