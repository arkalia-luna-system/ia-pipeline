#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validation Continue d'Athalia/Arkalia
Surveillance en temps réel de la qualité et détection de régressions
"""

import json
import logging
import os
import subprocess
import threading
import time
from datetime import datetime


class ValidationContinue:
    def __init__(self, intervalle_minutes=60):
        self.intervalle_minutes = intervalle_minutes
        self.actif = False
        self.thread_surveillance = None
        self.historique = []
        self.seuil_regression = 10  # 10% de baisse = régression

        # Configuration du logging
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler("validation_continue.log"),
                logging.StreamHandler(),
            ],
        )
        self.logger = logging.getLogger(__name__)

    def test_rapide(self):
        """Test rapide de validation (version allégée)"""
        start = time.time()
        resultats = {}

        # Test 1: Démarrage
        resultats["demarrage"] = self.test_demarrage()

        # Test 2: Imports
        resultats["imports"] = self.test_imports()

        # Test 3: Génération mini
        resultats["generation"] = self.test_generation_mini()

        # Test 4: Correction basique
        resultats["correction"] = self.test_correction_basique()

        temps_total = time.time() - start

        # Calcul du taux de succès
        succes = sum(1 for r in resultats.values() if r.get("succes", False))
        taux_succes = (succes / len(resultats)) * 100

        validation = {
            "timestamp": datetime.now().isoformat(),
            "taux_succes": taux_succes,
            "temps_total": temps_total,
            "resultats": resultats,
            "erreurs_critiques": len(
                [r for r in resultats.values() if not r.get("succes", False)]
            ),
        }

        # Sauvegarde dans l'historique
        self.historique.append(validation)
        self.sauvegarder_historique()

        return validation

    def test_demarrage(self):
        """Test de démarrage d'Athalia"""
        try:
            cmd = "python scripts/athalia_unified.py --help"
            result = subprocess.run(
                cmd, shell=True, capture_output=True, text=True, timeout=10
            )
            return {"succes": result.returncode == 0}
        except Exception as e:
            return {"succes": False, "erreur": str(e)}

    def test_imports(self):
        """Test des imports critiques"""
        try:
            cmd = "python -c 'import athalia_core; print(\"OK\")'"
            result = subprocess.run(
                cmd, shell=True, capture_output=True, text=True, timeout=10
            )
            return {"succes": result.returncode == 0}
        except Exception as e:
            return {"succes": False, "erreur": str(e)}

    def test_generation_mini(self):
        """Test de génération minimal"""
        try:
            # Crée un projet test temporaire
            projet_test = f"/tmp/test_continue_{int(time.time())}"
            os.makedirs(projet_test, exist_ok=True)

            with open(f"{projet_test}/main.py", "w") as f:
                f.write("print('test')")

            cmd = f"python scripts/athalia_unified.py {projet_test} --action audit"
            result = subprocess.run(
                cmd, shell=True, capture_output=True, text=True, timeout=30
            )

            # Nettoyage
            import shutil

            shutil.rmtree(projet_test, ignore_errors=True)

            return {"succes": result.returncode == 0}
        except Exception as e:
            return {"succes": False, "erreur": str(e)}

    def test_correction_basique(self):
        """Test de correction basique"""
        try:
            # Crée un fichier avec une erreur simple
            fichier_test = "/tmp/test_correction.py"
            with open(fichier_test, "w") as f:
                f.write("x = 1\ny = 2\nprint(x + y + z)  # Erreur: z non défini")

            cmd = f"python scripts/athalia_unified.py {os.path.dirname(fichier_test)} --action fix"
            result = subprocess.run(
                cmd, shell=True, capture_output=True, text=True, timeout=30
            )

            # Nettoyage
            os.remove(fichier_test)

            return {"succes": result.returncode == 0}
        except Exception as e:
            return {"succes": False, "erreur": str(e)}

    def detecter_regression(self, validation_actuelle):
        """Détecte une régression par rapport à l'historique"""
        if len(self.historique) < 3:
            return None

        # Compare avec les 3 dernières validations
        recentes = self.historique[-3:]
        taux_moyen_recent = sum(v["taux_succes"] for v in recentes) / len(recentes)

        baisse = taux_moyen_recent - validation_actuelle["taux_succes"]

        if baisse > self.seuil_regression:
            return {
                "type": "regression",
                "baisse": baisse,
                "taux_avant": taux_moyen_recent,
                "taux_apres": validation_actuelle["taux_succes"],
            }

        return None

    def demarrer_surveillance(self):
        """Démarre la surveillance continue"""
        if self.actif:
            self.logger.warning("Surveillance déjà active")
            return

        self.actif = True

        def boucle_surveillance():
            self.logger.info("🚀 Démarrage de la surveillance continue...")

            while self.actif:
                try:
                    self.logger.info("🔍 Exécution du test de validation...")
                    validation = self.test_rapide()

                    # Détection de régression
                    regression = self.detecter_regression(validation)

                    if regression:
                        self.logger.warning(
                            f"🚨 RÉGRESSION DÉTECTÉE: {regression['baisse']:.1f}% de baisse"
                        )
                        self.alerter_regression(validation, regression)

                    # Rapport de tendance périodique
                    if len(self.historique) % 10 == 0:  # Tous les 10 tests
                        self.generer_rapport_tendance()
                        self.logger.info("📊 Rapport de tendance généré")

                    self.logger.info(
                        f"✅ Test terminé: {validation['taux_succes']:.1f}% de succès"
                    )

                except Exception as e:
                    self.logger.error(f"❌ Erreur lors du test: {str(e)}")

                # Attente jusqu'au prochain test
                time.sleep(self.intervalle_minutes * 60)

        self.thread_surveillance = threading.Thread(
            target=boucle_surveillance, daemon=True
        )
        self.thread_surveillance.start()

        return self.thread_surveillance

    def arreter_surveillance(self):
        """Arrête la surveillance continue"""
        self.actif = False
        if self.thread_surveillance:
            self.thread_surveillance.join(timeout=5)
        self.logger.info("🛑 Surveillance arrêtée")

    def alerter_regression(self, validation, regression):
        """Génère une alerte en cas de régression"""
        alerte = {
            "timestamp": datetime.now().isoformat(),
            "type": "regression",
            "validation": validation,
            "regression": regression,
            "gravite": "CRITIQUE" if regression["baisse"] > 20 else "MOYENNE",
        }

        # Sauvegarde de l'alerte
        alertes_file = "alertes_regression.json"
        alertes = []

        if os.path.exists(alertes_file):
            try:
                with open(alertes_file, "r") as f:
                    alertes = json.load(f)
            except Exception:
                alertes = []

        alertes.append(alerte)

        with open(alertes_file, "w") as f:
            json.dump(alertes, f, indent=2)

        # Génération du rapport d'alerte
        rapport = self.generer_rapport_alerte(alerte)
        self.logger.warning(f"🚨 ALERTE: {rapport[:100]}...")

    def generer_rapport_alerte(self, alerte):
        """Génère un rapport d'alerte détaillé"""
        regression = alerte["regression"]
        validation = alerte["validation"]

        rapport = f"""# 🚨 ALERTE RÉGRESSION - Athalia/Arkalia

**Date:** {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}  
**Gravité:** {alerte['gravite']}  
**Baisse détectée:** {regression['baisse']:.1f}%

## 📊 Détails de la Régression

| Métrique | Avant | Après | Baisse |
|----------|-------|-------|--------|
| Taux de succès | {regression['taux_avant']:.1f}% | {regression['taux_apres']:.1f}% | {regression['baisse']:.1f}% |
| Temps total | - | {validation['temps_total']:.1f}s | - |
| Erreurs critiques | - | {validation['erreurs_critiques']} | - |

## 🔍 Analyse des Résultats

"""

        for nom, resultat in validation["resultats"].items():
            status = "✅ SUCCÈS" if resultat.get("succes") else "❌ ÉCHEC"
            rapport += f"- **{nom}:** {status}\n"

            if not resultat.get("succes"):
                rapport += f"  - Erreur: {resultat.get('erreur', 'Inconnue')}\n"

        rapport += """
## 🎯 Actions Recommandées

1. **Vérifier** les derniers changements de code
2. **Analyser** les logs d'erreur
3. **Tester** manuellement les fonctionnalités défaillantes
4. **Revert** si nécessaire vers une version stable

## 📈 Historique Récent

"""

        # Affiche les 5 dernières validations
        for validation in self.historique[-5:]:
            date = datetime.fromisoformat(validation["timestamp"]).strftime(
                "%d/%m %H:%M"
            )
            rapport += f"- {date}: {validation['taux_succes']:.1f}% de succès\n"

        # Sauvegarde du rapport
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        rapport_file = f"alerte_regression_{timestamp}.md"

        with open(rapport_file, "w", encoding="utf-8") as f:
            f.write(rapport)

        self.logger.info(f"📄 Rapport d'alerte généré: {rapport_file}")

    def sauvegarder_historique(self):
        """Sauvegarde l'historique des validations"""
        try:
            with open("historique_validation.json", "w") as f:
                json.dump(self.historique, f, indent=2)
        except Exception as e:
            self.logger.error(f"Erreur sauvegarde historique: {str(e)}")

    def charger_historique(self):
        """Charge l'historique des validations"""
        try:
            if os.path.exists("historique_validation.json"):
                with open("historique_validation.json", "r") as f:
                    self.historique = json.load(f)
        except Exception as e:
            self.logger.error(f"Erreur chargement historique: {str(e)}")

    def generer_rapport_tendance(self):
        """Génère un rapport de tendance basé sur l'historique"""
        if len(self.historique) < 5:
            return "Pas assez de données pour analyser les tendances"

        # Calcul des tendances
        recentes = self.historique[-10:]  # 10 dernières validations
        anciennes = self.historique[:10]  # 10 premières validations

        if len(anciennes) < 10:
            anciennes = self.historique[: len(self.historique) // 2]

        taux_recent = sum(v["taux_succes"] for v in recentes) / len(recentes)
        taux_ancien = sum(v["taux_succes"] for v in anciennes) / len(anciennes)

        evolution = taux_recent - taux_ancien

        rapport = f"""# 📊 Rapport de Tendance - Athalia/Arkalia

**Période analysée:** {len(self.historique)} validations  
**Tendance:** {'📈 AMÉLIORATION' if evolution > 0 else '📉 RÉGRESSION' if evolution < 0 else '➡️ STABLE'}

## 📈 Métriques de Tendance

| Métrique | Ancien | Récent | Évolution |
|----------|--------|--------|-----------|
| Taux de succès | {taux_ancien:.1f}% | {taux_recent:.1f}% | {evolution:+.1f}% |
| Temps moyen | {sum(v['temps_total'] for v in anciennes)/len(anciennes):.1f}s | {sum(v['temps_total'] for v in recentes)/len(recentes):.1f}s | - |
| Erreurs critiques | {sum(v['erreurs_critiques'] for v in anciennes)/len(anciennes):.1f} | {sum(v['erreurs_critiques'] for v in recentes)/len(recentes):.1f} | - |

## 🎯 Recommandations

"""

        if evolution > 5:
            rapport += (
                "🎉 **Excellent !** Athalia s'améliore. Continue dans cette direction."
            )
        elif evolution > 0:
            rapport += "✅ **Bien !** Légère amélioration détectée."
        elif evolution > -5:
            rapport += "⚠️ **Attention !** Légère régression détectée. Surveille les prochains changements."
        else:
            rapport += "🚨 **Problème !** Régression significative détectée. Action corrective nécessaire."

        return rapport


if __name__ == "__main__":
    # Exemple d'utilisation
    validator = ValidationContinue(intervalle_minutes=30)  # Test toutes les 30 minutes

    # Charge l'historique existant
    validator.charger_historique()

    # Test unique
    print("🔍 Test de validation continue...")
    validation = validator.test_rapide()
    print(f"Résultat: {validation['taux_succes']:.1f}% de succès")

    # Démarre la surveillance continue
    print("🚀 Démarrage de la surveillance continue...")
    thread = validator.demarrer_surveillance()

    try:
        # Garde le programme actif avec timeout
        timeout_seconds = 300  # 5 minutes max
        start_time = time.time()
        while time.time() - start_time < timeout_seconds:
            time.sleep(10)  # Check toutes les 10 secondes
        print(f"\n⏰ Timeout atteint ({timeout_seconds}s) - Arrêt automatique")
    except KeyboardInterrupt:
        print("\n🛑 Arrêt de la surveillance...")
    finally:
        validator.arreter_surveillance()
