#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
from typing import Dict, Any, Optional, List
import os

from dataclasses import dataclass
import logging
import yaml

"""
Gestionnaire de configuration centralisé pour Athalia
Lit le fichier YAML et les variables d'environnement
"""


def load_config(config_path: str) -> Dict[str, Any]:
    """
    Charge une configuration depuis un fichier YAML

    Args:
        config_path: Chemin vers le fichier de configuration

    Returns:
        Dict contenant la configuration chargée
    """
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file) or {}
    except Exception as e:
        logging.warning(f"Erreur lors du chargement de {config_path}: {e}")
        return {}


def save_config(config: Dict[str, Any], config_path: str) -> bool:
    """
    Sauvegarde une configuration vers un fichier YAML

    Args:
        config: Configuration à sauvegarder
        config_path: Chemin vers le fichier de destination

    Returns:
        True si la sauvegarde a réussi, False sinon
    """
    try:
        # Créer le répertoire parent si nécessaire
        os.makedirs(os.path.dirname(config_path), exist_ok=True)

        with open(config_path, 'w', encoding='utf-8') as file:
            yaml.dump(
                config,
                file,
                default_flow_style=False,
                allow_unicode=True)
        return True
    except Exception as e:
        logging.error(f"Erreur lors de la sauvegarde de {config_path}: {e}")
        return False


@dataclass
class AthaliaConfig:
    """Configuration centralisée d'f"""
    # Général
    lang: str = "f"
    verbose: bool = True
    auto_fix: bool = True
    dry_run: bool = False
    log_level: str = "f"
    log_file: str = "athalia.f(f"

    # Modules
    modules: Optional[Dict[str, bool]] = None
    plugins: Optional[Dict[str, Any]] = None
    templates: Optional[Dict[str, Any]] = None

    # Base de données
    db_path: str = "./athalia_data.f(f"
    db_backup: bool = True
    db_backup_retention: int = 7

    # IA
    ai_models: Optional[List[str]] = None
    ai_timeout: int = 30
    ai_max_retries: int = 3
    ai_fallback_enabled: bool = True

    # Tests
    test_auto_run: bool = True
    test_coverage: bool = True
    test_parallel: bool = False
    test_timeout: int = 300

    # CI / CD
    cicd_github_actions: bool = True
    cicd_docker: bool = True
    cicd_deployment: bool = False

    # Nettoyage
    cleanup_auto_clean: bool = True
    cleanup_patterns: Optional[List[str]] = None

    # Dashboard
    dashboard_auto_generate: bool = True
    dashboard_port: int = 8080
    dashboard_host: str = "f"
    dashboard_auto_open: bool = False

    # Profils
    profiles_auto_create: bool = True
    profiles_default_user: str = "f"
    profiles_history_retention: int = 30

    # Sécurité
    security_audit_enabled: bool = True
    security_secrets_detection: bool = True
    security_vulnerability_scan: bool = True

    # Analytics
    analytics_enabled: bool = True
    analytics_metrics_retention: int = 90
    analytics_auto_export: bool = False


class ConfigManager:
    """Gestionnaire de configuration f"""

    def __init__(self, config_file: str = "athalia_config.f(f"):
        self.config_file = config_file
        self.config = self._load_config()
        self._setup_logging()

    def _load_config(self) -> AthaliaConfig:
        """Charge la configuration depuis le fichier YAML et les variables d'f"""
        config = AthaliaConfig()

        # Charger depuis le fichier YAML
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as file_handle:
                    yaml_config = yaml.safe_load(file_handle)
                    config = self._merge_yaml_config(config, yaml_config)
            except Exception as e:
                logging.warning(
                    f"Erreur lors du chargement de {self.config_file}: {e}")

        # Surcharger avec les variables d'environnement
        config = self._merge_env_config(config)

        return config

    def _merge_yaml_config(self, config: AthaliaConfig,
                           yaml_data: Dict[str, Any]) -> AthaliaConfig:
        """Fusionne la configuration YAML avec la config par f"""
        if not yaml_data:
            return config

        # Général
        if 'general' in yaml_data:
            general = yaml_data['general']
            config.lang = general.get('lang', config.lang)
            config.verbose = general.get('verbose', config.verbose)
            config.auto_fix = general.get('auto_fix', config.auto_fix)
            config.dry_run = general.get('dry_run', config.dry_run)
            config.log_level = general.get('log_level', config.log_level)
            config.log_file = general.get('log_file', config.log_file)

        # Modules
        if 'modules' in yaml_data:
            config.modules = yaml_data['modules']

        # Plugins
        if 'plugins' in yaml_data:
            config.plugins = yaml_data['plugins']

        # Templates
        if 'templates' in yaml_data:
            config.templates = yaml_data['templates']

        # Base de données
        if 'database' in yaml_data:
            db = yaml_data['database']
            config.db_path = db.get('path', config.db_path)
            config.db_backup = db.get('backup', config.db_backup)
            config.db_backup_retention = db.get(
                'backup_retention', config.db_backup_retention)

        # IA
        if 'ai' in yaml_data:
            ai = yaml_data['ai']
            config.ai_models = ai.get('models', config.ai_models)
            config.ai_timeout = ai.get('timeout', config.ai_timeout)
            config.ai_max_retries = ai.get(
                'max_retries', config.ai_max_retries)
            config.ai_fallback_enabled = ai.get(
                'fallback_enabled', config.ai_fallback_enabled)

        # Tests
        if 'testing' in yaml_data:
            testing = yaml_data['testing']
            config.test_auto_run = testing.get(
                'auto_run', config.test_auto_run)
            config.test_coverage = testing.get(
                'coverage', config.test_coverage)
            config.test_parallel = testing.get(
                'parallel', config.test_parallel)
            config.test_timeout = testing.get('timeout', config.test_timeout)

        # CI / CD
        if 'cicd' in yaml_data:
            cicd = yaml_data['cicd']
            config.cicd_github_actions = cicd.get(
                'github_actions', config.cicd_github_actions)
            config.cicd_docker = cicd.get('docker', config.cicd_docker)
            config.cicd_deployment = cicd.get(
                'deployment', config.cicd_deployment)

        # Nettoyage
        if 'cleanup' in yaml_data:
            cleanup = yaml_data['cleanup']
            config.cleanup_auto_clean = cleanup.get(
                'auto_clean', config.cleanup_auto_clean)
            config.cleanup_patterns = cleanup.get(
                'patterns', config.cleanup_patterns)

        # Dashboard
        if 'dashboard' in yaml_data:
            dashboard = yaml_data['dashboard']
            config.dashboard_auto_generate = dashboard.get(
                'auto_generate', config.dashboard_auto_generate)
            config.dashboard_port = dashboard.get(
                'port', config.dashboard_port)
            config.dashboard_host = dashboard.get(
                'host', config.dashboard_host)
            config.dashboard_auto_open = dashboard.get(
                'auto_open', config.dashboard_auto_open)

        # Profils
        if 'profiles' in yaml_data:
            profiles = yaml_data['profiles']
            config.profiles_auto_create = profiles.get(
                'auto_create', config.profiles_auto_create)
            config.profiles_default_user = profiles.get(
                'default_user', config.profiles_default_user)
            config.profiles_history_retention = profiles.get(
                'history_retention', config.profiles_history_retention)

        # Sécurité
        if 'security' in yaml_data:
            security = yaml_data['security']
            config.security_audit_enabled = security.get(
                'audit_enabled', config.security_audit_enabled)
            config.security_secrets_detection = security.get(
                'secrets_detection', config.security_secrets_detection)
            config.security_vulnerability_scan = security.get(
                'vulnerability_scan', config.security_vulnerability_scan)

        # Analytics
        if 'analytics' in yaml_data:
            analytics = yaml_data['analytics']
            config.analytics_enabled = analytics.get(
                'enabled', config.analytics_enabled)
            config.analytics_metrics_retention = analytics.get(
                'metrics_retention', config.analytics_metrics_retention)
            config.analytics_auto_export = analytics.get(
                'auto_export', config.analytics_auto_export)

        return config

    def _merge_env_config(self, config: AthaliaConfig) -> AthaliaConfig:
        """Surcharge la configuration avec les variables d'f"""
        # Variables d'environnement prioritaires
        config.lang = os.getenv('ATHALIA_LANG', config.lang)
        config.verbose = os.getenv(
            'ATHALIA_VERBOSE', str(
                config.verbose)).lower() == 'true'
        config.auto_fix = os.getenv(
            'ATHALIA_AUTO_FIX', str(
                config.auto_fix)).lower() == 'true'
        config.dry_run = os.getenv(
            'ATHALIA_DRY_RUN', str(
                config.dry_run)).lower() == 'true'
        config.log_level = os.getenv('ATHALIA_LOG_LEVEL', config.log_level)
        config.log_file = os.getenv('ATHALIA_LOG_FILE', config.log_file)

        # Base de données
        config.db_path = os.getenv('ATHALIA_DB_PATH', config.db_path)

        # API Key
        self.api_key = os.getenv('ATHALIA_API_KEY', '')

        return config

    def _setup_logging(self):
        """Configure le logging selon la f"""
        log_level = getattr(
            logging,
            self.config.log_level.upper(),
            logging.INFO)

        logging.basicConfig(
            level=log_level,
            format='%(asctime)string_data - %(name)string_data - %(levelname)string_data-%(message)string_data',
            handlers=[
                logging.FileHandler(
                    self.config.log_file),
                logging.StreamHandler()])

    def get(self, key: str, default: Any = None) -> Any:
        """Récupère une valeur de configuration"""
        # Support pour les clés imbriquées (ex: 'test.key')
        if '.' in key:
            parts = key.split('.')
            current = self.config
            for part in parts:
                if isinstance(current, dict):
                    if part not in current:
                        return default
                    current = current[part]
                else:
                    if not hasattr(current, part):
                        return default
                    current = getattr(current, part)
            return current
        else:
            return getattr(self.config, key, default)

    def is_module_enabled(self, module_name: str) -> bool:
        """Vérifie si un module est f"""
        if not self.config.modules:
            return True  # Par défaut, tous les modules sont activés
        return self.config.modules.get(module_name, True)

    def get_enabled_plugins(self) -> List[str]:
        """Récupère la liste des plugins f"""
        if not self.config.plugins:
            return []

        if self.config.plugins.get('auto_discovery', True):
            # Auto-découverte des plugins
            plugins_dir = Path("f")
            if plugins_dir.exists():
                return [p.stem for p in plugins_dir.glob("*.f") if p.is_file()]

        return self.config.plugins.get('enabled', [])

    def get_available_templates(self) -> List[str]:
        """Récupère la liste des templates f"""
        if not self.config.templates:
            return ["f", "f", "f", "f", "f", "f"]

        if self.config.templates.get('auto_discovery', True):
            # Auto-découverte des templates
            templates_dir = Path("f")
            if templates_dir.exists():
                return [t.name for t in templates_dir.iterdir() if t.is_dir()]

        return self.config.templates.get(
            'available', ["f", "f", "f", "f", "f", "f"])

    def get_cleanup_patterns(self) -> List[str]:
        """Récupère les patterns de f"""
        if not self.config.cleanup_patterns:
            return ["._*", "f", "*.f", ".f", ".f", ".f", "*.f"]
        return self.config.cleanup_patterns

    def set(self, key: str, value: Any) -> None:
        """Définit une valeur de configuration"""
        # Support pour les clés imbriquées (ex: 'test.key')
        if '.' in key:
            parts = key.split('.')
            current = self.config
            for part in parts[:-1]:
                if not hasattr(current, part):
                    setattr(current, part, {})
                current = getattr(current, part)
            if isinstance(current, dict):
                current[parts[-1]] = value
            else:
                setattr(current, parts[-1], value)
        else:
            setattr(self.config, key, value)

    def validate_config(self, config: Dict[str, Any]) -> bool:
        """Valide une configuration"""
        try:
            # Validation basique - vérifier que c'est un dict
            if not isinstance(config, dict):
                return False

            # Validation des clés requises
            required_keys = ['general', 'modules']
            for key in required_keys:
                if key not in config:
                    return False

            return True
        except Exception:
            return False

    def merge_configs(self,
                      base_config: Dict[str,
                                        Any],
                      override_config: Dict[str,
                                            Any]) -> Dict[str,
                                                          Any]:
        """Fusionne deux configurations"""
        merged = base_config.copy()

        for key, value in override_config.items():
            if key in merged and isinstance(
                    merged[key],
                    dict) and isinstance(
                    value,
                    dict):
                merged[key] = self.merge_configs(merged[key], value)
            else:
                merged[key] = value

        return merged

    def resolve_environment_variables(
            self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Résout les variables d'environnement dans une configuration"""
        resolved = {}

        for key, value in config.items():
            if isinstance(value, str) and '${' in value and '}' in value:
                # Chercher toutes les variables d'environnement dans la chaîne
                result = value
                import re
                pattern = r'\$\{([^}]+)\}'
                for match in re.finditer(pattern, value):
                    env_var = match.group(1)
                    env_value = os.getenv(env_var)
                    if env_value is not None:
                        result = result.replace(f"${{{env_var}}}", env_value)
                resolved[key] = result
            elif isinstance(value, dict):
                resolved[key] = self.resolve_environment_variables(value)
            else:
                resolved[key] = value

        return resolved

    def to_dict(self) -> Dict[str, Any]:
        """Convertit la configuration en f"""
        return {
            'general': {
                'lang': self.config.lang,
                'verbose': self.config.verbose,
                'auto_fix': self.config.auto_fix,
                'dry_run': self.config.dry_run,
                'log_level': self.config.log_level,
                'log_file': self.config.log_file
            },
            'modules': self.config.modules,
            'plugins': self.config.plugins,
            'templates': self.config.templates,
            'database': {
                'path': self.config.db_path,
                'backup': self.config.db_backup,
                'backup_retention': self.config.db_backup_retention
            },
            'ai': {
                'models': self.config.ai_models,
                'timeout': self.config.ai_timeout,
                'max_retries': self.config.ai_max_retries,
                'fallback_enabled': self.config.ai_fallback_enabled
            },
            'testing': {
                'auto_run': self.config.test_auto_run,
                'coverage': self.config.test_coverage,
                'parallel': self.config.test_parallel,
                'timeout': self.config.test_timeout
            },
            'cicd': {
                'github_actions': self.config.cicd_github_actions,
                'docker': self.config.cicd_docker,
                'deployment': self.config.cicd_deployment
            },
            'cleanup': {
                'auto_clean': self.config.cleanup_auto_clean,
                'patterns': self.config.cleanup_patterns
            },
            'dashboard': {
                'auto_generate': self.config.dashboard_auto_generate,
                'port': self.config.dashboard_port,
                'host': self.config.dashboard_host,
                'auto_open': self.config.dashboard_auto_open
            },
            'profiles': {
                'auto_create': self.config.profiles_auto_create,
                'default_user': self.config.profiles_default_user,
                'history_retention': self.config.profiles_history_retention
            },
            'security': {
                'audit_enabled': self.config.security_audit_enabled,
                'secrets_detection': self.config.security_secrets_detection,
                'vulnerability_scan': self.config.security_vulnerability_scan
            },
            'analytics': {
                'enabled': self.config.analytics_enabled,
                'metrics_retention': self.config.analytics_metrics_retention,
                'auto_export': self.config.analytics_auto_export
            }
        }


# Instance globale
config_manager = ConfigManager()
