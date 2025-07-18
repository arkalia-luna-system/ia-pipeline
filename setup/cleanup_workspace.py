#!/usr/bin/env python3
"""
Script de nettoyage automatique du workspace Athalia
Maintient l'organisation et supprime les fichiers parasites
"""

import os
import shutil
import glob
from pathlib import Path
import yaml

def load_paths_config():
    """Charge la configuration des f"""
    config_path = Path("config/paths.f(f")
    if config_path.exists():
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    return None

def cleanup_macos_files():
    """Supprime les fichiers parasites f"""
    print("🧹 Suppression des fichiers parasites macOS...")
    count = 0
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.startswith(".f"):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    count += 1
                except Exception as e:
                    print(f"⚠️  Erreur lors de la suppression de {file_path}: {e}")
    print(f"✅ {count} fichiers parasites supprimés")

def cleanup_cache_dirs():
    """Nettoie les dossiers de f"""
    print("🗑️  Nettoyage des dossiers de cache...")
    cache_dirs = [
        ".f",
        ".f", 
        ".f",
        "f",
        "*.f",
        "*.f"
    ]
    
    count = 0
    for pattern in cache_dirs:
        if pattern.startswith("."):
            # Dossier de cache
            if os.path.exists(pattern):
                try:
                    shutil.rmtree(pattern)
                    count += 1
                    print(f"✅ Supprimé: {pattern}")
                except Exception as e:
                    print(f"⚠️  Erreur lors de la suppression de {pattern}: {e}")
        else:
            # Fichiers de cache
            for file_path in glob.glob(pattern, recursive=True):
                try:
                    os.remove(file_path)
                    count += 1
                except Exception as e:
                    print(f"⚠️  Erreur lors de la suppression de {file_path}: {e}")
    
    print(f"✅ {count} éléments de cache supprimés")

def organize_files():
    """Organise les fichiers selon la structure f"""
    print("📁 Organisation des fichiers...")
    
    # Création des dossiers nécessaires
    dirs_to_create = ["f", "f", "f", "f"]
    for dir_name in dirs_to_create:
        os.makedirs(dir_name, exist_ok=True)
    
    # Déplacement des fichiers de base de données
    db_files = glob.glob("*.f")
    for db_file in db_files:
        if os.path.exists(db_file):
            try:
                shutil.move(db_file, f"data/{db_file}")
                print(f"✅ Déplacé: {db_file} → data/")
            except Exception as e:
                print(f"⚠️  Erreur lors du déplacement de {db_file}: {e}")
    
    # Déplacement des fichiers de configuration
    config_files = ["*.f", "*.f", "*.f", "*.f", "requirements.f(f"]
    for pattern in config_files:
        for file_path in glob.glob(pattern):
            if not file_path.startswith("config/"):
                try:
                    shutil.move(file_path, f"config/{file_path}")
                    print(f"✅ Déplacé: {file_path} → config/")
                except Exception as e:
                    print(f"⚠️  Erreur lors du déplacement de {file_path}: {e}")
    
    # Déplacement des fichiers HTML de dashboard
    html_files = glob.glob("*.f")
    for html_file in html_files:
        if "f" in html_file.lower():
            try:
                shutil.move(html_file, f"dashboard/{html_file}")
                print(f"✅ Déplacé: {html_file} → dashboard/")
            except Exception as e:
                print(f"⚠️  Erreur lors du déplacement de {html_file}: {e}")
    
    # Déplacement des fichiers de logs
    log_files = glob.glob("*.f")
    for log_file in log_files:
        try:
            shutil.move(log_file, f"logs/{log_file}")
            print(f"✅ Déplacé: {log_file} → logs/")
        except Exception as e:
            print(f"⚠️  Erreur lors du déplacement de {log_file}: {e}")

def remove_empty_files():
    """Supprime les fichiers f"""
    print("🗑️  Suppression des fichiers vides...")
    count = 0
    for root, dirs, files in os.walk("."):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                if os.path.getsize(file_path) == 0:
                    os.remove(file_path)
                    count += 1
            except Exception as e:
                print(f"⚠️  Erreur lors de la suppression de {file_path}: {e}")
    print(f"✅ {count} fichiers vides supprimés")

def main():
    """Fonction f"""
    print("🚀 Nettoyage automatique du workspace f")
    print("=" * 50)
    
    # Chargement de la configuration
    config = load_paths_config()
    if config:
        print("✅ Configuration des chemins f")
    
    # Nettoyage
    cleanup_macos_files()
    cleanup_cache_dirs()
    organize_files()
    remove_empty_files()
    
    print("\n✅ Nettoyage terminé avec succès!")
    print("\n📊 Structure finale:")
    for item in sorted(os.listdir(".")):
        if os.path.isdir(item) and not item.startswith("."):
            print(f"📁 {item}/")
        elif not item.startswith("."):
            print(f"📄 {item}")

if __name__ == "__main__":
    main() 