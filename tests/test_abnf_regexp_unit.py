"""
Tests unitaires générés pour abnf_regexp
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import abnf_regexp
except ImportError:
    pytest.skip(f"Module abnf_regexp non importable")


if __name__ == "__main__":
    pytest.main([__file__])
