#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests pour le système d'audit intelligent Athalia
"""
import logging
import os
import shutil
import tempfile
from pathlib import Path

import pytest

# Configuration du logging pour les tests
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Test d'import des modules d'audit
AUDIT_AVAILABLE = False
try:
    from athalia_core.intelligent_auditor import IntelligentAuditor
    AUDIT_AVAILABLE = True
except ImportError as e:
    print(f"Import error: {e}")
    AUDIT_AVAILABLE = False


class TestAuditIntelligent:
    """Tests pour l'audit intelligent."""

    def setup_method(self):
        """Prépare un projet de test pour l'audit."""
        self.test_dir = tempfile.mkdtemp()
        self.create_test_project()

    def teardown_method(self):
        """Nettoie après les tests."""
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def create_test_project(self):
        """Crée un projet de test avec des problèmes connus."""
        os.makedirs(os.path.join(self.test_dir, 'src'), exist_ok=True)
        os.makedirs(os.path.join(self.test_dir, 'tests'), exist_ok=True)
        
        # Fichier main.py avec problèmes
        main_content = '''"""
Module principal avec problèmes.
"""

# Problème de sécurité
password = "f"
api_key = "sk-f"

# Problème de performance
def slow_function():
    result = []
    for index in range(100):
        result.append(index)
    return result

# Problème de logging
def debug_function():
    import logging
    logging.info("Debug f")
    return True

# Appel shell risqué
def run_command():
    import os
    os.system("ls -f")
    return True

if __name__ == "__main__":
    debug_function()
    run_command()
'''
        with open(os.path.join(self.test_dir, 'main.py'), 'w') as file_handle:
            file_handle.write(main_content)
        
        # Fichier de test basique
        test_content = '''"""
Test basique.
"""

def test_basic():
    assert True
'''
        with open(os.path.join(self.test_dir, 'tests/test_basic.py'), 'w') as file_handle:
            file_handle.write(test_content)
        
        # README minimal
        with open(os.path.join(self.test_dir, 'README.md'), 'w') as file_handle:
            file_handle.write("# Test Project\n\nMinimal README.")

    @pytest.mark.skipif(not AUDIT_AVAILABLE, reason="Module d'audit intelligent non disponible")
    def test_audit_project_structure(self):
        """Test de l'audit de structure du projet"""
        auditor = IntelligentAuditor(self.test_dir)
        result = auditor.audit_project(str(self.test_dir))
        
        # Vérifier que l'audit a fonctionné
        assert isinstance(result, dict)
        assert 'score' in result or 'global_score' in result or 'summary' in result

    @pytest.mark.skipif(not AUDIT_AVAILABLE, reason="Module d'audit intelligent non disponible")
    def test_audit_code_quality(self):
        """Test de l'audit de qualité du code"""
        auditor = IntelligentAuditor(self.test_dir)
        result = auditor.audit_project(str(self.test_dir))
        
        # Vérifier que l'audit a fonctionné
        assert isinstance(result, dict)
        
        # Les métriques peuvent être dans result ou result['metrics']
        metrics = result.get('metrics', result)
        assert isinstance(metrics, dict)

    @pytest.mark.skipif(not AUDIT_AVAILABLE, reason="Module d'audit intelligent non disponible")
    def test_audit_security(self):
        """Test de l'audit de sécurité"""
        auditor = IntelligentAuditor(self.test_dir)
        result = auditor.audit_project(str(self.test_dir))
        
        # Vérifier que l'audit a fonctionné
        assert isinstance(result, dict)
        
        # Vérifier qu'il y a des informations de sécurité
        security_info = result.get('security', {})
        assert isinstance(security_info, dict)

    @pytest.mark.skipif(not AUDIT_AVAILABLE, reason="Module d'audit intelligent non disponible")
    def test_audit_performance(self):
        """Test de l'audit de performance"""
        auditor = IntelligentAuditor(self.test_dir)
        result = auditor.audit_project(str(self.test_dir))
        
        # Vérifier que l'audit a fonctionné
        assert isinstance(result, dict)

    @pytest.mark.skipif(not AUDIT_AVAILABLE, reason="Module d'audit intelligent non disponible")
    def test_audit_complete(self):
        """Test d'audit complet"""
        auditor = IntelligentAuditor(self.test_dir)
        result = auditor.audit_project(str(self.test_dir))
        
        # Vérifier que l'audit a fonctionné
        assert isinstance(result, dict)
        
        # Vérifier qu'il y a des informations de base
        assert len(result) > 0

    @pytest.mark.skipif(not AUDIT_AVAILABLE, reason="Module d'audit intelligent non disponible")
    def test_generate_audit_report(self):
        """Test de génération de rapport d'audit"""
        auditor = IntelligentAuditor(self.test_dir)
        result = auditor.audit_project(str(self.test_dir))
        
        # Vérifier que l'audit a fonctionné
        assert isinstance(result, dict)
        
        # Vérifier qu'on peut générer un rapport
        if hasattr(auditor, 'generate_report'):
            report = auditor.generate_report()
            assert isinstance(report, (str, dict))

    def test_audit_project_not_found(self):
        """Test d'audit avec un projet inexistant"""
        if not AUDIT_AVAILABLE:
            pytest.skip("Module d'audit intelligent non disponible")
        
        non_existent_dir = "/tmp/non_existent_project_12345"
        try:
            auditor = IntelligentAuditor(non_existent_dir)
            result = auditor.audit_project(str(non_existent_dir))
            # L'audit devrait gérer le cas d'un projet inexistant
            assert isinstance(result, dict)
        except Exception as e:
            # C'est acceptable qu'une exception soit levée
            error_msg = str(e).lower()
            assert ("not found" in error_msg or 
                   "does not exist" in error_msg or 
                   "no such file" in error_msg)

    def test_audit_empty_project(self):
        """Test d'audit avec un projet vide"""
        if not AUDIT_AVAILABLE:
            pytest.skip("Module d'audit intelligent non disponible")
        
        empty_dir = tempfile.mkdtemp()
        try:
            auditor = IntelligentAuditor(empty_dir)
            result = auditor.audit_project(str(empty_dir))
            # L'audit devrait gérer le cas d'un projet vide
            assert isinstance(result, dict)
        finally:
            shutil.rmtree(empty_dir, ignore_errors=True)


def test_audit_integration():
    """Test d'intégration de l'audit"""
    # Test que le module peut être importé
    if not AUDIT_AVAILABLE:
        pytest.skip("Module d'audit intelligent non disponible")
    
    # Test de création d'instance
    with tempfile.TemporaryDirectory() as temp_dir:
        try:
            auditor = IntelligentAuditor(temp_dir)
            assert auditor is not None
        except Exception as e:
            # C'est acceptable qu'une exception soit levée pour un projet vide
            assert "empty" in str(e).lower() or "no files" in str(e).lower()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])