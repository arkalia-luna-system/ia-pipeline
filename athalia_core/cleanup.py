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
    """
    Supprime automatiquement les fichiers macOS parasites et temporaires dans tout le projet.
    Inclut les fichiers système macOS spécifiques comme .!44956!*.clean
    Retourne la liste des fichiers supprimés.
    """
    cleaned_files = []

    # Patterns de fichiers macOS à supprimer
    macos_patterns = [
        '._*',  # AppleDouble files
        '.DS_Store',  # Desktop Services Store
        'Thumbs.db',  # Windows thumbnail cache
        '.!*',
        # Fichiers temporaires macOS spécifiques (comme .!44956!*.clean)
        '*.tmp',  # Fichiers temporaires
        '*.bak',  # Fichiers de sauvegarde
        '*.log',  # Fichiers de log
        '*.clean',  # Fichiers de nettoyage temporaires
        '*.apdisk',  # Apple Partition Map
        '.Spotlight-V100',  # Spotlight index
        '.Trashes',  # Corbeille
        '.fseventsd',  # File System Events
        '.TemporaryItems',  # Items temporaires
        '._.DS_Store',  # AppleDouble DS_Store
        '.AppleDouble',  # Dossier AppleDouble
        '.LSOverride',  # Launch Services Override
    ]

    # Dossiers macOS à supprimer
    macos_dirs = [
        '.Spotlight-V100',
        '.Trashes',
        '.fseventsd',
        '.TemporaryItems',
        '.AppleDouble',
        '.LSOverride'
    ]

    for root, dirs, files in os.walk(directory):
        # Supprimer les dossiers macOS
        for dir_name in list(dirs):  # Copie de la liste pour modification
            if dir_name in macos_dirs:
                dir_path = os.path.join(root, dir_name)
                try:
                    shutil.rmtree(dir_path, ignore_errors=True)
                    cleaned_files.append(dir_path)
                    logging.info(f"Suppression dossier macOS: {dir_path}")
                except Exception as e:
                    logging.warning(
                        f"Impossible de supprimer le dossier {dir_path}: {e}")

        # Supprimer les fichiers macOS
        for file in files:
            should_delete = False

            # Vérifier les patterns
            for pattern in macos_patterns:
                if fnmatch.fnmatch(file, pattern):
                    should_delete = True
                    break

            # Vérifications spécifiques
            if (file.startswith('._') or
                file == '.DS_Store'
                or file == 'Thumbs.db'
                or file.startswith('.!')  # Fichiers comme .!44956!*.clean
                or file.endswith('.tmp')
                or file.endswith('.bak')
                or file.endswith('.log')
                or file.endswith('.clean')
                    or file.endswith('.apdisk')):
                should_delete = True

            if should_delete:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    cleaned_files.append(file_path)
                    logging.info(f"Suppression fichier macOS: {file_path}")
                except Exception as e:
                    logging.warning(
                        f"Impossible de supprimer {file_path}: {e}")

    logging.info(
        f"Nettoyage macOS terminé: {len(cleaned_files)} éléments supprimés")
    return cleaned_files
