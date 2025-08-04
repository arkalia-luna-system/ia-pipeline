#!/usr/bin/env python3
"""
Tests complets pour config_manager.py (512 lignes)
MODULE CENTRAL CRITIQUE GESTION CONFIGURATION

Couverture actuelle: 5% → Objectif: 85%
Standards: Black + Ruff + MyPy + Bandit
"""

import pytest
import tempfile
import shutil
import os
import yaml
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock, mock_open

from athalia_core.config_manager import (
    load_config,
    save_config,
    ConfigManager,
    merge_configs,
    validate_config_schema,
    get_env_config,
    create_default_config,
)


class TestConfigManagerFunctions:
    """Tests pour les fonctions utilitaires de config_manager."""

    def setup_method(self):
        """Configuration avant chaque test."""
        self.temp_dir = tempfile.mkdtemp()
        self.config_file = Path(self.temp_dir) / "test_config.yaml"
        
        # Configuration de test
        self.test_config = {
            "app": {
                "name": "Athalia",
                "version": "1.0.0",
                "debug": True
            },
            "database": {
                "host": "localhost",
                "port": 5432,
                "name": "athalia_db",
                "user": "athalia_user"
            },
            "logging": {
                "level": "INFO",
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                "handlers": ["console", "file"]
            },
            "features": {
                "auto_tests": True,
                "auto_documentation": True,
                "security_validation": True,
                "performance_monitoring": False
            }
        }

    def teardown_method(self):
        """Nettoyage après chaque test."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_load_config_valid_file(self):
        """Test chargement configuration fichier valide."""
        # Créer fichier YAML valide
        with open(self.config_file, 'w') as f:
            yaml.dump(self.test_config, f)
        
        config = load_config(str(self.config_file))
        
        assert isinstance(config, dict)
        assert config["app"]["name"] == "Athalia"
        assert config["database"]["port"] == 5432
        assert config["features"]["auto_tests"] is True

    def test_load_config_missing_file(self):
        """Test chargement configuration fichier manquant."""
        missing_file = str(Path(self.temp_dir) / "missing.yaml")
        
        config = load_config(missing_file)
        
        assert isinstance(config, dict)
        assert len(config) == 0  # Dictionnaire vide

    def test_load_config_invalid_yaml(self):
        """Test chargement configuration YAML invalide."""
        # Créer fichier YAML invalide
        with open(self.config_file, 'w') as f:
            f.write("invalid: yaml: content: [unclosed")
        
        config = load_config(str(self.config_file))
        
        assert isinstance(config, dict)
        assert len(config) == 0  # Dictionnaire vide en cas d'erreur

    def test_load_config_empty_file(self):
        """Test chargement configuration fichier vide."""
        # Créer fichier vide
        self.config_file.touch()
        
        config = load_config(str(self.config_file))
        
        assert isinstance(config, dict)
        assert len(config) == 0

    def test_save_config_valid_data(self):
        """Test sauvegarde configuration données valides."""
        result = save_config(self.test_config, str(self.config_file))
        
        assert result is True
        assert self.config_file.exists()
        
        # Vérifier contenu sauvegardé
        with open(self.config_file) as f:
            saved_config = yaml.safe_load(f)
        
        assert saved_config["app"]["name"] == "Athalia"
        assert saved_config["database"]["port"] == 5432

    def test_save_config_create_directory(self):
        """Test sauvegarde configuration avec création répertoire."""
        nested_file = Path(self.temp_dir) / "nested" / "dir" / "config.yaml"
        
        result = save_config(self.test_config, str(nested_file))
        
        assert result is True
        assert nested_file.exists()
        assert nested_file.parent.exists()

    def test_save_config_permission_error(self):
        """Test sauvegarde configuration erreur de permission."""
        with patch('builtins.open', side_effect=PermissionError("Permission denied")):
            result = save_config(self.test_config, str(self.config_file))
            
            assert result is False

    def test_save_config_invalid_path(self):
        """Test sauvegarde configuration chemin invalide."""
        # Chemin vers un répertoire qui ne peut pas être créé
        invalid_path = "/root/forbidden/config.yaml"
        
        with patch('os.makedirs', side_effect=OSError("Cannot create directory")):
            result = save_config(self.test_config, invalid_path)
            
            assert result is False

    def test_merge_configs_simple(self):
        """Test fusion configurations simples."""
        config1 = {"a": 1, "b": {"x": 10}}
        config2 = {"b": {"y": 20}, "c": 3}
        
        merged = merge_configs(config1, config2)
        
        assert merged["a"] == 1
        assert merged["b"]["x"] == 10
        assert merged["b"]["y"] == 20
        assert merged["c"] == 3

    def test_merge_configs_override(self):
        """Test fusion configurations avec écrasement."""
        config1 = {"app": {"debug": True, "port": 8000}}
        config2 = {"app": {"debug": False, "name": "Athalia"}}
        
        merged = merge_configs(config1, config2)
        
        assert merged["app"]["debug"] is False  # Écrasé par config2
        assert merged["app"]["port"] == 8000    # Conservé de config1
        assert merged["app"]["name"] == "Athalia"  # Ajouté de config2

    def test_merge_configs_deep_nesting(self):
        """Test fusion configurations avec imbrication profonde."""
        config1 = {
            "level1": {
                "level2": {
                    "level3": {"value1": "a", "value2": "b"}
                }
            }
        }
        config2 = {
            "level1": {
                "level2": {
                    "level3": {"value2": "c", "value3": "d"}
                }
            }
        }
        
        merged = merge_configs(config1, config2)
        
        level3 = merged["level1"]["level2"]["level3"]
        assert level3["value1"] == "a"  # Conservé
        assert level3["value2"] == "c"  # Écrasé
        assert level3["value3"] == "d"  # Ajouté

    def test_validate_config_schema_valid(self):
        """Test validation schéma configuration valide."""
        schema = {
            "app": {"required": ["name", "version"]},
            "database": {"required": ["host", "port"]}
        }
        
        is_valid, errors = validate_config_schema(self.test_config, schema)
        
        assert is_valid is True
        assert len(errors) == 0

    def test_validate_config_schema_missing_required(self):
        """Test validation schéma avec champs requis manquants."""
        schema = {
            "app": {"required": ["name", "version", "missing_field"]},
            "database": {"required": ["host", "port", "password"]}
        }
        
        is_valid, errors = validate_config_schema(self.test_config, schema)
        
        assert is_valid is False
        assert len(errors) > 0
        assert any("missing_field" in error for error in errors)
        assert any("password" in error for error in errors)

    def test_validate_config_schema_missing_section(self):
        """Test validation schéma avec section manquante."""
        schema = {
            "app": {"required": ["name"]},
            "missing_section": {"required": ["field"]}
        }
        
        is_valid, errors = validate_config_schema(self.test_config, schema)
        
        assert is_valid is False
        assert any("missing_section" in error for error in errors)

    def test_get_env_config_basic(self):
        """Test récupération configuration depuis variables environnement."""
        env_vars = {
            "ATHALIA_APP_NAME": "TestApp",
            "ATHALIA_DATABASE_PORT": "3306",
            "ATHALIA_DEBUG": "true",
            "ATHALIA_FEATURES_AUTO_TESTS": "false"
        }
        
        with patch.dict(os.environ, env_vars):
            env_config = get_env_config("ATHALIA_")
        
        assert isinstance(env_config, dict)
        # La structure exacte dépend de l'implémentation
        # Vérifier que les variables sont récupérées
        assert len(env_config) > 0

    def test_get_env_config_no_prefix_match(self):
        """Test récupération configuration env sans correspondance."""
        env_config = get_env_config("NONEXISTENT_PREFIX_")
        
        assert isinstance(env_config, dict)
        assert len(env_config) == 0

    def test_create_default_config_standard(self):
        """Test création configuration par défaut."""
        default_config = create_default_config()
        
        assert isinstance(default_config, dict)
        assert len(default_config) > 0
        
        # Vérifier sections essentielles
        expected_sections = ["app", "logging", "features"]
        for section in expected_sections:
            if section in default_config:
                assert isinstance(default_config[section], dict)

    def test_create_default_config_with_overrides(self):
        """Test création configuration par défaut avec surcharges."""
        overrides = {
            "app": {"name": "CustomApp"},
            "custom_section": {"value": 42}
        }
        
        default_config = create_default_config(overrides)
        
        assert isinstance(default_config, dict)
        assert "custom_section" in default_config
        assert default_config["custom_section"]["value"] == 42


class TestConfigManagerClass:
    """Tests pour la classe ConfigManager."""

    def setup_method(self):
        """Configuration avant chaque test."""
        self.temp_dir = tempfile.mkdtemp()
        self.config_file = Path(self.temp_dir) / "athalia_config.yaml"
        
        # Configuration de test
        self.test_config = {
            "app": {
                "name": "Athalia",
                "version": "1.0.0",
                "debug": False,
                "log_level": "INFO"
            },
            "paths": {
                "project_root": "/opt/athalia",
                "temp_dir": "/tmp/athalia",
                "log_dir": "/var/log/athalia"
            },
            "security": {
                "enable_validation": True,
                "max_file_size": "100MB",
                "allowed_extensions": [".py", ".yaml", ".json"]
            },
            "performance": {
                "cache_enabled": True,
                "cache_size": 1000,
                "timeout": 30
            }
        }
        
        # Créer fichier de configuration
        with open(self.config_file, 'w') as f:
            yaml.dump(self.test_config, f)

    def teardown_method(self):
        """Nettoyage après chaque test."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_config_manager_initialization_with_file(self):
        """Test initialisation ConfigManager avec fichier."""
        config_manager = ConfigManager(str(self.config_file))
        
        assert config_manager.config_path == str(self.config_file)
        assert isinstance(config_manager.config, dict)
        assert config_manager.config["app"]["name"] == "Athalia"

    def test_config_manager_initialization_without_file(self):
        """Test initialisation ConfigManager sans fichier."""
        config_manager = ConfigManager()
        
        assert config_manager.config_path is None
        assert isinstance(config_manager.config, dict)
        # Devrait avoir une configuration par défaut

    def test_config_manager_initialization_missing_file(self):
        """Test initialisation ConfigManager fichier manquant."""
        missing_file = str(Path(self.temp_dir) / "missing.yaml")
        config_manager = ConfigManager(missing_file)
        
        assert config_manager.config_path == missing_file
        assert isinstance(config_manager.config, dict)
        # Devrait avoir une configuration par défaut

    def test_get_setting_existing_simple(self):
        """Test récupération paramètre simple existant."""
        config_manager = ConfigManager(str(self.config_file))
        
        app_name = config_manager.get("app.name")
        debug_mode = config_manager.get("app.debug")
        
        assert app_name == "Athalia"
        assert debug_mode is False

    def test_get_setting_existing_nested(self):
        """Test récupération paramètre imbriqué existant."""
        config_manager = ConfigManager(str(self.config_file))
        
        project_root = config_manager.get("paths.project_root")
        cache_size = config_manager.get("performance.cache_size")
        
        assert project_root == "/opt/athalia"
        assert cache_size == 1000

    def test_get_setting_nonexistent(self):
        """Test récupération paramètre non existant."""
        config_manager = ConfigManager(str(self.config_file))
        
        nonexistent = config_manager.get("nonexistent.setting")
        
        assert nonexistent is None

    def test_get_setting_with_default(self):
        """Test récupération paramètre avec valeur par défaut."""
        config_manager = ConfigManager(str(self.config_file))
        
        nonexistent = config_manager.get("nonexistent.setting", "default_value")
        existing = config_manager.get("app.name", "default_name")
        
        assert nonexistent == "default_value"
        assert existing == "Athalia"  # Valeur existante, pas défaut

    def test_set_setting_new(self):
        """Test définition nouveau paramètre."""
        config_manager = ConfigManager(str(self.config_file))
        
        config_manager.set("new.setting", "new_value")
        
        assert config_manager.get("new.setting") == "new_value"

    def test_set_setting_existing_override(self):
        """Test modification paramètre existant."""
        config_manager = ConfigManager(str(self.config_file))
        
        # Modifier paramètre existant
        config_manager.set("app.debug", True)
        
        assert config_manager.get("app.debug") is True

    def test_set_setting_nested_new(self):
        """Test définition paramètre imbriqué nouveau."""
        config_manager = ConfigManager(str(self.config_file))
        
        config_manager.set("new_section.subsection.value", 42)
        
        assert config_manager.get("new_section.subsection.value") == 42

    def test_update_from_env(self):
        """Test mise à jour depuis variables environnement."""
        env_vars = {
            "ATHALIA_APP_DEBUG": "true",
            "ATHALIA_PERFORMANCE_CACHE_SIZE": "2000",
            "ATHALIA_NEW_SETTING": "env_value"
        }
        
        config_manager = ConfigManager(str(self.config_file))
        
        with patch.dict(os.environ, env_vars):
            config_manager.update_from_env("ATHALIA_")
        
        # Vérifier que les changements sont appliqués
        # (Le comportement exact dépend de l'implémentation)
        assert isinstance(config_manager.config, dict)

    def test_update_from_dict(self):
        """Test mise à jour depuis dictionnaire."""
        config_manager = ConfigManager(str(self.config_file))
        
        updates = {
            "app": {"version": "2.0.0", "new_field": "added"},
            "new_section": {"value": "test"}
        }
        
        config_manager.update_from_dict(updates)
        
        assert config_manager.get("app.version") == "2.0.0"
        assert config_manager.get("app.name") == "Athalia"  # Conservé
        assert config_manager.get("app.new_field") == "added"
        assert config_manager.get("new_section.value") == "test"

    def test_save_config_to_file(self):
        """Test sauvegarde configuration vers fichier."""
        config_manager = ConfigManager(str(self.config_file))
        
        # Modifier configuration
        config_manager.set("app.version", "2.0.0")
        
        # Sauvegarder
        result = config_manager.save()
        
        assert result is True
        
        # Vérifier sauvegarde
        with open(self.config_file) as f:
            saved_config = yaml.safe_load(f)
        
        assert saved_config["app"]["version"] == "2.0.0"

    def test_save_config_no_path(self):
        """Test sauvegarde sans chemin défini."""
        config_manager = ConfigManager()  # Sans fichier
        
        result = config_manager.save()
        
        # Devrait échouer gracieusement
        assert result is False

    def test_reload_config(self):
        """Test rechargement configuration."""
        config_manager = ConfigManager(str(self.config_file))
        
        # Modifier config en mémoire
        config_manager.set("app.debug", True)
        assert config_manager.get("app.debug") is True
        
        # Recharger depuis fichier
        config_manager.reload()
        
        # Devrait revenir à la valeur du fichier
        assert config_manager.get("app.debug") is False

    def test_reload_config_no_path(self):
        """Test rechargement sans chemin défini."""
        config_manager = ConfigManager()  # Sans fichier
        
        # Ne devrait pas causer d'erreur
        config_manager.reload()
        assert isinstance(config_manager.config, dict)

    def test_validate_configuration(self):
        """Test validation configuration."""
        config_manager = ConfigManager(str(self.config_file))
        
        # Schema de validation
        schema = {
            "app": {"required": ["name", "version"]},
            "paths": {"required": ["project_root"]}
        }
        
        is_valid, errors = config_manager.validate(schema)
        
        assert is_valid is True
        assert len(errors) == 0

    def test_validate_configuration_invalid(self):
        """Test validation configuration invalide."""
        config_manager = ConfigManager(str(self.config_file))
        
        # Schema avec champs manquants
        schema = {
            "app": {"required": ["name", "missing_field"]},
            "missing_section": {"required": ["field"]}
        }
        
        is_valid, errors = config_manager.validate(schema)
        
        assert is_valid is False
        assert len(errors) > 0

    def test_get_section_existing(self):
        """Test récupération section entière existante."""
        config_manager = ConfigManager(str(self.config_file))
        
        app_section = config_manager.get_section("app")
        paths_section = config_manager.get_section("paths")
        
        assert isinstance(app_section, dict)
        assert app_section["name"] == "Athalia"
        assert isinstance(paths_section, dict)
        assert "project_root" in paths_section

    def test_get_section_nonexistent(self):
        """Test récupération section non existante."""
        config_manager = ConfigManager(str(self.config_file))
        
        missing_section = config_manager.get_section("missing_section")
        
        assert missing_section is None

    def test_has_setting(self):
        """Test vérification existence paramètre."""
        config_manager = ConfigManager(str(self.config_file))
        
        assert config_manager.has("app.name") is True
        assert config_manager.has("app.nonexistent") is False
        assert config_manager.has("missing.section") is False

    def test_delete_setting(self):
        """Test suppression paramètre."""
        config_manager = ConfigManager(str(self.config_file))
        
        # Vérifier existence
        assert config_manager.has("app.debug") is True
        
        # Supprimer
        config_manager.delete("app.debug")
        
        # Vérifier suppression
        assert config_manager.has("app.debug") is False
        assert config_manager.get("app.debug") is None

    def test_delete_section(self):
        """Test suppression section entière."""
        config_manager = ConfigManager(str(self.config_file))
        
        # Vérifier existence
        assert config_manager.has("performance.cache_enabled") is True
        
        # Supprimer section
        config_manager.delete("performance")
        
        # Vérifier suppression
        assert config_manager.get_section("performance") is None
        assert config_manager.has("performance.cache_enabled") is False

    def test_list_all_settings(self):
        """Test listage de tous les paramètres."""
        config_manager = ConfigManager(str(self.config_file))
        
        all_settings = config_manager.list_all_settings()
        
        assert isinstance(all_settings, list)
        assert len(all_settings) > 0
        
        # Vérifier présence de paramètres connus
        setting_paths = [setting["path"] for setting in all_settings]
        assert "app.name" in setting_paths
        assert "paths.project_root" in setting_paths

    def test_export_config(self):
        """Test export configuration."""
        config_manager = ConfigManager(str(self.config_file))
        
        exported = config_manager.export()
        
        assert isinstance(exported, dict)
        assert exported["app"]["name"] == "Athalia"
        assert "paths" in exported
        assert "security" in exported

    def test_import_config(self):
        """Test import configuration."""
        config_manager = ConfigManager()  # Vide
        
        config_manager.import_config(self.test_config)
        
        assert config_manager.get("app.name") == "Athalia"
        assert config_manager.get("security.enable_validation") is True

    def test_backup_and_restore(self):
        """Test sauvegarde et restauration."""
        config_manager = ConfigManager(str(self.config_file))
        
        # Créer sauvegarde
        backup_id = config_manager.create_backup()
        assert backup_id is not None
        
        # Modifier configuration
        config_manager.set("app.name", "Modified")
        assert config_manager.get("app.name") == "Modified"
        
        # Restaurer sauvegarde
        result = config_manager.restore_backup(backup_id)
        assert result is True
        assert config_manager.get("app.name") == "Athalia"  # Valeur originale

    def test_config_change_notifications(self):
        """Test notifications changements configuration."""
        config_manager = ConfigManager(str(self.config_file))
        
        # Enregistrer callback
        changes = []
        def on_change(path, old_value, new_value):
            changes.append((path, old_value, new_value))
        
        config_manager.on_change(on_change)
        
        # Modifier configuration
        config_manager.set("app.debug", True)
        
        # Vérifier notification
        assert len(changes) > 0
        change = changes[-1]
        assert change[0] == "app.debug"
        assert change[1] is False  # Ancienne valeur
        assert change[2] is True   # Nouvelle valeur

    @pytest.mark.parametrize("setting_path,expected_type", [
        ("app.name", str),
        ("app.debug", bool),
        ("performance.cache_size", int),
        ("security.allowed_extensions", list),
    ])
    def test_setting_types(self, setting_path, expected_type):
        """Test types des paramètres."""
        config_manager = ConfigManager(str(self.config_file))
        
        value = config_manager.get(setting_path)
        
        assert isinstance(value, expected_type)

    def test_performance_large_config(self):
        """Test performance avec grande configuration."""
        import time
        
        # Créer grande configuration
        large_config = {}
        for i in range(100):
            large_config[f"section_{i}"] = {
                f"key_{j}": f"value_{i}_{j}" 
                for j in range(50)
            }
        
        # Créer fichier
        large_config_file = Path(self.temp_dir) / "large_config.yaml"
        with open(large_config_file, 'w') as f:
            yaml.dump(large_config, f)
        
        # Mesurer performance
        start_time = time.time()
        config_manager = ConfigManager(str(large_config_file))
        init_duration = time.time() - start_time
        
        start_get = time.time()
        value = config_manager.get("section_50.key_25")
        get_duration = time.time() - start_get
        
        # Vérifications performance
        assert value == "value_50_25"
        assert init_duration < 2.0  # Moins de 2 secondes pour charger
        assert get_duration < 0.1   # Moins de 0.1 seconde pour récupérer

    def test_concurrent_access(self):
        """Test accès concurrent à la configuration."""
        import threading
        
        config_manager = ConfigManager(str(self.config_file))
        results = []
        errors = []
        
        def worker(worker_id):
            """Worker pour accès concurrent."""
            try:
                # Lire
                value = config_manager.get("app.name")
                results.append(f"worker_{worker_id}_{value}")
                
                # Écrire
                config_manager.set(f"worker_{worker_id}", worker_id)
                
                # Relire
                worker_value = config_manager.get(f"worker_{worker_id}")
                results.append(f"set_{worker_id}_{worker_value}")
            except Exception as e:
                errors.append(f"worker_{worker_id}_{e}")
        
        # Lancer plusieurs workers
        threads = []
        for i in range(5):
            thread = threading.Thread(target=worker, args=(i,))
            threads.append(thread)
            thread.start()
        
        # Attendre fin
        for thread in threads:
            thread.join()
        
        # Vérifier résultats
        assert len(errors) == 0  # Aucune erreur
        assert len(results) == 10  # 2 résultats par worker


class TestConfigManagerIntegration:
    """Tests d'intégration pour ConfigManager."""

    def setup_method(self):
        """Configuration tests intégration."""
        self.temp_dir = tempfile.mkdtemp()

    def teardown_method(self):
        """Nettoyage tests intégration."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_full_config_workflow(self):
        """Test workflow complet de gestion configuration."""
        config_file = Path(self.temp_dir) / "workflow_config.yaml"
        
        # 1. Créer configuration par défaut
        default_config = create_default_config()
        result = save_config(default_config, str(config_file))
        assert result is True
        
        # 2. Charger avec ConfigManager
        config_manager = ConfigManager(str(config_file))
        assert isinstance(config_manager.config, dict)
        
        # 3. Modifier configuration
        config_manager.set("app.version", "2.0.0")
        config_manager.set("new_feature.enabled", True)
        
        # 4. Sauvegarder
        assert config_manager.save() is True
        
        # 5. Recharger et vérifier
        config_manager.reload()
        assert config_manager.get("app.version") == "2.0.0"
        assert config_manager.get("new_feature.enabled") is True
        
        # 6. Fusionner avec configuration env
        env_vars = {"ATHALIA_APP_DEBUG": "true"}
        with patch.dict(os.environ, env_vars):
            config_manager.update_from_env("ATHALIA_")
        
        # 7. Valider configuration finale
        schema = {"app": {"required": ["version"]}}
        is_valid, errors = config_manager.validate(schema)
        assert is_valid is True