"""
Tests unitaires générés pour ._security_validator
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ._security_validator
except ImportError:
    pytest.skip(f"Module ._security_validator non importable")


if __name__ == "__main__":
    pytest.main([__file__])
