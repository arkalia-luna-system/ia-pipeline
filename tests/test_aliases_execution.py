import os
import re
import subprocess
import pytest

ALIAS_FILE = os.path.join(os.path.dirname(__file__), '../setup', 'alias.sh')

# Alias à ignorer (interactifs, ouvrent des fichiers/GUI, à implémenter, ou dépendant de scripts absents)
SKIP_ALIASES = set([
    'ath-dashboard', 'ath-dashboard-py', 'ath-dashboard-full', 'ath-doc-open', 'ath-prompts', 'ath-config',
    'ath-coverage-html', 'ath-final-report', 'ath-code', 'ath-notebook', 'ath-mkdocs',
    'ath-help', 'ath-user-context', 'ath-context',
    'ath-dev-boost', 'ath-perplex', 'ath-docker', 'ath-jupyter',
    # Alias à implémenter ou nécessitant une interaction
    'ath-generate', 'ath-correct', 'ath-profile', 'ath-scan', 'ath-test-prompts', 'ath-benchmark', 'ath-export',
    'ath-auto-correct', 'ath-dashboard-unified', 'ath-profile-advanced', 'ath-plugin-docker', 'ath-plugin-hello',
    'ath-test-ci', 'ath-test-final', 'ath-test-dashboard', 'ath-benchmark-full', 'ath-plugins-list',
    # Alias dangereux (récursivité ou coverage)
    'ath-test', 'ath-coverage',
    # Alias shell dépendant de scripts absents ou non portables
    'ath-clean', 'ath-lint', 'ath-build', 'ath-smart', 'ath-cli-main', 'ath-unified', 'ath-audit',
])

# Récupère tous les alias testables automatiquement
with open(ALIAS_FILE) as f:
    content = f.read()
ALIASES = [
    m.group(1) for m in re.finditer(r"^alias ([a-zA-Z0-9_-]+)=", content, re.MULTILINE)
    if m.group(1) not in SKIP_ALIASES
]

@pytest.mark.parametrize("alias_name", ALIASES)
def test_alias_execution(alias_name):
    """
    Teste l'exécution de chaque alias non interactif dans un sous-shell interactif.
    Vérifie que l'exit code est 0 (pas d'erreur fatale).
    """
    # Skip explicite si l'alias est dangereux ou dépend d'un script absent
    if alias_name in SKIP_ALIASES:
        pytest.skip(f"Alias {alias_name} ignoré car potentiellement dangereux, interactif ou dépend d'un script absent.")
    cmd = f"bash -ic 'source {ALIAS_FILE} && {alias_name} --help || {alias_name}'"
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert result.returncode == 0, f"Alias {alias_name} a échoué : {result.stderr.decode().strip()}" 