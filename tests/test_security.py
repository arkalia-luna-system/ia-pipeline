#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests pour le module security.
Tests de base pour l'audit de sécurité des projets.
"""

import pytest


# Import conditionnel du module security
try:
    from athalia_core.security import security_audit_project

    SECURITY_AVAILABLE = True
except ImportError:
    SECURITY_AVAILABLE = False


@pytest.mark.skipif(not SECURITY_AVAILABLE, reason="Module security non disponible")
class TestSecurityAudit:
    """Tests pour l'audit de sécurité des projets."""

    def test_security_audit_basic(self, tmp_path):
        """Test d'audit de sécurité de base."""
        proj = tmp_path / "test_project"
        proj.mkdir()

        # Créer des fichiers avec des problèmes de sécurité
        (proj / "danger.py").write_text(
            'password = "secret123"\napi_key = "sk-abcdef1234567890"'
        )
        (proj / "config.py").write_text('DATABASE_PASSWORD = "admin123"')

        # Exécuter l'audit
        security_audit_project(proj)

        # Vérifier que le rapport a été généré
        log = proj / "security_audit.txt"
        assert log.exists(), "Le rapport d'audit de sécurité doit être généré"

        content = log.read_text()

        # Vérifier la détection des problèmes
        assert any("Clé API trouvée" in line for line in content.splitlines()), (
            "Les clés API doivent être détectées"
        )
        assert any("Mot de passe en clair" in line for line in content.splitlines()), (
            "Les mots de passe en clair doivent être détectés"
        )

    def test_security_audit_clean_project(self, tmp_path):
        """Test d'audit sur un projet propre."""
        proj = tmp_path / "clean_project"
        proj.mkdir()

        # Créer des fichiers sans problèmes de sécurité
        (proj / "main.py").write_text('def main():\n    print("Hello World")')
        (proj / "config.py").write_text("DEBUG = True\nPORT = 8000")

        # Exécuter l'audit
        security_audit_project(proj)

        # Vérifier que le rapport a été généré
        log = proj / "security_audit.txt"
        assert log.exists(), (
            "Le rapport d'audit de sécurité doit être généré même pour un projet propre"
        )

        content = log.read_text()

        # Pour un projet propre, le rapport peut être vide ou contenir un message de succès
        # Le module retourne un score de 100 si aucun problème n'est détecté
        assert len(content.strip()) == 0 or "0 problème" in content, (
            "Un projet propre ne doit pas avoir de problèmes de sécurité"
        )

    def test_security_audit_empty_project(self, tmp_path):
        """Test d'audit sur un projet vide."""
        proj = tmp_path / "empty_project"
        proj.mkdir()

        # Exécuter l'audit sur un projet vide
        security_audit_project(proj)

        # Vérifier que le rapport a été généré
        log = proj / "security_audit.txt"
        assert log.exists(), (
            "Le rapport d'audit de sécurité doit être généré même pour un projet vide"
        )

    def test_security_audit_python_files_only(self, tmp_path):
        """Test d'audit sur des fichiers Python uniquement (comportement du module)."""
        proj = tmp_path / "python_project"
        proj.mkdir()

        # Créer des fichiers Python avec des problèmes détectables par le module
        (proj / "secrets.py").write_text(
            'DB_PASSWORD = "secret123"\nAPI_KEY = "sk-test123"'
        )
        (proj / "config.py").write_text('PASSWORD = "admin123"\nTOKEN = "secret456"')

        # Créer des fichiers non-Python qui ne seront pas scannés
        (proj / "secrets.env").write_text("DB_PASSWORD=secret123\nAPI_KEY=sk-test123")
        (proj / "config.json").write_text('{"password": "admin", "token": "secret"}')
        (proj / "script.sh").write_text('#!/bin/bash\necho "password=secret123"')

        # Exécuter l'audit
        security_audit_project(proj)

        # Vérifier que le rapport a été généré
        log = proj / "security_audit.txt"
        assert log.exists(), "Le rapport d'audit de sécurité doit être généré"

        content = log.read_text()

        # Vérifier que seuls les fichiers Python sont analysés
        assert "secrets.py" in content, "Les fichiers Python doivent être analysés"
        assert "config.py" in content, "Les fichiers Python doivent être analysés"
        # Les fichiers non-Python ne doivent pas apparaître dans le rapport
        assert "secrets.env" not in content, (
            "Les fichiers .env ne sont pas analysés par ce module"
        )
        assert "config.json" not in content, (
            "Les fichiers JSON ne sont pas analysés par ce module"
        )
        assert "script.sh" not in content, (
            "Les fichiers shell ne sont pas analysés par ce module"
        )


@pytest.mark.skipif(not SECURITY_AVAILABLE, reason="Module security non disponible")
def test_security_module_import():
    """Test d'import du module security."""
    from athalia_core.security import security_audit_project

    assert security_audit_project is not None
    assert callable(security_audit_project)
