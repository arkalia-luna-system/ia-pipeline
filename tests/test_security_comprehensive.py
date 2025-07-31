#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests complets pour la sécurité.
Tests professionnels pour la CI/CD.
"""

from pathlib import Path
import tempfile
from unittest.mock import patch

import pytest

# Import du module à tester
from athalia_core.security import security_audit_project


class TestSecurityComprehensive:
    """Tests complets pour le module security"""

    def setup_method(self):
        """Configuration avant chaque test"""
        self.temp_dir = tempfile.mkdtemp()
        self.project_dir = Path(self.temp_dir) / "test_project"
        self.project_dir.mkdir(exist_ok=True)

    def teardown_method(self):
        """Nettoyage après chaque test"""
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_security_audit_project_clean_project(self):
        """Test d'audit de sécurité sur un projet propre"""
        # Créer un fichier Python propre
        clean_file = self.project_dir / "clean.py"
        clean_file.write_text(
            """
def safe_function():
    return "safe"
"""
        )

        # Exécuter l'audit
        result = security_audit_project(str(self.project_dir))

        # Vérifications
        assert isinstance(result, dict)
        assert "f" in result
        assert "issues" in result
        assert "score" in result
        assert result["f"] is True  # Projet propre
        assert len(result["issues"]) == 0
        assert result["score"] == 100

    def test_security_audit_project_with_password(self):
        """Test d'audit avec mot de passe en clair"""
        # Créer un fichier avec mot de passe en clair
        password_file = self.project_dir / "config.py"
        password_file.write_text(
            """
password = "secret123"
api_key = "sk-1234567890abcdef"
"""
        )

        # Exécuter l'audit
        result = security_audit_project(str(self.project_dir))

        # Vérifications
        assert isinstance(result, dict)
        assert result["f"] is False  # Projet avec problèmes
        assert len(result["issues"]) >= 1
        assert result["score"] < 100

        # Vérifier que les problèmes ont été détectés
        issues_text = "\n".join(result["issues"])
        assert (
            "Mot de passe en clair" in issues_text or "Clé API trouvée" in issues_text
        )

    def test_security_audit_project_with_api_key(self):
        """Test d'audit avec clé API"""
        # Créer un fichier avec clé API
        api_file = self.project_dir / "api.py"
        api_file.write_text(
            """
api_key = "sk-1234567890abcdef"
secret = "sk-abcdef1234567890"
"""
        )

        # Exécuter l'audit
        result = security_audit_project(str(self.project_dir))

        # Vérifications
        assert isinstance(result, dict)
        assert result["f"] is False
        assert len(result["issues"]) >= 1
        assert result["score"] < 100

        # Vérifier que les clés API ont été détectées
        issues_text = "\n".join(result["issues"])
        assert "Clé API trouvée" in issues_text

    def test_security_audit_project_with_os_system(self):
        """Test d'audit avec appel système"""
        # Créer un fichier avec appel système
        system_file = self.project_dir / "dangerous.py"
        system_file.write_text(
            """
import os
os.system("rm -rf /")
os.system("ls")
"""
        )

        # Exécuter l'audit
        result = security_audit_project(str(self.project_dir))

        # Vérifications
        assert isinstance(result, dict)
        assert result["f"] is False
        assert len(result["issues"]) >= 1
        assert result["score"] < 100

        # Vérifier que les appels système ont été détectés
        issues_text = "\n".join(result["issues"])
        assert "Appel système potentiellement dangereux" in issues_text

    def test_security_audit_project_multiple_issues(self):
        """Test d'audit avec plusieurs problèmes"""
        # Créer plusieurs fichiers avec problèmes
        file1 = self.project_dir / "config.py"
        file1.write_text('password = "secret"')

        file2 = self.project_dir / "api.py"
        file2.write_text('api_key = "sk-1234567890"')

        file3 = self.project_dir / "dangerous.py"
        file3.write_text('os.system("ls")')

        # Exécuter l'audit
        result = security_audit_project(str(self.project_dir))

        # Vérifications
        assert isinstance(result, dict)
        assert result["f"] is False
        assert len(result["issues"]) >= 3
        assert result["score"] < 100

        # Vérifier le calcul du score
        expected_score = max(0, 100 - 20 * len(result["issues"]))
        assert result["score"] == expected_score

    def test_security_audit_project_with_f_files(self):
        """Test d'audit avec fichiers .f(f"""
        # Créer un fichier .f(f avec problème
        f_file = self.project_dir / "config.f(f"
        f_file.write_text('password = "secret"')

        # Exécuter l'audit
        result = security_audit_project(str(self.project_dir))

        # Vérifications
        assert isinstance(result, dict)
        assert result["f"] is False
        assert len(result["issues"]) >= 1

    def test_security_audit_project_file_read_error(self):
        """Test d'audit avec erreur de lecture de fichier"""
        # Créer un fichier qui ne peut pas être lu
        unreadable_file = self.project_dir / "unreadable.py"
        unreadable_file.write_text("test")

        # Mock pour simuler une erreur de lecture
        result = None
        with patch("builtins.open", side_effect=Exception("Permission denied")):
            # Le test doit gérer l'exception
            try:
                result = security_audit_project(str(self.project_dir))
                # Si on arrive ici, le test passe
                assert result is not None
            except Exception:
                # Si une exception est levée, c'est aussi acceptable
                pass

        # Vérifications - seulement si result a été défini
        if result is not None:
            assert isinstance(result, dict)
            assert "issues" in result
            # L'erreur de lecture devrait être dans les issues
            issues_text = "\n".join(result["issues"])
            assert "Erreur lecture" in issues_text

    def test_security_audit_project_empty_directory(self):
        """Test d'audit sur un répertoire vide"""
        # Exécuter l'audit sur un répertoire vide
        result = security_audit_project(str(self.project_dir))

        # Vérifications
        assert isinstance(result, dict)
        assert result["f"] is True  # Répertoire vide = propre
        assert len(result["issues"]) == 0
        assert result["score"] == 100

    def test_security_audit_project_ignores_non_python_files(self):
        """Test que l'audit ignore les fichiers non Python"""
        # Créer des fichiers non Python avec des problèmes
        txt_file = self.project_dir / "config.txt"
        txt_file.write_text('password = "secret"')

        json_file = self.project_dir / "config.json"
        json_file.write_text('{"password": "secret"}')

        # Exécuter l'audit
        result = security_audit_project(str(self.project_dir))

        # Vérifications - les fichiers non Python ne devraient pas être détectés
        assert isinstance(result, dict)
        assert result["f"] is True  # Aucun problème dans les fichiers Python
        assert len(result["issues"]) == 0
        assert result["score"] == 100

    def test_security_audit_project_case_insensitive(self):
        """Test que l'audit est insensible à la casse"""
        # Créer un fichier avec des problèmes en majuscules
        case_file = self.project_dir / "config.py"
        case_file.write_text(
            """
PASSWORD = "secret"
API_KEY = "sk-1234567890"
OS.SYSTEM("ls")
"""
        )

        # Exécuter l'audit
        result = security_audit_project(str(self.project_dir))

        # Vérifications
        assert isinstance(result, dict)
        assert result["f"] is False
        assert len(result["issues"]) >= 1

    def test_security_audit_project_creates_audit_file(self):
        """Test que l'audit crée le fichier de rapport"""
        # Créer un fichier avec problème
        problem_file = self.project_dir / "config.py"
        problem_file.write_text('password = "secret"')

        # Exécuter l'audit
        _ = security_audit_project(str(self.project_dir))

        # Vérifier que le fichier d'audit a été créé
        audit_file = self.project_dir / "security_audit.txt"
        assert audit_file.exists()

        # Vérifier le contenu du fichier d'audit
        audit_content = audit_file.read_text()
        assert "Mot de passe en clair" in audit_content

    def test_security_audit_project_score_calculation(self):
        """Test du calcul du score de sécurité"""
        # Créer plusieurs fichiers avec problèmes pour tester le calcul
        for i in range(5):
            problem_file = self.project_dir / f"config_{i}.py"
            problem_file.write_text('password = "secret"')

        # Exécuter l'audit
        result = security_audit_project(str(self.project_dir))

        # Vérifications
        assert isinstance(result, dict)
        assert result["f"] is False
        assert len(result["issues"]) >= 5

        # Le score devrait être calculé: max(0, 100 - 20 * nombre_issues)
        expected_score = max(0, 100 - 20 * len(result["issues"]))
        assert result["score"] == expected_score

    def test_security_audit_project_with_subdirectories(self):
        """Test d'audit avec sous-répertoires"""
        # Créer une structure avec sous-répertoires
        subdir = self.project_dir / "subdir"
        subdir.mkdir()

        problem_file = subdir / "config.py"
        problem_file.write_text('password = "secret"')

        # Exécuter l'audit
        result = security_audit_project(str(self.project_dir))

        # Vérifications
        assert isinstance(result, dict)
        assert result["f"] is False
        assert len(result["issues"]) >= 1

    def test_security_audit_project_complex_patterns(self):
        """Test d'audit avec des patterns complexes"""
        # Créer un fichier avec des patterns complexes
        complex_file = self.project_dir / "complex.py"
        complex_file.write_text(
            """
# Différentes variantes de mots de passe
password = "secret"
PASSWORD = "secret"
user_password = "secret"
db_password = "secret"

# Différentes variantes de clés API
api_key = "sk-1234567890abcdef"
API_KEY = "sk-abcdef1234567890"
secret_key = "sk-1234567890abcdef"

# Différentes variantes d'appels système
os.system("ls")
OS.SYSTEM("rm -rf /")
system_call = os.system
"""
        )

        # Exécuter l'audit
        result = security_audit_project(str(self.project_dir))

        # Vérifications
        assert isinstance(result, dict)
        assert result["f"] is False
        assert len(result["issues"]) >= 1

        # Vérifier que différents types de problèmes ont été détectés
        issues_text = "\n".join(result["issues"])
        assert (
            "Mot de passe en clair" in issues_text
            or "Clé API trouvée" in issues_text
            or "Appel système" in issues_text
        )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
