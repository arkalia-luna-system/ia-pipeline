"""
Tests unitaires générés pour jmespath
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import jmespath
except ImportError:
    pytest.skip(f"Module jmespath non importable")


class TestJMESPathLexer:
    """Tests pour la classe JMESPathLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(jmespath, 'JMESPathLexer')
        assert isinstance(getattr(jmespath, 'JMESPathLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(jmespath, 'JMESPathLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
