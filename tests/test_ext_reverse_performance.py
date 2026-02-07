"""
Tests de performance générés automatiquement pour ext_reverse
"""

import pytest
import time
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ext_reverse
except ImportError:
    pytest.skip(f"Module ext_reverse non importable")

    def test_ext_reverse_performance():
        """Test de performance pour ext_reverse"""
        start_time = time.time()

        # TODO: Implémenter les tests de performance spécifiques
        # Par exemple, tester le temps d'exécution des fonctions

        end_time = time.time()
        execution_time = end_time - start_time

        # Vérifier que l'exécution est rapide (moins de 1 seconde)
        assert execution_time < 1.0, f"Exécution trop lente: {execution_time:.3f}s"

if __name__ == "__main__":
    pytest.main([__file__])
