"""
Tests unitaires générés pour ._device_code
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ._device_code
except ImportError:
    pytest.skip(f"Module ._device_code non importable")


if __name__ == "__main__":
    pytest.main([__file__])
