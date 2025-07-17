#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from modules.profils_utilisateur_avances import GestionnaireProfils, ProfilUtilisateur
from pathlib import Path
import os
import sys
import shutil
import tempfile
import unittest

"""Tests pour le module de profils utilisateur avancés"""

# Ajout du chemin des modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

class TestProfilsUtilisateurAvances(unittest.TestCase):
    """Tests pour la gestion des profils utilisateur avancés"""

    def setUp(self):
        """Configuration des tests"""
        self.temp_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.temp_dir, "test_profils.db")

    def tearDown(self):
        """Nettoyage après les tests"""
        shutil.rmtree(self.temp_dir)

    def test_initialisation(self):
        """Test de l'initialisation du gestionnaire"""
        gestionnaire = GestionnaireProfils(self.db_path)
        self.assertIsNotNone(gestionnaire)
        self.assertEqual(gestionnaire.db_path, self.db_path)

    def test_creation_profil(self):
        """Test de création d'un profil utilisateur"""
        gestionnaire = GestionnaireProfils(self.db_path)
        profil = gestionnaire.creer_profil("Alice", "alice@example.com")
        self.assertIsNotNone(profil)
        self.assertEqual(profil.nom, "Alice")
        self.assertEqual(profil.email, "alice@example.com")

    def test_obtention_profil(self):
        """Test de récupération d'un profil utilisateur"""
        gestionnaire = GestionnaireProfils(self.db_path)
        gestionnaire.creer_profil("Bob", "bob@example.com")
        profil = gestionnaire.obtenir_profil("Bob")
        self.assertIsNotNone(profil)
        self.assertEqual(profil.nom, "Bob")

    def test_enregistrement_action(self):
        """Test de l'enregistrement d'une action utilisateur"""
        gestionnaire = GestionnaireProfils(self.db_path)
        gestionnaire.creer_profil("Charlie", "charlie@example.com")
        # Enregistrement d'une action
        gestionnaire.enregistrer_action("Charlie", "connexion", {"ip": "127.0.0.1"})
        # Vérification des statistiques
        stats = gestionnaire.obtenir_statistiques("Charlie")
        self.assertIn("connexion", stats)

    def test_generation_rapport(self):
        """Test de génération de rapport utilisateur"""
        gestionnaire = GestionnaireProfils(self.db_path)
        gestionnaire.creer_profil("Diane", "diane@example.com")
        rapport = gestionnaire.generer_rapport_profil("Diane")
        self.assertIsInstance(rapport, str)
        self.assertIn("Diane", rapport)

if __name__ == "__main__":
    unittest.main()