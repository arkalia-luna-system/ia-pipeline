#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧹 Phase 3 Optimization - Athalia Project
Script sécurisé pour l'optimisation de maintenance

Fonctionnalités :
- Optimisation des performances
- Nettoyage intelligent des caches
- Analyse de l'espace disque
- Mode dry-run pour vérification
- Rapports détaillés
"""

import argparse
import logging
import os
import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/phase3_optimization.log", mode="a", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


def analyze_cache_sizes() -> Dict[str, float]:
    """Analyse la taille des caches"""
    cache_dirs = {
        ".mypy_cache": "Cache MyPy",
        ".pytest_cache": "Cache Pytest",
        "__pycache__": "Cache Python",
        ".ruff_cache": "Cache Ruff",
        ".coverage": "Cache Coverage",
    }

    cache_sizes = {}

    for cache_dir, description in cache_dirs.items():
        cache_path = Path(cache_dir)
        if cache_path.exists():
            total_size = 0
            file_count = 0

            for file_path in cache_path.rglob("*"):
                if file_path.is_file():
                    try:
                        total_size += file_path.stat().st_size
                        file_count += 1
                    except (OSError, PermissionError):
                        continue

            cache_sizes[description] = {
                "size_mb": total_size / 1024 / 1024,
                "files": file_count,
                "path": cache_dir
            }

    return cache_sizes


def clean_cache_intelligently(cache_sizes: Dict[str, float], dry_run: bool = True) -> Dict[str, int]:
    """Nettoie les caches de manière intelligente"""
    cleaned = {}

    for description, info in cache_sizes.items():
        size_mb = info["size_mb"]
        cache_path = Path(info["path"])

        # Nettoyer seulement si le cache est volumineux (> 50MB)
        if size_mb > 50:
            if dry_run:
                logger.info(f"🔍 [DRY-RUN] Nettoyage du cache {description}: {size_mb:.1f}MB")
            else:
                try:
                    if cache_path.is_dir():
                        shutil.rmtree(cache_path)
                    else:
                        cache_path.unlink()

                    logger.info(f"✅ Cache {description} nettoyé: {size_mb:.1f}MB libérés")
                    cleaned[description] = int(size_mb)
                except Exception as e:
                    logger.error(f"❌ Erreur nettoyage {description}: {e}")
        else:
            logger.info(f"ℹ️ Cache {description} conservé: {size_mb:.1f}MB (taille acceptable)")

    return cleaned


def analyze_disk_usage() -> Dict[str, float]:
    """Analyse l'utilisation du disque"""
    total_size = 0
    file_count = 0
    dir_count = 0

    for item in Path(".").rglob("*"):
        try:
            if item.is_file():
                total_size += item.stat().st_size
                file_count += 1
            elif item.is_dir():
                dir_count += 1
        except (OSError, PermissionError):
            continue

    return {
        "total_size_mb": total_size / 1024 / 1024,
        "file_count": file_count,
        "dir_count": dir_count
    }


def optimize_python_files(dry_run: bool = True) -> Dict[str, int]:
    """Optimise les fichiers Python"""
    optimized = {}

    # Supprimer les fichiers __pycache__ inutiles
    pycache_dirs = list(Path(".").rglob("__pycache__"))

    if dry_run:
        logger.info(f"🔍 [DRY-RUN] {len(pycache_dirs)} dossiers __pycache__ trouvés")
    else:
        for pycache_dir in pycache_dirs:
            try:
                shutil.rmtree(pycache_dir)
                logger.info(f"✅ Dossier supprimé: {pycache_dir}")
            except Exception as e:
                logger.error(f"❌ Erreur suppression {pycache_dir}: {e}")

        optimized["__pycache__"] = len(pycache_dirs)

    return optimized


def generate_optimization_report(
    cache_sizes: Dict[str, float],
    disk_usage: Dict[str, float],
    cleaned: Dict[str, int],
    optimized: Dict[str, int]
) -> str:
    """Génère un rapport d'optimisation"""
    report = []
    report.append("=" * 60)
    report.append("📊 RAPPORT D'OPTIMISATION PHASE 3")
    report.append("=" * 60)
    report.append(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("")

    # Cache analysis
    report.append("🗂️ ANALYSE DES CACHES:")
    total_cache_size = sum(info["size_mb"] for info in cache_sizes.values())
    report.append(f"   Taille totale des caches: {total_cache_size:.1f}MB")

    for description, info in cache_sizes.items():
        report.append(f"   - {description}: {info['size_mb']:.1f}MB ({info['files']} fichiers)")

    report.append("")

    # Disk usage
    report.append("💾 UTILISATION DISQUE:")
    report.append(f"   Taille totale du projet: {disk_usage['total_size_mb']:.1f}MB")
    report.append(f"   Nombre de fichiers: {disk_usage['file_count']}")
    report.append(f"   Nombre de dossiers: {disk_usage['dir_count']}")

    report.append("")

    # Optimization results
    if cleaned:
        report.append("🧹 OPTIMISATIONS RÉALISÉES:")
        for description, size_mb in cleaned.items():
            report.append(f"   - {description}: {size_mb}MB libérés")

    if optimized:
        report.append("⚡ OPTIMISATIONS PYTHON:")
        for item, count in optimized.items():
            report.append(f"   - {item}: {count} éléments traités")

    report.append("")
    report.append("=" * 60)

    return "\n".join(report)


def main():
    """Fonction principale"""
    parser = argparse.ArgumentParser(description="Optimisation Phase 3 - Athalia Project")
    parser.add_argument("--dry-run", action="store_true", default=True,
                        help="Mode vérification (par défaut)")
    parser.add_argument("--execute", action="store_true",
                        help="Exécuter réellement les optimisations")
    parser.add_argument("--root", default=".", help="Répertoire racine")

    args = parser.parse_args()

    if args.execute:
        args.dry_run = False

    logger.info(f"🚀 Démarrage de l'optimisation Phase 3 (Dry-run: {args.dry_run})")
    start_time = datetime.now()

    # Analyse des caches
    logger.info("🔍 Analyse des caches...")
    cache_sizes = analyze_cache_sizes()

    # Analyse de l'espace disque
    logger.info("💾 Analyse de l'espace disque...")
    disk_usage = analyze_disk_usage()

    # Nettoyage intelligent des caches
    logger.info("🧹 Nettoyage intelligent des caches...")
    cleaned = clean_cache_intelligently(cache_sizes, args.dry_run)

    # Optimisation des fichiers Python
    logger.info("⚡ Optimisation des fichiers Python...")
    optimized = optimize_python_files(args.dry_run)

    # Génération du rapport
    report = generate_optimization_report(cache_sizes, disk_usage, cleaned, optimized)

    # Affichage du rapport
    print(report)

    # Sauvegarde du rapport
    report_file = f"logs/phase3_optimization_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    os.makedirs("logs", exist_ok=True)

    with open(report_file, "w", encoding="utf-8") as f:
        f.write(report)

    end_time = datetime.now()
    duration = end_time - start_time
    logger.info(f"✅ Optimisation Phase 3 terminée en {duration}")
    logger.info(f"Rapport sauvegardé: {report_file}")


if __name__ == "__main__":
    main()
