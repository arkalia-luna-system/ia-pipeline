"""
Tests unitaires générés pour .__widget_navigation
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import .__widget_navigation
except ImportError:
    pytest.skip(f"Module .__widget_navigation non importable")


if __name__ == "__main__":
    pytest.main([__file__])
