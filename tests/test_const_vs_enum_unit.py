"""
Tests unitaires générés pour const_vs_enum
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import const_vs_enum
except ImportError:
    pytest.skip(f"Module const_vs_enum non importable")


if __name__ == "__main__":
    pytest.main([__file__])
