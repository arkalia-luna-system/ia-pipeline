"""
Tests unitaires générés pour pt_br
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import pt_br
except ImportError:
    pytest.skip(f"Module pt_br non importable")


if __name__ == "__main__":
    pytest.main([__file__])
