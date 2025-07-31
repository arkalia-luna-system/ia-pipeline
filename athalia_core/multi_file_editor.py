#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module d'édition/correction multi-fichiers pour Athalia/Arkalia.
Permet d'appliquer des corrections/refactoring sur plusieurs fichiers en une seule commande,
avec logs et rollback.
"""
import logging
import os
import shutil
from typing import Any, Callable, Dict, List, Tuple


logger = logging.getLogger(__name__)


class MultiFileEditor:
    def __init__(self, backup_dir: str = ".multi_file_backups"):
        self.backup_dir = backup_dir
        os.makedirs(self.backup_dir, exist_ok=True)
        self.logs: List[str] = []
        self.rollback_files: List[Tuple[str, str]] = []

    def backup_file(self, file_path: str):
        backup_path = os.path.join(self.backup_dir, os.path.basename(file_path))
        shutil.copy2(file_path, backup_path)
        self.rollback_files.append((file_path, backup_path))
        self.logs.append(f"Backup: {file_path} -> {backup_path}")

    def apply_corrections(
        self, files: List[str], correction_fn: Callable[[str], str]
    ) -> Dict[str, Any]:
        """
            Applique la fonction de correction à chaque fichier.
        :param files: Liste des chemins de fichiers à corriger
        :param correction_fn: Fonction qui prend le contenu du fichier et
                                 retourne le contenu corrigé
        :return: Dictionnaire de résultats (succès, erreurs, logs)
        """
        results: Dict[str, Any] = {"success": [], "errors": [], "logs": []}
        for file_path in files:
            try:
                self.backup_file(file_path)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                corrected = correction_fn(content)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(corrected)
                self.logs.append(f"Corrigé: {file_path}")
                results["success"].append(file_path)
            except Exception as e:
                self.logs.append(f"Erreur sur {file_path}: {e}")
                results["errors"].append((file_path, str(e)))
        results["logs"] = self.logs.copy()
        return results

    def rollback(self):
        """Restaure tous les fichiers depuis les backups."""
        for file_path, backup_path in self.rollback_files:
            try:
                shutil.copy2(backup_path, file_path)
                self.logs.append(f"Rollback: {backup_path} -> {file_path}")
            except Exception as e:
                self.logs.append(f"Erreur rollback {file_path}: {e}")
        return self.logs.copy()


# Exemple d'utilisation (à supprimer ou commenter en prod)
if __name__ == "__main__":

    def dummy_correction(content):
        return content.replace("foo", "bar")

    mfe = MultiFileEditor()
    result = mfe.apply_corrections(["test1.py", "test2.py"], dummy_correction)
    print(result)
    # mfe.rollback()
