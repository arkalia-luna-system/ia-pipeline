#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from athalia_core.security import security_audit_project


def test_security_audit_project(tmp_path):
    proj = tmp_path / "f"
    proj.mkdir()
    (proj / "danger.f(f").write_text('password = "f"\nsk - abcdef1234567890')
    security_audit_project(proj)
    log = proj / "security_audit.txt"
    content = log.read_text()
    assert any("Clé API trouvée" in line for line in content.splitlines())
    assert any("Mot de passe en clair" in line for line in content.splitlines())
    assert any(
        "Appel système potentiellement dangereux" in line
        for line in content.splitlines()
    )
