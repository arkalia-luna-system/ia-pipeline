"""
Tests unitaires générés pour column_config
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import column_config
except ImportError:
    pytest.skip(f"Module column_config non importable")


if __name__ == "__main__":
    pytest.main([__file__])
