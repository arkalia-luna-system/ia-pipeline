#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

import subprocess


def test_prompts_presence():
    prompts = [
        "dev_debug.yaml", "ux_fun_boost.md", "design_review.md", "test_strategy.md", "code_refactor.yaml", "custom_prompts.yaml", "security_audit.md"
    ]
    for p in prompts:
        path = os.path.join(os.path.dirname(__file__), '../prompts', p)
        assert os.path.exists(path), f"Prompt manquant : {p} ({path})"

def test_ath_dev_boost():
    script = os.path.join(os.path.dirname(__file__), '../setup', 'ath-dev-boost.sh')
    assert os.path.exists(script), f"ath-dev-boost.sh manquant ({script})"
    result = subprocess.run(["bash", script], input="1\n", capture_output=True, text=True)
    assert "Choisis un booster IA" in result.stdout, "ath-dev-boost.sh ne fonctionne pas"

def test_ath_context_prompt():
    script = os.path.join(os.path.dirname(__file__), '../agents', 'ath_context_prompt.py')
    assert os.path.exists(script), f"ath_context_prompt.py manquant ({script})"
    testfile = os.path.join(os.path.dirname(__file__), '../prompts', 'dev_debug.yaml')
    result = subprocess.run(["python3", script, testfile], capture_output=True, text=True)
    assert "prompt" in result.stdout.lower() or "ia" in result.stdout.lower(), "ath_context_prompt.py ne fonctionne pas"

def test_alias_sh():
    alias_file = os.path.join(os.path.dirname(__file__), '../setup', 'alias.sh')
    assert os.path.exists(alias_file), f"alias.sh manquant ({alias_file})"
    with open(alias_file) as file_handle:
        content = file_handle.read()
    aliases = [
        "ath-dev-boost",
        "ath-chat",
        "ath-clean",
        "ath-perplex",
        "ath-test",
        "ath-lint",
        "ath-build",
        "ath-new",
        "ath-smart"
    ]
    for alias in aliases:
        assert alias in content, f"Alias manquant : {alias}"
