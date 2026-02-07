"""
Tests unitaires générés pour ._convert_percent_format_to_fstring
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ._convert_percent_format_to_fstring
except ImportError:
    pytest.skip(f"Module ._convert_percent_format_to_fstring non importable")


if __name__ == "__main__":
    pytest.main([__file__])
