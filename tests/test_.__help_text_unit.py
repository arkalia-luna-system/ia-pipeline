"""
Tests unitaires générés pour .__help_text
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import .__help_text
except ImportError:
    pytest.skip(f"Module .__help_text non importable")


if __name__ == "__main__":
    pytest.main([__file__])
