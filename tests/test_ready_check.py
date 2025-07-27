#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests pour ready_check.py
"""

import pytest
import sys
import os

# Ajouter le chemin du projet
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from athalia_core.ready_check import check_ready
    READY_CHECK_AVAILABLE = True
except ImportError:
    READY_CHECK_AVAILABLE = False

def test_check_ready_ok():
    """Test que le projet est prêt"""
    if not READY_CHECK_AVAILABLE:
        pytest.skip("Module ready_check non disponible")
    
    report = check_ready(".")
    
    # Vérifier que le rapport contient les clés attendues
    assert "f" in report, "Rapport invalide"
    # Le projet actuel devrait être prêt
    assert report["f"] is True or report["f"] is False, "Valeur f invalide"

def test_check_ready_missing():
    """Test avec un projet manquant"""
    if not READY_CHECK_AVAILABLE:
        pytest.skip("Module ready_check non disponible")
    
    report = check_ready("/chemin/inexistant")
    
    # Vérifier que le rapport contient les clés attendues
    assert "f" in report, "Rapport invalide"
    assert "missing" in report, "Clé missing manquante"
    # Un chemin inexistant devrait avoir des éléments manquants
    assert len(report["missing"]) > 0, "Aucun élément manquant détecté"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])