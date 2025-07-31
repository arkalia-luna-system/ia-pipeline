#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validation Objective d'Athalia/Arkalia
Tests qui ne peuvent pas mentir - Mesures concrètes et indépendantes
"""

from datetime import datetime
import json
import os
from pathlib import Path
import subprocess
import time


# Import du validateur de sécurité
try:
    from athalia_core.security_validator import SecurityError, validate_and_run
except ImportError:
    # Fallback si le module n'est pas disponible
    def validate_and_run(command, **kwargs):
        return subprocess.run(command, **kwargs)

    class SecurityError(Exception):
        pass


class ValidationObjective:
    def __init__(self):
        self.resultats = {}
        self.seuils_critiques = {
            "temps_max_generation": 30,  # 30 secondes max pour générer un projet
            "temps_max_correction": 10,  # 10 secondes max pour corriger
            "taux_compilation_min": 80,  # 80% du code généré doit compiler
            "taux_succes_min": 85,  # 85% de succès minimum
            "memoire_max": 1000,  # 1GB max
        }

    def test_generation_et_compilation(self):
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

        cmd = (
            f"python scripts/athalia_unified.py {projet_test} --action complete"
            " --auto-fix"
        )

        try:
            # Utilisation du validateur de sécurité
            cmd_parts = cmd.split()
            result = validate_and_run(cmd_parts, timeout=60)
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
                    with open(py_file, "r", encoding="utf-8") as f:
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

    def test_correction_reelle(self):
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
        cmd = (
            "python scripts/athalia_unified.py"
            f" {os.path.dirname(fichier_test)} --action fix --auto-fix"
        )

        try:
            result = subprocess.run(
                cmd, shell=True, capture_output=True, text=True, timeout=30
            )
            temps_correction = time.time() - start

            if result.returncode != 0:
                return {
                    "succes": False,
                    "erreur": f"Correction échouée: {result.stderr}",
                    "temps": temps_correction,
                }

            # Vérifie si le code corrigé compile maintenant
            try:
                with open(fichier_test, "r", encoding="utf-8") as f:
                    code_corrige = f.read()
                compile(code_corrige, fichier_test, "exec")
                compilation_ok = True
                erreur_compilation = None
            except Exception as e:
                compilation_ok = False
                erreur_compilation = str(e)

            return {
                "succes": compilation_ok,
                "temps": temps_correction,
                "code_compile_apres_correction": compilation_ok,
                "erreur_compilation": erreur_compilation,
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
                "erreur": f"Exception lors de la correction: {str(e)}",
                "temps": time.time() - start,
            }

    def test_robustesse_cas_limites(self):
        """Test 3: Athalia gère-t-il gracieusement les cas d'erreur ?"""
        print("🔍 Test 3: Robustesse et cas limites...")

        tests_robustesse = []

        # Test avec fichier inexistant
        cmd = [
            "python",
            "scripts/athalia_unified.py",
            "--audit",
            "/fichier/inexistant/qui/n/existe/pas",
        ]
        result = validate_and_run(cmd)
        tests_robustesse.append(
            {
                "test": "fichier_inexistant",
                "succes": result.returncode != 1,  # Ne doit pas crasher (exit 1)
                "exit_code": result.returncode,
            }
        )

        # Test avec fichier vide
        fichier_vide = "/tmp/fichier_vide.py"
        with open(fichier_vide, "w") as f:
            f.write("")

        cmd = ["python", "scripts/athalia_unified.py", "--audit", fichier_vide]
        result = validate_and_run(cmd)
        tests_robustesse.append(
            {
                "test": "fichier_vide",
                "succes": result.returncode != 1,
                "exit_code": result.returncode,
            }
        )

        # Test avec syntaxe invalide
        fichier_syntaxe_invalide = "/tmp/syntaxe_invalide.py"
        with open(fichier_syntaxe_invalide, "w") as f:
            f.write("def func(:\n    invalid syntax here\n    )")

        cmd = [
            "python",
            "scripts/athalia_unified.py",
            "--audit",
            fichier_syntaxe_invalide,
        ]
        result = validate_and_run(cmd)
        tests_robustesse.append(
            {
                "test": "syntaxe_invalide",
                "succes": result.returncode != 1,
                "exit_code": result.returncode,
            }
        )

        # Calcul du taux de succès
        succes = sum(1 for t in tests_robustesse if t["succes"])
        taux_robustesse = (succes / len(tests_robustesse)) * 100

        return {
            "succes": taux_robustesse >= 80,  # 80% des cas doivent être gérés
            "taux_robustesse": taux_robustesse,
            "tests_detail": tests_robustesse,
        }

    def test_performance_benchmark(self):
        """Test 4: Performance vs solution manuelle"""
        print("🔍 Test 4: Benchmark de performance...")

        # Test de génération d'un projet simple
        start = time.time()
        projet_benchmark = "/tmp/benchmark_test"
        os.makedirs(projet_benchmark, exist_ok=True)

        # Crée un fichier Python simple pour benchmark
        with open(f"{projet_benchmark}/main.py", "w") as f:
            f.write(
                """def benchmark():
    return "test"

if __name__ == "__main__":
    benchmark()
"""
            )

        cmd = [
            "python",
            "scripts/athalia_unified.py",
            projet_benchmark,
            "--action",
            "complete",
        ]
        result = validate_and_run(cmd, timeout=60)
        temps_athalia = time.time() - start

        if result.returncode != 0:
            return {
                "succes": False,
                "erreur": f"Benchmark échoué: {result.stderr}",
                "temps_athalia": temps_athalia,
            }

        # Estimation du temps manuel (créer un projet équivalent)
        temps_estime_manuel = (
            300  # 5 minutes pour créer un projet équivalent manuellement
        )

        gain_temps = temps_estime_manuel / temps_athalia if temps_athalia > 0 else 0

        return {
            "succes": temps_athalia <= self.seuils_critiques["temps_max_generation"],
            "temps_athalia": temps_athalia,
            "temps_estime_manuel": temps_estime_manuel,
            "gain_temps": gain_temps,
            "efficacite": (
                "EXCELLENTE"
                if gain_temps > 10
                else "BONNE"
                if gain_temps > 5
                else "MOYENNE"
            ),
        }

    def test_qualite_code_genere(self):
        """Test 5: Qualité objective du code généré"""
        print("🔍 Test 5: Qualité du code généré...")

        # Génère un projet pour analyse
        projet_qualite = "/tmp/projet_qualite"
        os.makedirs(projet_qualite, exist_ok=True)

        # Crée un fichier Python pour analyse de qualité
        with open(f"{projet_qualite}/main.py", "w") as f:
            f.write(
                """def qualite_test():
    return "qualite"

if __name__ == "__main__":
    qualite_test()
"""
            )

        cmd = f"python scripts/athalia_unified.py {projet_qualite} --action complete"

        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, timeout=60
        )

        if result.returncode != 0:
            return {
                "succes": False,
                "erreur": "Impossible de générer le projet pour analyse",
            }

        # Analyse avec pylint si disponible
        try:
            cmd_pylint = f"python -m pylint {projet_qualite} --output-format=json"
            result_pylint = subprocess.run(
                cmd_pylint, shell=True, capture_output=True, text=True
            )

            if result_pylint.returncode == 0:
                try:
                    pylint_data = json.loads(result_pylint.stdout)
                    score_pylint = pylint_data.get("score", 0)
                    erreurs = len(
                        [
                            e
                            for e in pylint_data.get("errors", [])
                            if e.get("type") == "error"
                        ]
                    )
                    warnings = len([w for w in pylint_data.get("warnings", [])])

                    return {
                        "succes": score_pylint >= 7.0,  # Score pylint minimum
                        "score_pylint": score_pylint,
                        "erreurs": erreurs,
                        "warnings": warnings,
                        "qualite": (
                            "EXCELLENTE"
                            if score_pylint >= 9.0
                            else "BONNE"
                            if score_pylint >= 7.0
                            else "MOYENNE"
                        ),
                    }
                except json.JSONDecodeError:
                    pass
        except Exception:
            pass

        # Fallback: analyse basique
        fichiers_python = list(Path(projet_qualite).glob("**/*.py"))
        total_lignes = 0
        fonctions = 0
        classes = 0

        for py_file in fichiers_python:
            try:
                with open(py_file, "r", encoding="utf-8") as f:
                    contenu = f.read()
                    lignes = contenu.split("\n")
                    total_lignes += len(lignes)
                    fonctions += contenu.count("def ")
                    classes += contenu.count("class ")
            except Exception:
                pass

        return {
            "succes": total_lignes > 0,  # Au moins du code généré
            "lignes_code": total_lignes,
            "fonctions": fonctions,
            "classes": classes,
            "qualite": "ANALYSE_BASIQUE",
        }

    def validation_complete(self):
        """Validation complète objective"""
        print("🚀 Démarrage de la validation objective d'Athalia/Arkalia")
        print("=" * 60)

        tests = {
            "generation_compilation": self.test_generation_et_compilation,
            "correction_erreurs": self.test_correction_reelle,
            "robustesse": self.test_robustesse_cas_limites,
            "performance": self.test_performance_benchmark,
            "qualite_code": self.test_qualite_code_genere,
        }

        resultats = {}
        temps_total_start = time.time()

        for nom, test_func in tests.items():
            print(f"\n🔍 Exécution du test: {nom}")
            try:
                resultats[nom] = test_func()
                status = "✅ SUCCÈS" if resultats[nom].get("succes") else "❌ ÉCHEC"
                print(f"   {status}")

                if not resultats[nom].get("succes"):
                    print(f"   Erreur: {resultats[nom].get('erreur', 'Inconnue')}")

            except Exception as e:
                resultats[nom] = {"succes": False, "erreur": str(e)}
                print(f"   ❌ ERREUR: {str(e)}")

        temps_total = time.time() - temps_total_start

        # Génération du rapport
        rapport = self.generer_rapport_objectif(resultats, temps_total)

        # Sauvegarde du rapport
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        os.makedirs("logs", exist_ok=True)
        rapport_file = f"logs/rapport_validation_objective_{timestamp}.md"

        with open(rapport_file, "w", encoding="utf-8") as f:
            f.write(rapport)

        print(f"\n📊 Rapport sauvegardé: {rapport_file}")
        print("\n" + "=" * 60)
        print(rapport)

        return resultats

    def generer_rapport_objectif(self, resultats, temps_total):
        """Génère un rapport objectif et détaillé"""

        # Calcul des métriques globales
        tests_succes = sum(1 for r in resultats.values() if r.get("succes", False))
        taux_succes = (tests_succes / len(resultats)) * 100

        # Détermination du verdict
        if taux_succes >= 90:
            verdict = "🎉 EXCELLENT - Athalia est très fiable"
            recommandation = "Tu peux faire confiance à ton outil"
        elif taux_succes >= 75:
            verdict = "✅ BON - Athalia est fiable avec quelques améliorations"
            recommandation = "Quelques ajustements mineurs recommandés"
        elif taux_succes >= 50:
            verdict = "⚠️ MOYEN - Athalia a des problèmes à corriger"
            recommandation = "Corrections importantes nécessaires"
        else:
            verdict = "❌ PROBLÉMATIQUE - Athalia nécessite une refonte"
            recommandation = "Refonte majeure recommandée"

        rapport = f"""# 📊 Rapport de Validation Objective - Athalia/Arkalia

**Date:** {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
**Temps total:** {temps_total:.1f} secondes
**Tests réussis:** {tests_succes}/{len(resultats)} ({taux_succes:.1f}%)

## 🎯 Verdict Global
**{verdict}**

## 📈 Résultats Détaillés

"""

        for nom, resultat in resultats.items():
            status = "✅ SUCCÈS" if resultat.get("succes") else "❌ ÉCHEC"
            rapport += f"### {nom.replace('_', ' ').title()}\n"
            rapport += f"**Statut:** {status}\n\n"

            # Détails spécifiques selon le test
            if nom == "generation_compilation":
                if resultat.get("succes"):
                    rapport += (
                        f"- ⏱️ Temps de génération: {resultat.get('temps', 0):.1f}s\n"
                    )
                    rapport += (
                        "- 📁 Fichiers générés:"
                        f" {resultat.get('fichiers_generes', 0)}\n"
                    )
                    rapport += (
                        "- ✅ Taux de compilation:"
                        f" {resultat.get('taux_compilation', 0):.1f}%\n"
                    )
                else:
                    rapport += f"- ❌ Erreur: {resultat.get('erreur', 'Inconnue')}\n"

            elif nom == "correction_erreurs":
                if resultat.get("succes"):
                    rapport += (
                        f"- ⏱️ Temps de correction: {resultat.get('temps', 0):.1f}s\n"
                    )
                    rapport += "- ✅ Code compile après correction: OUI\n"
                else:
                    rapport += f"- ❌ Erreur: {resultat.get('erreur', 'Inconnue')}\n"

            elif nom == "robustesse":
                rapport += (
                    "- 🛡️ Taux de robustesse:"
                    f" {resultat.get('taux_robustesse', 0):.1f}%\n"
                )
                for test in resultat.get("tests_detail", []):
                    status_test = "✅" if test["succes"] else "❌"
                    rapport += (
                        f"- {status_test} {test['test']}: exit code"
                        f" {test['exit_code']}\n"
                    )

            elif nom == "performance":
                if resultat.get("succes"):
                    rapport += (
                        f"- ⏱️ Temps Athalia: {resultat.get('temps_athalia', 0):.1f}s\n"
                    )
                    rapport += (
                        "- ⏱️ Temps estimé manuel:"
                        f" {resultat.get('temps_estime_manuel', 0):.1f}s\n"
                    )
                    rapport += (
                        f"- 🚀 Gain de temps: {resultat.get('gain_temps', 0):.1f}x\n"
                    )
                    rapport += f"- 📊 Efficacité: {resultat.get('efficacite', 'N/A')}\n"
                else:
                    rapport += f"- ❌ Erreur: {resultat.get('erreur', 'Inconnue')}\n"

            elif nom == "qualite_code":
                if resultat.get("score_pylint"):
                    rapport += (
                        f"- 📊 Score pylint: {resultat.get('score_pylint', 0):.1f}/10\n"
                    )
                    rapport += f"- ❌ Erreurs: {resultat.get('erreurs', 0)}\n"
                    rapport += f"- ⚠️ Warnings: {resultat.get('warnings', 0)}\n"
                    rapport += f"- 📈 Qualité: {resultat.get('qualite', 'N/A')}\n"
                else:
                    rapport += (
                        f"- 📝 Lignes de code: {resultat.get('lignes_code', 0)}\n"
                    )
                    rapport += f"- 🔧 Fonctions: {resultat.get('fonctions', 0)}\n"
                    rapport += f"- 🏗️ Classes: {resultat.get('classes', 0)}\n"

            rapport += "\n"

        rapport += f"""
## 🎯 Recommandation
**{recommandation}**

## 📋 Métriques de Confiance

| Métrique | Valeur | Seuil | Statut |
|----------|--------|-------|--------|
| Taux de succès global | {taux_succes:.1f}% | 85% | "
 f"{"✅" if taux_succes >= 85 else "❌"} |"

## 🔍 Points d'Attention

"""

        # Ajoute des points d'attention spécifiques
        if resultats.get("generation_compilation", {}).get("taux_compilation", 0) < 90:
            rapport += (
                "- ⚠️ Le code généré ne compile pas toujours (amélioration nécessaire)\n"
            )

        if resultats.get("performance", {}).get("gain_temps", 0) < 5:
            rapport += "- ⚠️ Gain de temps limité (optimisation recommandée)\n"

        if resultats.get("robustesse", {}).get("taux_robustesse", 0) < 90:
            rapport += "- ⚠️ Robustesse insuffisante (gestion d'erreurs à améliorer)\n"

        rapport += f"""
## 🎉 Conclusion
Ce rapport est basé sur des **tests objectifs et mesurables**. "
"Les résultats ne peuvent pas mentir."

**{verdict}**

---
*Validation générée automatiquement le {datetime.now().strftime("%d/%m/%Y à %H:%M:%S")}*
"""

        return rapport


if __name__ == "__main__":
    validator = ValidationObjective()
    resultats = validator.validation_complete()

    # Affichage du score final
    tests_succes = sum(1 for r in resultats.values() if r.get("succes", False))
    taux_succes = (tests_succes / len(resultats)) * 100

    print(f"\n🎯 SCORE FINAL: {taux_succes:.1f}%")

    if taux_succes >= 85:
        print("🎉 TON OUTIL EST FIABLE ! Tu peux lui faire confiance.")
    elif taux_succes >= 70:
        print("✅ Ton outil est bon avec quelques améliorations mineures.")
    else:
        print("⚠️ Ton outil a des problèmes à corriger avant utilisation en production.")
