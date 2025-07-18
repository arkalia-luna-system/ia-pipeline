import os
import re
import subprocess
import pytest
from pathlib import Path

# Configuration
ALIAS_FILE = Path(__file__).parent.parent / 'setup' / 'alias-unified.sh'
ATHALIA_ROOT = Path(__file__).parent.parent

class TestAliasesUnified:
    """Tests complets pour le système d'alias unifié Athalia"""

    def test_alias_file_exists(self):
        """Vérifie que le fichier d'alias unifié existe"""
        assert ALIAS_FILE.exists(), f"Fichier d'alias manquant : {ALIAS_FILE}"
        assert ALIAS_FILE.is_file(), f"Le fichier {ALIAS_FILE} n'est pas un fichier"

    def test_alias_file_readable(self):
        """Vérifie que le fichier d'alias est lisible"""
        with open(ALIAS_FILE, 'r') as f:
            content = f.read()
        assert len(content) > 0, "Le fichier d'alias est vide"
        assert "ATHALIA_ROOT" in content, "Variable ATHALIA_ROOT manquante"

    def test_all_aliases_defined(self):
        """Vérifie que tous les alias sont correctement définis"""
        with open(ALIAS_FILE, 'r') as f:
            content = f.read()
        
        # Trouve tous les alias définis
        alias_pattern = r'^alias ([a-zA-Z0-9_-]+)='
        aliases = re.findall(alias_pattern, content, re.MULTILINE)
        
        assert len(aliases) > 0, "Aucun alias trouvé dans le fichier"
        
        # Vérifie que chaque alias a une définition
        for alias in aliases:
            assert f"alias {alias}=" in content, f"Alias {alias} mal défini"

    def test_git_aliases_present(self):
        """Vérifie la présence des alias Git essentiels"""
        git_aliases = ['gb', 'gba', 'gco', 'gs', 'gl', 'ga', 'gc', 'gp', 'gpl']
        
        with open(ALIAS_FILE, 'r') as f:
            content = f.read()
        
        for alias in git_aliases:
            assert f"alias {alias}=" in content, f"Alias Git manquant : {alias}"

    def test_athalia_core_aliases_present(self):
        """Vérifie la présence des alias Athalia essentiels"""
        athalia_aliases = [
            'ath-test', 'ath-lint', 'ath-clean', 'ath-dashboard', 
            'ath-cli', 'ath-smart', 'ath-audit'
        ]
        
        with open(ALIAS_FILE, 'r') as f:
            content = f.read()
        
        for alias in athalia_aliases:
            assert f"alias {alias}=" in content, f"Alias Athalia manquant : {alias}"

    def test_athalia_functions_present(self):
        """Vérifie la présence des fonctions Athalia essentielles"""
        athalia_functions = ['ath-help', 'ath-status', 'ath-user-context']
        
        with open(ALIAS_FILE, 'r') as f:
            content = f.read()
        
        for func in athalia_functions:
            assert f"function {func}()" in content, f"Fonction Athalia manquante : {func}"

    def test_workflow_aliases_present(self):
        """Vérifie la présence des alias de workflow"""
        workflow_aliases = ['ath-start', 'ath-feature', 'ath-commit', 'ath-push', 'ath-merge']
        
        with open(ALIAS_FILE, 'r') as f:
            content = f.read()
        
        for alias in workflow_aliases:
            assert f"alias {alias}=" in content, f"Alias workflow manquant : {alias}"

    def test_functions_present(self):
        """Vérifie la présence des fonctions d'aide"""
        functions = ['ath-help', 'ath-status', 'ath-user-context']
        
        with open(ALIAS_FILE, 'r') as f:
            content = f.read()
        
        for func in functions:
            assert f"function {func}()" in content, f"Fonction manquante : {func}"

    def test_autocompletion_configured(self):
        """Vérifie que l'auto-complétion est configurée"""
        with open(ALIAS_FILE, 'r') as f:
            content = f.read()
        
        assert "compctl -K _athalia_aliases ath-" in content, "Auto-complétion ZSH manquante"
        assert "complete -A alias ath-" in content, "Auto-complétion Bash manquante"

    def test_athalia_root_exported(self):
        """Vérifie que ATHALIA_ROOT est exporté"""
        with open(ALIAS_FILE, 'r') as f:
            content = f.read()
        
        assert "export ATHALIA_ROOT" in content, "ATHALIA_ROOT n'est pas exporté"

    def test_placeholder_aliases_defined(self):
        """Vérifie que les alias à implémenter sont définis"""
        placeholder_aliases = [
            'ath-generate', 'ath-correct', 'ath-profile', 'ath-scan',
            'ath-test-prompts', 'ath-export', 'ath-mkdocs'
        ]
        
        with open(ALIAS_FILE, 'r') as f:
            content = f.read()
        
        for alias in placeholder_aliases:
            assert f"alias {alias}=" in content, f"Placeholder manquant : {alias}"
            assert "Fonctionnalité à implémenter" in content, f"Message placeholder manquant pour {alias}"

    def test_plugin_aliases_configured(self):
        """Vérifie la configuration des alias de plugins"""
        with open(ALIAS_FILE, 'r') as f:
            content = f.read()
        
        assert "ath-plugin-docker" in content, "Alias plugin Docker manquant"
        assert "ath-plugin-hello" in content, "Alias plugin Hello manquant"
        assert "ath-plugins-list" in content, "Alias liste plugins manquant"

    def test_test_aliases_specific(self):
        """Vérifie les alias de tests spécifiques"""
        test_aliases = [
            'ath-test-unit', 'ath-test-integration', 'ath-test-performance',
            'ath-coverage', 'ath-coverage-html'
        ]
        
        with open(ALIAS_FILE, 'r') as f:
            content = f.read()
        
        for alias in test_aliases:
            assert f"alias {alias}=" in content, f"Alias test manquant : {alias}"

    def test_docker_aliases_present(self):
        """Vérifie les alias Docker"""
        docker_aliases = ['ath-docker', 'ath-docker-build', 'ath-docker-down']
        
        with open(ALIAS_FILE, 'r') as f:
            content = f.read()
        
        for alias in docker_aliases:
            assert f"alias {alias}=" in content, f"Alias Docker manquant : {alias}"

    def test_benchmark_aliases_present(self):
        """Vérifie les alias de benchmark"""
        benchmark_aliases = ['ath-benchmark', 'ath-benchmark-full']
        
        with open(ALIAS_FILE, 'r') as f:
            content = f.read()
        
        for alias in benchmark_aliases:
            assert f"alias {alias}=" in content, f"Alias benchmark manquant : {alias}"

    def test_documentation_aliases_present(self):
        """Vérifie les alias de documentation"""
        doc_aliases = ['ath-doc', 'ath-doc-open', 'ath-doc-api', 'ath-doc-guide']
        
        with open(ALIAS_FILE, 'r') as f:
            content = f.read()
        
        for alias in doc_aliases:
            assert f"alias {alias}=" in content, f"Alias documentation manquant : {alias}"

    def test_security_aliases_present(self):
        """Vérifie les alias de sécurité"""
        security_aliases = ['ath-audit', 'ath-audit-intelligent', 'ath-security']
        
        with open(ALIAS_FILE, 'r') as f:
            content = f.read()
        
        for alias in security_aliases:
            assert f"alias {alias}=" in content, f"Alias sécurité manquant : {alias}"

    def test_development_aliases_present(self):
        """Vérifie les alias de développement"""
        dev_aliases = ['ath-dev-boost', 'ath-perplex', 'ath-jupyter', 'ath-notebook']
        
        with open(ALIAS_FILE, 'r') as f:
            content = f.read()
        
        for alias in dev_aliases:
            assert f"alias {alias}=" in content, f"Alias développement manquant : {alias}"

    def test_configuration_aliases_present(self):
        """Vérifie les alias de configuration"""
        config_aliases = ['ath-config', 'ath-prompts', 'ath-final-report']
        
        with open(ALIAS_FILE, 'r') as f:
            content = f.read()
        
        for alias in config_aliases:
            assert f"alias {alias}=" in content, f"Alias configuration manquant : {alias}"

    def test_modules_aliases_present(self):
        """Vérifie les alias de modules avancés"""
        module_aliases = ['ath-auto-correct', 'ath-dashboard-unified', 'ath-profile-advanced']
        
        with open(ALIAS_FILE, 'r') as f:
            content = f.read()
        
        for alias in module_aliases:
            assert f"alias {alias}=" in content, f"Alias module manquant : {alias}"

    def test_syntax_validity(self):
        """Vérifie la validité syntaxique du fichier bash"""
        try:
            result = subprocess.run(
                ['bash', '-n', str(ALIAS_FILE)],
                capture_output=True,
                text=True
            )
            assert result.returncode == 0, f"Erreur de syntaxe bash : {result.stderr}"
        except FileNotFoundError:
            pytest.skip("Bash non disponible pour le test de syntaxe")

    def test_help_function_content(self):
        """Vérifie le contenu de la fonction d'aide"""
        with open(ALIAS_FILE, 'r') as f:
            content = f.read()
        
        # Trouve la fonction ath-help
        help_pattern = r'function ath-help\(\) \{.*?\}'
        help_match = re.search(help_pattern, content, re.DOTALL)
        
        assert help_match, "Fonction ath-help non trouvée"
        
        help_content = help_match.group(0)
        
        # Vérifie les sections importantes
        sections = ['GIT WORKFLOW', 'TESTS & QUALITÉ', 'CORE FEATURES', 'DÉVELOPPEMENT']
        for section in sections:
            assert section in help_content, f"Section {section} manquante dans ath-help"

    def test_status_function_content(self):
        """Vérifie le contenu de la fonction de statut"""
        with open(ALIAS_FILE, 'r') as f:
            content = f.read()
        
        # Trouve la fonction ath-status
        status_pattern = r'function ath-status\(\) \{.*?\}'
        status_match = re.search(status_pattern, content, re.DOTALL)
        
        assert status_match, "Fonction ath-status non trouvée"
        
        status_content = status_match.group(0)
        
        # Vérifie les informations importantes
        info_items = ['ATHALIA_ROOT', 'git branch', 'tests/', 'plugins/', 'docs/']
        for item in info_items:
            assert item in status_content, f"Information {item} manquante dans ath-status"

    def test_initialization_message(self):
        """Vérifie le message d'initialisation"""
        with open(ALIAS_FILE, 'r') as f:
            content = f.read()
        
        # Vérifie les messages de bienvenue
        welcome_messages = [
            "Alias Athalia/Arkalia unifiés chargés",
            "ath-help",
            "ath-status"
        ]
        
        for message in welcome_messages:
            assert message in content, f"Message de bienvenue manquant : {message}"

if __name__ == "__main__":
    pytest.main([__file__]) 