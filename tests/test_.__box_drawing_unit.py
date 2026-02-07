"""
Tests unitaires générés pour .__box_drawing
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import .__box_drawing
except ImportError:
    pytest.skip(f"Module .__box_drawing non importable")


if __name__ == "__main__":
    pytest.main([__file__])
