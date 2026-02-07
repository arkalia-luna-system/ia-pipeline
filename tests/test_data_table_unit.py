"""
Tests unitaires générés pour data_table
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import data_table
except ImportError:
    pytest.skip(f"Module data_table non importable")


if __name__ == "__main__":
    pytest.main([__file__])
