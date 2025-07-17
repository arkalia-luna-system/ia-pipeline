#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from athalia_core.i18n import get_translation


def test_get_translation_fr():
    tr = get_translation('fr')
    assert tr["error"].startswith("Erreur")
    assert tr["success"].startswith("Succès")

def test_get_translation_en():
    tr = get_translation('en')
    assert tr["error"].startswith("Error")
    assert tr["success"].startswith("Success")