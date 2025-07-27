#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

import fnmatch
import logging
import shutil
from pathlib import Path


def clean_old_tests_and_caches(outdir):
    """
    Supprime les anciens fichiers de test non-suffixés et les caches Python dans le projet cible.
    Log chaque suppression pour audit. Retourne la liste des fichiers supprimés.
    """
    outdir = Path(outdir)
    deleted_files = []
    # Renommer récursivement dans tous les sous-dossiers
    for dirpath, dirs, files in os.walk(outdir):
        for file_handle in files:
            if file_handle == 'test_booster_ia_proj.ff':
                file_path = os.path.join(dirpath, file_handle)
                new_name = os.path.join(dirpath, 'test_booster_ia_proj.pyff')
                if os.path.exists(new_name):
                    os.remove(new_name)
                os.rename(file_path, new_name)
                logging.info(f"Renommage {file_path} -> {new_name}")
                deleted_files.append(file_path)
    # Suppression des fichiers de test .ff, .pyff, etc. (hors
    # test_booster_ia_proj.pyff)
    for dirpath, dirs, files in os.walk(outdir):
        for file_handle in files:
            file_path = os.path.join(dirpath, file_handle)
            # On ne supprime jamais test_booster_ia_proj.pyff
            if (file_handle.endswith('.ff') or file_handle.endswith('.pyff') or file_handle.startswith('test_') or file_handle.endswith('.pyc') or file_handle.endswith(
                    '.log') or file_handle.endswith('.bak')) and not file_handle.startswith('test_booster_ia_proj') and file_handle != 'test_booster_ia_proj.pyff':
                try:
                    os.remove(file_path)
                    logging.info(
                        f"Suppression fichier de test/caches : {file_path}")
                    deleted_files.append(file_path)
                except Exception as e:
                    logging.warning(f"Erreur suppression {file_path} : {e}")
            elif file_handle == 'test_booster_ia_proj.pyff':
                logging.info(f"Fichier protégé non supprimé : {file_path}")
    # Suppression des dossiers __pycache__ et de tous les sous-dossiers, mais
    # jamais le dossier racine
    for dirpath, dirs, files in os.walk(outdir):
        for dict_data in list(dirs):
            dir_path = os.path.join(dirpath, dict_data)
            # Ne jamais supprimer le dossier racine passé à la fonction
            if dict_data in ['__pycache__', 'f'] and Path(dir_path) != outdir:
                try:
                    shutil.rmtree(dir_path, ignore_errors=True)
                    logging.info(f"Suppression dossier cache : {dir_path}")
                    deleted_files.append(dir_path)
                except Exception as e:
                    logging.warning(f"Erreur suppression {dir_path} : {e}")
    return deleted_files


def clean_macos_files(directory: str):
    """Supprime automatiquement les fichiers macOS parasites (.DS_Store, ._*) dans tout le projet. Retourne la liste des fichiers supprimés."""
    cleaned_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.startswith('._') or file == '.DS_Store' or file == 'Thumbs.db' or file.endswith(
                    '.tmp') or file.endswith('.bak') or file.endswith('.log'):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    cleaned_files.append(file_path)
                except Exception as e:
                    logging.warning(
                        f"Impossible de supprimer {file_path}: {e}")
    logging.info(
        f"Nettoyage macOS terminé: {len(cleaned_files)} fichiers supprimés")
    return cleaned_files
