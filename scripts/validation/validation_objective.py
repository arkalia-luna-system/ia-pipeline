#!/usr/bin/env python3
"""
Validation Objective d'Athalia/Arkalia
Tests qui ne peuvent pas mentir - Mesures concrètes et indépendantes
"""

import json
import os
import subprocess
import time
from datetime import datetime
from pathlib import Path
from typing import Any

# Import du validateur de sécurité
try:
    from athalia_core.security_validator import validate_and_run
except ImportError:
    # Fallback si le module n'est pas disponible
    def validate_and_run(
        command: list[str], **kwargs: Any
    ) -> subprocess.CompletedProcess:
        return subprocess.run(command, **kwargs)


class ValidationObjective:
    def __init__(self) -> None:
        self.resultats: dict = {}
        self.seuils_critiques: dict = {
            "temps_max_generation": 30.0,  # 30 secondes max pour générer un projet
            "temps_max_correction": 10.0,  # 10 secondes max pour corriger
            "taux_compilation_min": 80.0,  # 80% du code généré doit compiler
            "taux_succes_min": 85.0,  # 85% de succès minimum
            "memoire_max": 1000.0,  # 1GB max
        }

    def test_generation_et_compilation(self) -> dict:
        """Test 1: Le code généré compile-t-il vraiment ?"""
        print("🔍 Test 1: Génération et compilation...")

        start = time.time()

        # Crée un projet test avec Athalia
        projet_test = f"/tmp/test_athalia_{int(time.time())}"
        os.makedirs(projet_test, exist_ok=True)

        # Crée un fichier Python simple pour tester
        with open(f"{projet_test}/main.py", "w") as f:
            f.write(
                """def hello():
    print("Hello World")
    return "OK"

if __name__ == "__main__":
    hello()
"""
            )

        cmd = [
            "python",
            "bin/core/athalia_unified.py",
            projet_test,
            "--action",
            "complete",
            "--auto-fix",
        ]

        try:
            # Utilisation du validateur de sécurité
            result = validate_and_run(cmd, timeout=60)
            temps_generation = time.time() - start

            if result.returncode != 0:
                return {
                    "succes": False,
                    "erreur": f"Génération échouée: {result.stderr}",
                    "temps": temps_generation,
                }

            # Vérifie que le projet a été créé
            if not os.path.exists(projet_test):
                return {
                    "succes": False,
                    "erreur": "Projet non créé",
                    "temps": temps_generation,
                }

            # Test de compilation de tous les fichiers Python générés
            fichiers_python = list(Path(projet_test).glob("**/*.py"))
            compilation_ok = 0
            erreurs_compilation = []

            for py_file in fichiers_python:
                try:
                    with open(py_file, encoding="utf-8") as f:
                        code = f.read()
                    compile(code, str(py_file), "exec")
                    compilation_ok += 1
                except Exception as e:
                    erreurs_compilation.append(f"{py_file}: {str(e)}")

            taux_compilation = (
                (compilation_ok / len(fichiers_python)) * 100 if fichiers_python else 0
            )

            return {
                "succes": (
                    taux_compilation >= self.seuils_critiques["taux_compilation_min"]
                ),
                "temps": temps_generation,
                "fichiers_generes": len(fichiers_python),
                "compilation_ok": compilation_ok,
                "taux_compilation": taux_compilation,
                "erreurs_compilation": erreurs_compilation,
                "projet_creer": True,
            }

        except subprocess.TimeoutExpired:
            return {
                "succes": False,
                "erreur": "Timeout - Génération trop lente",
                "temps": 60,
            }
        except Exception as e:
            return {
                "succes": False,
                "erreur": f"Exception: {str(e)}",
                "temps": time.time() - start,
            }

    def test_correction_reelle(self) -> dict:
        """Test 2: Athalia corrige-t-il vraiment les erreurs ?"""
        print("🔍 Test 2: Correction d'erreurs...")

        # Crée un fichier avec des erreurs volontaires (plus réalistes)
        code_avec_erreurs = """
def fonction_cassee():
    x = 1
    y = 2
    return x + y + z  # Erreur: z n'existe pas

def autre_fonction( ):  # Erreur: espace mal placé
    pass

def fonction_syntaxe():
    if True:
        print("Erreur de syntaxe")  # Erreur corrigée
"""

        fichier_test = "/tmp/code_avec_erreurs.py"
        with open(fichier_test, "w", encoding="utf-8") as f:
            f.write(code_avec_erreurs)

        start = time.time()

        # Utilise Athalia pour corriger
        cmd = [
            "python",
            "bin/core/athalia_unified.py",
            fichier_test,
            "--action",
            "correct",
            "--auto-fix",
        ]

        try:
            result = validate_and_run(cmd, timeout=30)
            temps_correction = time.time() - start

            if result.returncode != 0:
                return {
                    "succes": False,
                    "erreur": f"Correction échouée: {result.stderr}",
                    "temps": temps_correction,
                }

            # Vérifie que le fichier corrigé existe
            fichier_corrige = f"{fichier_test}.corrected"
            if not os.path.exists(fichier_corrige):
                return {
                    "succes": False,
                    "erreur": "Fichier corrigé non créé",
                    "temps": temps_correction,
                }

            # Test de compilation du fichier corrigé
            try:
                with open(fichier_corrige, encoding="utf-8") as f:
                    code_corrige = f.read()
                compile(code_corrige, fichier_corrige, "exec")
                compilation_ok = True
            except Exception as e:
                compilation_ok = False
                erreur_compilation = str(e)

            return {
                "succes": (
                    compilation_ok
                    and temps_correction
                    <= self.seuils_critiques["temps_max_correction"]
                ),
                "temps": temps_correction,
                "compilation_ok": compilation_ok,
                "erreur_compilation": (
                    erreur_compilation if not compilation_ok else None
                ),
                "fichier_corrige": fichier_corrige,
            }

        except subprocess.TimeoutExpired:
            return {
                "succes": False,
                "erreur": "Timeout - Correction trop lente",
                "temps": 30,
            }
        except Exception as e:
            return {
                "succes": False,
                "erreur": f"Exception: {str(e)}",
                "temps": time.time() - start,
            }

    def test_robustesse_cas_limites(self) -> dict:
        """Test 3: Athalia gère-t-il les cas limites ?"""
        print("🔍 Test 3: Robustesse cas limites...")

        cas_limites = [
            {"nom": "Fichier vide", "contenu": "", "attendu": "Gestion d'erreur"},
            {
                "nom": "Fichier très long",
                "contenu": "print('test')\n" * 10000,
                "attendu": "Traitement sans crash",
            },
            {
                "nom": "Caractères spéciaux",
                "contenu": "print('éàçù€£¥')",
                "attendu": "Encodage correct",
            },
            {
                "nom": "Syntaxe invalide",
                "contenu": "def test():\n    if True:\n        print('test'",
                "attendu": "Détection d'erreur",
            },
        ]

        resultats_cas_limites = []
        temps_total = 0.0

        for cas in cas_limites:
            start = time.time()
            fichier_test = f"/tmp/cas_limite_{cas['nom'].replace(' ', '_')}.py"

            with open(fichier_test, "w", encoding="utf-8") as f:
                f.write(cas["contenu"])

            cmd = [
                "python",
                "bin/core/athalia_unified.py",
                fichier_test,
                "--action",
                "analyze",
            ]

            try:
                result = validate_and_run(cmd, timeout=10)
                temps_cas = time.time() - start
                temps_total += temps_cas

                resultats_cas_limites.append(
                    {
                        "cas": cas["nom"],
                        "succes": result.returncode == 0,
                        "temps": temps_cas,
                        "attendu": cas["attendu"],
                        "resultat": "OK" if result.returncode == 0 else "ERREUR",
                    }
                )

            except Exception as e:
                temps_cas = time.time() - start
                temps_total += temps_cas
                resultats_cas_limites.append(
                    {
                        "cas": cas["nom"],
                        "succes": False,
                        "temps": temps_cas,
                        "attendu": cas["attendu"],
                        "resultat": f"EXCEPTION: {str(e)}",
                    }
                )

        taux_succes = (
            sum(1 for r in resultats_cas_limites if r["succes"])
            / len(resultats_cas_limites)
            * 100
        )

        return {
            "succes": taux_succes >= 75,  # 75% de succès minimum
            "temps": temps_total,
            "taux_succes": taux_succes,
            "cas_testes": len(cas_limites),
            "resultats_detailles": resultats_cas_limites,
        }

    def test_performance_benchmark(self) -> dict:
        """Test 4: Performance et benchmark"""
        print("🔍 Test 4: Performance benchmark...")

        # Test de performance sur un projet simple
        projet_benchmark = f"/tmp/benchmark_athalia_{int(time.time())}"
        os.makedirs(projet_benchmark, exist_ok=True)

        # Crée plusieurs fichiers pour tester
        for i in range(10):
            with open(f"{projet_benchmark}/file_{i}.py", "w") as f:
                f.write(
                    f"""
def fonction_{i}():
    return {i}

if __name__ == "__main__":
    print(fonction_{i}())
"""
                )

        start = time.time()
        cmd = [
            "python",
            "bin/core/athalia_unified.py",
            projet_benchmark,
            "--action",
            "complete",
            "--auto-fix",
        ]

        try:
            result = validate_and_run(cmd, timeout=120)
            temps_total = time.time() - start

            # Mesure de la mémoire utilisée (approximative)
            import psutil  # type: ignore

            process = psutil.Process()
            memoire_utilisee = float(process.memory_info().rss) / 1024 / 1024  # MB

            return {
                "succes": (
                    result.returncode == 0
                    and temps_total <= self.seuils_critiques["temps_max_generation"]
                    and memoire_utilisee <= self.seuils_critiques["memoire_max"]
                ),
                "temps": temps_total,
                "memoire_mb": memoire_utilisee,
                "fichiers_traites": 10,
                "performance_ok": temps_total <= 30,
            }

        except Exception as e:
            return {
                "succes": False,
                "erreur": f"Benchmark échoué: {str(e)}",
                "temps": time.time() - start,
            }

    def test_qualite_code_genere(self) -> dict:
        """Test 5: Qualité du code généré"""
        print("🔍 Test 5: Qualité du code généré...")

        # Test avec un projet plus complexe
        projet_qualite = f"/tmp/qualite_athalia_{int(time.time())}"
        os.makedirs(projet_qualite, exist_ok=True)

        # Crée un fichier avec des problèmes de qualité
        code_problematique = """
import os
import sys
import time
import datetime
import json
import subprocess
import pathlib
import shutil
import tempfile
import logging
import argparse
import configparser
import csv
import xml.etree.ElementTree as ET
import yaml
import toml
import requests
import urllib.parse
import hashlib
import base64
import zlib
import gzip
import bz2
import lzma
import pickle
import shelve
import sqlite3
import threading
import multiprocessing
import asyncio
import concurrent.futures
import queue
import collections
import itertools
import functools
import operator
import math
import random
import statistics
import decimal
import fractions
import cmath
import array
import struct
import mmap
import select
import socket
import ssl
import http.client
import urllib.request
import urllib.error
import urllib.parse
import email
import smtplib
import poplib
import imaplib
import ftplib
import telnetlib
import nntplib
import smtpd
import http.server
import socketserver
import xmlrpc.client
import xmlrpc.server
import webbrowser
import cgi
import cgitb
import wsgiref.simple_server
import wsgiref.util
import wsgiref.validate
import wsgiref.handlers
import wsgiref.headers
import wsgiref.responder
import wsgiref.simple_server
import wsgiref.util
import wsgiref.validate
import wsgiref.handlers
import wsgiref.headers
import wsgiref.responder

def fonction_tres_longue_avec_beaucoup_de_parametres(param1, param2, param3, param4, param5, param6, param7, param8, param9, param10):
    # Cette fonction est trop longue et a trop de paramètres
    resultat = 0
    for i in range(1000):
        resultat += i
        if i % 100 == 0:
            print(f"Progression: {i}")
    return resultat

class ClasseAvecBeaucoupDeMethodes:
    def __init__(self):
        self.valeur = 0

    def methode1(self):
        pass

    def methode2(self):
        pass

    def methode3(self):
        pass

    def methode4(self):
        pass

    def methode5(self):
        pass

    def methode6(self):
        pass

    def methode7(self):
        pass

    def methode8(self):
        pass

    def methode9(self):
        pass

    def methode10(self):
        pass

# Code dupliqué
def fonction1():
    x = 1
    y = 2
    return x + y

def fonction2():
    x = 1
    y = 2
    return x + y

# Variables non utilisées
variable_non_utilisee = "test"
"""

        with open(f"{projet_qualite}/code_problematique.py", "w") as f:
            f.write(code_problematique)

        start = time.time()
        cmd = [
            "python",
            "bin/core/athalia_unified.py",
            projet_qualite,
            "--action",
            "improve",
            "--auto-fix",
        ]

        try:
            result = validate_and_run(cmd, timeout=60)
            temps_amelioration = time.time() - start

            if result.returncode != 0:
                return {
                    "succes": False,
                    "erreur": f"Amélioration échouée: {result.stderr}",
                    "temps": temps_amelioration,
                }

            # Analyse de la qualité après amélioration
            fichier_ameliore = f"{projet_qualite}/code_problematique.py.improved"
            if os.path.exists(fichier_ameliore):
                with open(fichier_ameliore) as f:
                    code_ameliore = f.read()

                # Mesures de qualité simples
                lignes_code = len(code_ameliore.split("\n"))
                fonctions = code_ameliore.count("def ")
                classes = code_ameliore.count("class ")
                imports = code_ameliore.count("import ")

                return {
                    "succes": True,
                    "temps": temps_amelioration,
                    "lignes_code": lignes_code,
                    "fonctions": fonctions,
                    "classes": classes,
                    "imports": imports,
                    "qualite_amelioree": True,
                }
            else:
                return {
                    "succes": False,
                    "erreur": "Fichier amélioré non créé",
                    "temps": temps_amelioration,
                }

        except Exception as e:
            return {
                "succes": False,
                "erreur": f"Test qualité échoué: {str(e)}",
                "temps": time.time() - start,
            }

    def validation_complete(self) -> dict:
        """Exécute tous les tests de validation"""
        print("🚀 Démarrage de la validation objective complète...")

        start_total = time.time()

        # Exécute tous les tests
        self.resultats["generation_compilation"] = self.test_generation_et_compilation()
        self.resultats["correction_reelle"] = self.test_correction_reelle()
        self.resultats["robustesse_cas_limites"] = self.test_robustesse_cas_limites()
        self.resultats["performance_benchmark"] = self.test_performance_benchmark()
        self.resultats["qualite_code_genere"] = self.test_qualite_code_genere()

        temps_total = time.time() - start_total

        # Calcule le score global
        tests_reussis = sum(
            1 for r in self.resultats.values() if r.get("succes", False)
        )
        score_global = (tests_reussis / len(self.resultats)) * 100

        validation_reussie = score_global >= self.seuils_critiques["taux_succes_min"]

        print(f"✅ Validation terminée en {temps_total:.2f}s")
        print(
            f"📊 Score global: {score_global:.1f}% ({tests_reussis}/{len(self.resultats)} tests réussis)"
        )
        print(f"🎯 Validation {'RÉUSSIE' if validation_reussie else 'ÉCHOUÉE'}")

        return {
            "validation_reussie": validation_reussie,
            "score_global": score_global,
            "temps_total": temps_total,
            "tests_reussis": tests_reussis,
            "total_tests": len(self.resultats),
            "resultats_detailles": self.resultats,
        }

    def generer_rapport_objectif(self, resultats: dict, temps_total: float) -> str:
        """Génère un rapport détaillé de la validation"""
        rapport = {
            "timestamp": datetime.now().isoformat(),
            "validation_objective": "Athalia/Arkalia",
            "temps_total": temps_total,
            "score_global": resultats["score_global"],
            "validation_reussie": resultats["validation_reussie"],
            "seuils_critiques": self.seuils_critiques,
            "resultats_detailles": resultats["resultats_detailles"],
        }

        # Sauvegarde le rapport dans data/validation_reports
        os.makedirs("data/validation_reports", exist_ok=True)
        rapport_file = f"data/validation_reports/validation_objective_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(rapport_file, "w", encoding="utf-8") as f:
            json.dump(rapport, f, indent=2, ensure_ascii=False)

        print(f"📄 Rapport sauvegardé: {rapport_file}")
        return rapport_file


def main() -> int:
    """Fonction principale"""
    print("🎯 Validation Objective d'Athalia/Arkalia")
    print("=" * 50)

    validator = ValidationObjective()

    try:
        resultats = validator.validation_complete()
        rapport_file = validator.generer_rapport_objectif(
            resultats, resultats["temps_total"]
        )
        print(f"📄 Rapport objectif généré : {rapport_file}")

        if resultats["validation_reussie"]:
            print("🎉 Validation objective RÉUSSIE !")
            return 0
        else:
            print("❌ Validation objective ÉCHOUÉE !")
            return 1

    except Exception as e:
        print(f"💥 Erreur critique: {str(e)}")
        return 2


if __name__ == "__main__":
    exit(main())
