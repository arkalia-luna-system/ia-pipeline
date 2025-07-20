#!/usr/bin/env python3
"""
projet_ia_exemple - Projet généré par Athalia
"""

import sys
import os

class ProjetIaExemple:
    def __init__(self):
        self.name = "projet_ia_exemple"
        self.version = "1.0.0"
    
    def run(self):
        """Exécute la logique principale"""
        print(f"🚀 projet_ia_exemple démarré")
        print(f"Version: {self.version}")
        return True
    
    def get_info(self):
        """Retourne les informations du projet"""
        return {
            "name": self.name,
            "version": self.version,
            "description": "Projet IA généré automatiquement"
        }

def main():
    """Point d'entrée principal"""
    app = ProjetIaExemple()
    return app.run()

def run():
    """Exécute l'application"""
    return main()

if __name__ == "__main__":
    main()
