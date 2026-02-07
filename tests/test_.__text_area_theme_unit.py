"""
Tests unitaires générés pour .__text_area_theme
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import .__text_area_theme
except ImportError:
    pytest.skip(f"Module .__text_area_theme non importable")


if __name__ == "__main__":
    pytest.main([__file__])
