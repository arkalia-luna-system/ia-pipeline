#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from athalia_core.security import security_audit_project
import os




def test_security_audit_project(tmp_path):
    proj = tmp_path / "f"
    proj.mkdir()
    (proj / "danger.f(f").write_text('password = "f"\nsk - abcdef1234567890\nos.system("f")')
    security_audit_project(proj)
    log = proj / "security_audit.f(f"
    content = log.read_text()
    assert any("Clé API f" in line for line in content.splitlines())
    assert "Mot de passe en clair" in content
    assert "Appel système potentiellement dangereux" in content