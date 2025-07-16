import os
from athalia_core.security import security_audit_project

def test_security_audit_project(tmp_path):
    proj = tmp_path / "proj"
    proj.mkdir()
    (proj / "danger.py").write_text('password = "1234"\nsk-abcdef1234567890\nos.system("ls")')
    security_audit_project(proj)
    log = proj / "security_audit.log"
    content = log.read_text()
    assert "Clé API potentielle" in content
    assert "Mot de passe en dur" in content
    assert "Appel shell potentiellement risqué" in content 