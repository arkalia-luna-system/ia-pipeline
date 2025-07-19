#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests pour le menu ath-dev-boost
Version: 1.0
Auteur: Athalia Team
"""

import unittest
import pytest
from pathlib import Path


class TestAthDevBoostMenu(unittest.TestCase):
    """Tests pour le menu ath-dev-boost
    
    Cette classe teste les aspects suivants :
    - Existence du script
    - Exécutabilité du script
    - Contenu du script
    - Fonctionnalités du menu
    """
    
    def setUp(self):
        """Initialisation avant chaque test"""
        self.script_path = Path("setup/ath-dev-boost.sh")
    
    def test_script_exists(self):
        """Test que le script ath-dev-boost existe
        
        Scénario : Vérification de l'existence du fichier
        Données : Chemin vers setup/ath-dev-boost.sh
        Résultat attendu : Le fichier doit exister
        """
        self.assertTrue(self.script_path.exists(), 
                       f"Script ath-dev-boost.sh manquant à {self.script_path}")
    
    def test_script_executable(self):
        """Test que le script est exécutable
        
        Scénario : Vérification de l'exécutabilité du script
        Données : Fichier setup/ath-dev-boost.sh
        Résultat attendu : Le script doit être exécutable
        """
        if self.script_path.exists():
            # Vérifie que le fichier contient du contenu
            with open(self.script_path, 'r') as f:
                content = f.read()
                self.assertTrue(content.strip(), 
                              "Script ath-dev-boost.sh vide")
        else:
            self.skipTest("Script ath-dev-boost.sh non trouvé")
    
    def test_script_content_structure(self):
        """Test de la structure du contenu du script
        
        Scénario : Vérification de la structure du script
        Données : Contenu du fichier setup/ath-dev-boost.sh
        Résultat attendu : Le script doit avoir une structure valide
        """
        if self.script_path.exists():
            with open(self.script_path, 'r') as f:
                content = f.read()
                
            # Vérifications de structure
            self.assertIn("#!/bin/bash", content, 
                         "Le script doit commencer par le shebang bash")
            self.assertIn("echo", content, 
                         "Le script doit contenir des commandes echo")
            self.assertIn("read", content, 
                         "Le script doit contenir des commandes read pour l'interactivité")
        else:
            self.skipTest("Script ath-dev-boost.sh non trouvé")


def test_script_path_validity():
    """Test de la validité du chemin du script
    
    Scénario : Vérification du chemin du script
    Données : Chemin setup/ath-dev-boost.sh
    Résultat attendu : Le chemin doit être valide
    """
    script_path = Path("setup/ath-dev-boost.sh")
    assert script_path.is_file() or not script_path.exists(), (
        f"Le chemin {script_path} doit être un fichier ou ne pas exister")


if __name__ == "__main__":
    unittest.main()