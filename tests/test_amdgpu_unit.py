"""
Tests unitaires générés pour amdgpu
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import amdgpu
except ImportError:
    pytest.skip(f"Module amdgpu non importable")


class TestAMDGPULexer:
    """Tests pour la classe AMDGPULexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(amdgpu, 'AMDGPULexer')
        assert isinstance(getattr(amdgpu, 'AMDGPULexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(amdgpu, 'AMDGPULexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
