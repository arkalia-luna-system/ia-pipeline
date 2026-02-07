"""
Tests unitaires générés pour wrappers_pb2
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import wrappers_pb2
except ImportError:
    pytest.skip(f"Module wrappers_pb2 non importable")


if __name__ == "__main__":
    pytest.main([__file__])
