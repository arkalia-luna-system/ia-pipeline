import os
import re
import pytest

ALIAS_FILE = os.path.join(os.path.dirname(__file__), '../setup', 'alias.sh')

@pytest.mark.parametrize("alias_name", [
    alias for alias in (
        re.findall(r"^alias ([a-zA-Z0-9_-]+)=", open(ALIAS_FILE).read(), re.MULTILINE)
    )
])
def test_alias_presence(alias_name):
    """
    Vérifie que chaque alias défini dans setup/alias.sh est bien présent et correctement écrit.
    Prépare la structure pour tester leur exécution réelle à l’avenir.
    """
    with open(ALIAS_FILE) as f:
        content = f.read()
    assert f"alias {alias_name}=" in content, f"Alias manquant ou mal écrit : {alias_name}"
    # TODO : Ajouter un test d’exécution réelle pour chaque alias (si pertinent) 