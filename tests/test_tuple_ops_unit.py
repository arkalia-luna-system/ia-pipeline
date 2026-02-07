"""
Tests unitaires générés pour tuple_ops
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import tuple_ops
except ImportError:
    pytest.skip(f"Module tuple_ops non importable")


if __name__ == "__main__":
    pytest.main([__file__])
