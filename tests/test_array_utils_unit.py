"""
Tests unitaires générés pour array_utils
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import array_utils
except ImportError:
    pytest.skip(f"Module array_utils non importable")


if __name__ == "__main__":
    pytest.main([__file__])
