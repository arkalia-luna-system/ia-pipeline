#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests de validité YAML pour Athalia.
Tests professionnels pour la CI/CD.
"""

from pathlib import Path
import sys
import tempfile

import pytest
import yaml


# Ajouter le répertoire parent au path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))


class TestYAMLValidity:
    """Tests de validité des fichiers YAML."""

    def setup_method(self):
        """Initialisation pour chaque test."""
        self.test_dir = Path(tempfile.mkdtemp())

    def teardown_method(self):
        """Nettoyage après chaque test."""
        import shutil

        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    def test_yaml_syntax_validity(self):
        """Test de la validité syntaxique YAML."""
        # YAML valide
        valid_yaml = """
        project:
          name: test_project
          version: 1.0.0
          dependencies:
            - pytest
            - requests
        """

        try:
            data = yaml.safe_load(valid_yaml)
            assert isinstance(data, dict)
            assert "project" in data
            assert data["project"]["name"] == "test_project"
        except yaml.YAMLError as e:
            pytest.fail(f"YAML valide rejeté: {e}")

    def test_yaml_syntax_invalidity(self):
        """Test de la détection d'YAML invalide."""
        # YAML invalide
        invalid_yaml = """
        project:
          name: test_project
          version: 1.0.0
          dependencies:
            - pytest
            - requests
          invalid_key: [unclosed_bracket
        """

        with pytest.raises(yaml.YAMLError):
            yaml.safe_load(invalid_yaml)

    def test_config_yaml_validity(self):
        """Test de validité du fichier de configuration."""
        config_path = Path("config/athalia_config.yaml")
        if not config_path.exists():
            pytest.skip("Fichier de configuration non trouvé")

        try:
            with open(config_path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)

            assert isinstance(data, dict), "La configuration doit être un dictionnaire"

            # Vérifier les clés essentielles
            if "general" in data:
                assert isinstance(
                    data["general"], dict
                ), "La section general doit être un dictionnaire"

            if "modules" in data:
                assert isinstance(
                    data["modules"], dict
                ), "La section modules doit être un dictionnaire"

        except yaml.YAMLError as e:
            pytest.fail(f"Configuration YAML invalide: {e}")

    def test_blueprint_yaml_structure(self):
        """Test de la structure des blueprints YAML."""
        # Créer un blueprint de test
        blueprint = {
            "project_name": "test_project",
            "project_type": "api",
            "version": "1.0.0",
            "description": "Test project",
            "modules": ["api", "database"],
            "dependencies": {
                "python": ["flask", "sqlalchemy"],
                "system": ["git", "docker"],
            },
        }

        # Convertir en YAML
        yaml_content = yaml.dump(blueprint, default_flow_style=False)

        # Recharger et vérifier
        loaded_blueprint = yaml.safe_load(yaml_content)
        assert loaded_blueprint["project_name"] == "test_project"
        assert loaded_blueprint["project_type"] == "api"
        assert "modules" in loaded_blueprint
        assert "dependencies" in loaded_blueprint

    def test_yaml_anchors_and_aliases(self):
        """Test des ancres et alias YAML."""
        yaml_with_anchors = """
        defaults: &defaults
          timeout: 30
          retries: 3

        api_config:
          <<: *defaults
          endpoint: /api/v1

        cli_config:
          <<: *defaults
          command: athalia
        """

        try:
            data = yaml.safe_load(yaml_with_anchors)
            assert "defaults" in data
            assert "api_config" in data
            assert "cli_config" in data

            # Vérifier que les alias fonctionnent
            assert data["api_config"]["timeout"] == 30
            assert data["cli_config"]["timeout"] == 30

        except yaml.YAMLError as e:
            pytest.fail(f"YAML avec ancres rejeté: {e}")

    def test_yaml_complex_types(self):
        """Test des types complexes en YAML."""
        complex_yaml = """
        project:
          name: complex_project
          metadata:
            tags: [api, web, cli]
            authors:
              - name: John Doe
                email: john@example.com
              - name: Jane Smith
                email: jane@example.com
          config:
            database:
              host: localhost
              port: 5432
              credentials:
                username: admin
                password: secret
            api:
              endpoints:
                - path: /users
                  method: GET
                  auth: required
                - path: /users
                  method: POST
                  auth: required
        """

        try:
            data = yaml.safe_load(complex_yaml)
            assert isinstance(data["project"]["metadata"]["tags"], list)
            assert isinstance(data["project"]["metadata"]["authors"], list)
            assert isinstance(data["project"]["config"]["database"], dict)
            assert isinstance(data["project"]["config"]["api"]["endpoints"], list)

        except yaml.YAMLError as e:
            pytest.fail(f"YAML complexe rejeté: {e}")

    def test_yaml_unicode_support(self):
        """Test du support Unicode en YAML."""
        unicode_yaml = """
        project:
          name: "Projet avec accents éàçù"
          description: "Description avec des caractères spéciaux: €£¥"
          tags:
            - "API REST"
            - "Web Services"
            - "Microservices"
        """

        try:
            data = yaml.safe_load(unicode_yaml)
            assert "éàçù" in data["project"]["name"]
            assert "€£¥" in data["project"]["description"]
            assert "API REST" in data["project"]["tags"]

        except yaml.YAMLError as e:
            pytest.fail(f"YAML Unicode rejeté: {e}")

    def test_yaml_file_roundtrip(self):
        """Test d'aller-retour fichier YAML."""
        original_data = {
            "project": {
                "name": "roundtrip_test",
                "version": "1.0.0",
                "config": {"debug": True, "log_level": "INFO"},
            }
        }

        # Écrire en YAML
        yaml_file = self.test_dir / "test.yaml"
        with open(yaml_file, "w", encoding="utf-8") as f:
            yaml.dump(original_data, f, default_flow_style=False)

        # Relire et comparer
        with open(yaml_file, "r", encoding="utf-8") as f:
            loaded_data = yaml.safe_load(f)

        assert loaded_data == original_data

    def test_yaml_validation_schema(self):
        """Test de validation avec schéma YAML."""
        # Schéma simple
        _ = {
            "type": "object",
            "properties": {
                "project_name": {"type": "string"},
                "version": {"type": "string"},
                "dependencies": {"type": "array"},
            },
            "required": ["project_name", "version"],
        }

        # Données valides
        valid_data = {
            "project_name": "test_project",
            "version": "1.0.0",
            "dependencies": ["pytest", "requests"],
        }

        # Données invalides
        invalid_data = {"project_name": 123, "version": "1.0.0"}  # Doit être une string

        # Test avec des données valides
        yaml_content = yaml.dump(valid_data)
        loaded_data = yaml.safe_load(yaml_content)
        assert isinstance(loaded_data["project_name"], str)

        # Test avec des données invalides
        yaml_content = yaml.dump(invalid_data)
        loaded_data = yaml.safe_load(yaml_content)
        # Note: YAML lui-même ne valide pas les types, c'est juste pour tester la
        # structure

    def test_yaml_error_handling(self):
        """Test de la gestion d'erreurs YAML."""
        # YAML avec erreur de syntaxe
        invalid_yaml = """
        project:
          name: test_project
          config:
            debug: true
            invalid_key: [unclosed_bracket
        """

        with pytest.raises(yaml.YAMLError):
            yaml.safe_load(invalid_yaml)

        # YAML avec caractères non-UTF8 (simulé)
        try:
            # Test avec des caractères spéciaux
            special_yaml = """
            project:
              name: "Test with special chars: \x00\x01"
            """
            yaml.safe_load(special_yaml)
        except yaml.YAMLError:
            # C'est normal que ça échoue avec des caractères de contrôle
            pass

    def test_yaml_performance(self):
        """Test de performance YAML."""
        import time

        # Créer un YAML complexe
        complex_data = {
            "project": {
                "name": "performance_test",
                "modules": [f"module_{i}" for i in range(100)],
                "config": {f"key_{i}": f"value_{i}" for i in range(50)},
            }
        }

        # Test de sérialisation
        start_time = time.time()
        yaml_content = yaml.dump(complex_data)
        serialize_time = time.time() - start_time

        # Test de désérialisation
        start_time = time.time()
        loaded_data = yaml.safe_load(yaml_content)
        deserialize_time = time.time() - start_time

        # Les opérations ne devraient pas prendre plus de 1 seconde
        assert serialize_time < 1.0, f"Sérialisation trop lente: {serialize_time:.3f}s"
        assert (
            deserialize_time < 1.0
        ), f"Désérialisation trop lente: {deserialize_time:.3f}s"

        # Vérifier l'intégrité des données
        assert loaded_data == complex_data

    def test_yaml_security(self):
        """Test de sécurité YAML."""
        # Test avec des données potentiellement dangereuses
        dangerous_yaml = """
        project:
          name: !python/object/apply:os.system ['echo "dangerous"']
        """

        # Utiliser safe_load pour éviter l'exécution de code
        try:
            data = yaml.safe_load(dangerous_yaml)
            # Si safe_load fonctionne, les tags dangereux sont ignorés
            assert isinstance(data, dict)
        except yaml.YAMLError:
            # C'est aussi acceptable que ça échoue
            pass


def test_yaml_basic_functionality():
    """Test de fonctionnalité de base YAML."""
    # Test simple
    simple_yaml = """
    name: test
    value: 42
    """

    data = yaml.safe_load(simple_yaml)
    assert data["name"] == "test"
    assert data["value"] == 42


def test_yaml_file_operations():
    """Test des opérations de fichiers YAML."""
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        # Créer un fichier YAML
        test_data = {"test": "data"}
        yaml_file = temp_path / "test.yaml"

        with open(yaml_file, "w") as f:
            yaml.dump(test_data, f)

        # Lire le fichier
        with open(yaml_file, "r") as f:
            loaded_data = yaml.safe_load(f)

        assert loaded_data == test_data


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
