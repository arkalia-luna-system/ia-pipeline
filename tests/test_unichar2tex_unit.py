"""
Tests unitaires générés pour unichar2tex
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import unichar2tex
except ImportError:
    pytest.skip(f"Module unichar2tex non importable")


if __name__ == "__main__":
    pytest.main([__file__])
