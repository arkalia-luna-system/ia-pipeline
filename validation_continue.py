#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validation Continue d'Athalia/Arkalia
Surveillance automatique et détection de régressions
"""

import time
import json
import os
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
import threading
import logging

class ValidationContinue:
    def __init__(self, intervalle_minutes=60):
        self.intervalle = intervalle_minutes * 60  # Conversion en secondes
        self.historique = []
        self.seuils_alerte = {
            'taux_succes_min': 80,
            'temps_max': 120,
            'memoire_max': 1000,
            'erreurs_critiques_max': 2
        }
        self.actif = False
        
        # Configuration du logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('validation_continue.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def test_rapide(self):
        """Test rapide pour validation continue (5-10 secondes)"""
        start = time.time()
        
        tests_rapides = {
            'demarrage': self.test_demarrage,
            'imports': self.test_imports,
            'generation_mini': self.test_generation_mini,
            'correction_basique': self.test_correction_basique
        }
        
        resultats = {}
        erreurs_critiques = 0
        
        for nom, test_func in tests_rapides.items():
            try:
                resultat = test_func()
                resultats[nom] = resultat
                if not resultat.get('succes'):
                    erreurs_critiques += 1
            except Exception as e:
                resultats[nom] = {'succes': False, 'erreur': str(e)}
                erreurs_critiques += 1
        
        temps_total = time.time() - start
        tests_succes = sum(1 for r in resultats.values() if r.get('succes'))
        taux_succes = (tests_succes / len(resultats)) * 100
        
        validation = {
            'timestamp': datetime.now().isoformat(),
            'temps_total': temps_total,
            'taux_succes': taux_succes,
            'erreurs_critiques': erreurs_critiques,
            'tests_detail': resultats,
            'statut': 'OK' if taux_succes >= self.seuils_alerte['taux_succes_min'] else 'ALERTE'
        }
        
        return validation
    
    def test_demarrage(self):
        """Test: Athalia démarre-t-il ?"""
        try:
            result = subprocess.run(
                ["python", "athalia_unified.py", "--version"],
                capture_output=True, text=True, timeout=10
            )
            return {
                'succes': result.returncode == 0,
                'temps': 0,
                'details': f"Exit code: {result.returncode}"
            }
        except Exception as e:
            return {'succes': False, 'erreur': str(e)}
    
    def test_imports(self):
        """Test: Les imports fonctionnent-ils ?"""
        try:
            code_test = """
import sys
sys.path.insert(0, '.')
try:
    from athalia_core.main import *
    from athalia_core.ai_robust import *
    print('OK')
except Exception as e:
    print(f'ERREUR: {e}')
    sys.exit(1)
"""
            result = subprocess.run(
                ["python", "-c", code_test],
                capture_output=True, text=True, timeout=10
            )
            return {
                'succes': result.returncode == 0,
                'temps': 0,
                'details': result.stdout.strip()
            }
        except Exception as e:
            return {'succes': False, 'erreur': str(e)}
    
    def test_generation_mini(self):
        """Test: Génération d'un mini-projet"""
        start = time.time()
        projet_test = f"/tmp/validation_continue_{int(time.time())}"
        
        try:
            cmd = f"python athalia_unified.py --generate --project-name MiniTest --output {projet_test}"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
            
            temps = time.time() - start
            succes = result.returncode == 0 and os.path.exists(projet_test)
            
            # Nettoyage
            if os.path.exists(projet_test):
                import shutil
                shutil.rmtree(projet_test)
            
            return {
                'succes': succes,
                'temps': temps,
                'details': f"Projet créé: {succes}"
            }
        except Exception as e:
            return {'succes': False, 'erreur': str(e)}
    
    def test_correction_basique(self):
        """Test: Correction basique"""
        start = time.time()
        
        # Crée un fichier avec une erreur simple
        fichier_test = "/tmp/test_correction_basique.py"
        with open(fichier_test, 'w') as f:
            f.write("def test():\n    x = 1\n    return x + y  # y n'existe pas\n")
        
        try:
            cmd = f"python athalia_unified.py --fix {fichier_test}"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=20)
            
            temps = time.time() - start
            
            # Vérifie si le fichier a été modifié
            with open(fichier_test, 'r') as f:
                contenu = f.read()
            
            # Nettoyage
            os.remove(fichier_test)
            
            return {
                'succes': result.returncode == 0,
                'temps': temps,
                'details': f"Fichier modifié: {len(contenu)} caractères"
            }
        except Exception as e:
            return {'succes': False, 'erreur': str(e)}
    
    def detecter_regression(self, validation_actuelle):
        """Détecte les régressions par rapport à l'historique"""
        if len(self.historique) < 3:
            return None
        
        # Compare avec les 3 dernières validations
        recentes = self.historique[-3:]
        taux_moyen = sum(v['taux_succes'] for v in recentes) / len(recentes)
        
        regression = {
            'detectee': False,
            'type': None,
            'details': None
        }
        
        # Détection de régression de performance
        if validation_actuelle['taux_succes'] < taux_moyen - 10:
            regression['detectee'] = True
            regression['type'] = 'PERFORMANCE'
            regression['details'] = f"Taux de succès chuté de {taux_moyen:.1f}% à {validation_actuelle['taux_succes']:.1f}%"
        
        # Détection d'augmentation des erreurs critiques
        erreurs_moyennes = sum(v['erreurs_critiques'] for v in recentes) / len(recentes)
        if validation_actuelle['erreurs_critiques'] > erreurs_moyennes + 1:
            regression['detectee'] = True
            regression['type'] = 'STABILITE'
            regression['details'] = f"Erreurs critiques augmentées de {erreurs_moyennes:.1f} à {validation_actuelle['erreurs_critiques']}"
        
        # Détection de ralentissement
        temps_moyen = sum(v['temps_total'] for v in recentes) / len(recentes)
        if validation_actuelle['temps_total'] > temps_moyen * 1.5:
            regression['detectee'] = True
            regression['type'] = 'VITESSE'
            regression['details'] = f"Temps d'exécution augmenté de {temps_moyen:.1f}s à {validation_actuelle['temps_total']:.1f}s"
        
        return regression
    
    def demarrer_surveillance(self):
        """Démarre la surveillance continue"""
        if self.actif:
            self.logger.warning("⚠️ Surveillance déjà active")
            return None
        
        self.actif = True
        self.logger.info("🚀 Démarrage de la surveillance continue")
        
        def boucle_surveillance():
            """Boucle de surveillance avec arrêt propre"""
            while self.actif:
                try:
                    # Test rapide de validation
                    validation = self.test_rapide()
                    
                    # Détection de régression
                    regression = self.detecter_regression(validation)
                    if regression and regression['detectee']:
                        self.logger.warning(f"⚠️ RÉGRESSION DÉTECTÉE: {regression['type']} - {regression['details']}")
                        self.alerter_regression(validation, regression)
                    
                    # Ajout à l'historique
                    self.historique.append(validation)
                    
                    # Limite l'historique à 50 entrées (réduit de 100 à 50)
                    if len(self.historique) > 50:
                        self.historique = self.historique[-50:]
                    
                    # Log du statut
                    statut_emoji = "✅" if validation['statut'] == 'OK' else "⚠️"
                    self.logger.info(f"{statut_emoji} Validation: {validation['taux_succes']:.1f}% de succès en {validation['temps_total']:.1f}s")
                    
                    # Sauvegarde de l'historique
                    self.sauvegarder_historique()
                    
                except Exception as e:
                    self.logger.error(f"❌ Erreur dans la surveillance: {str(e)}")
                
                # Attente avant le prochain test
                if self.actif:
                    time.sleep(self.intervalle)
        
        # Lance la surveillance dans un thread séparé
        thread_surveillance = threading.Thread(target=boucle_surveillance, daemon=True)
        thread_surveillance.start()
        
        return thread_surveillance
    
    def arreter_surveillance(self):
        """Arrête la surveillance continue"""
        self.actif = False
        self.logger.info("🛑 Arrêt de la surveillance continue")
    
    def alerter_regression(self, validation, regression):
        """Génère une alerte de régression"""
        alerte = {
            'timestamp': datetime.now().isoformat(),
            'type': regression['type'],
            'details': regression['details'],
            'validation': validation,
            'gravite': 'HAUTE' if validation['taux_succes'] < 50 else 'MOYENNE'
        }
        
        # Sauvegarde de l'alerte
        alertes_file = 'alertes_regression.json'
        alertes = []
        
        if os.path.exists(alertes_file):
            try:
                with open(alertes_file, 'r') as f:
                    alertes = json.load(f)
            except:
                alertes = []
        
        alertes.append(alerte)
        
        with open(alertes_file, 'w') as f:
            json.dump(alertes, f, indent=2)
        
        # Log de l'alerte
        self.logger.error(f"🚨 ALERTE RÉGRESSION: {regression['type']} - {regression['details']}")
        
        # Génération d'un rapport d'alerte
        self.generer_rapport_alerte(alerte)
    
    def generer_rapport_alerte(self, alerte):
        """Génère un rapport d'alerte détaillé"""
        rapport = f"""# 🚨 Alerte de Régression - Athalia/Arkalia

**Date:** {datetime.fromisoformat(alerte['timestamp']).strftime("%d/%m/%Y %H:%M:%S")}  
**Type:** {alerte['type']}  
**Gravité:** {alerte['gravite']}

## 📊 Détails de la Régression
{alerte['details']}

## 📈 Métriques Actuelles
- **Taux de succès:** {alerte['validation']['taux_succes']:.1f}%
- **Temps d'exécution:** {alerte['validation']['temps_total']:.1f}s
- **Erreurs critiques:** {alerte['validation']['erreurs_critiques']}

## 🔍 Tests Détaillés
"""
        
        for nom, resultat in alerte['validation']['tests_detail'].items():
            status = "✅" if resultat.get('succes') else "❌"
            rapport += f"- {status} **{nom}**: {resultat.get('details', 'N/A')}\n"
        
        rapport += f"""
## 🎯 Actions Recommandées

1. **Vérifier les derniers changements** dans le code
2. **Analyser les logs** pour identifier la cause
3. **Tester manuellement** les fonctionnalités affectées
4. **Revert si nécessaire** vers une version stable

## 📋 Historique Récent
"""
        
        # Ajoute les 5 dernières validations
        for i, validation in enumerate(self.historique[-5:]):
            date = datetime.fromisoformat(validation['timestamp']).strftime("%H:%M:%S")
            rapport += f"- {date}: {validation['taux_succes']:.1f}% de succès\n"
        
        # Sauvegarde du rapport
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        rapport_file = f"alerte_regression_{timestamp}.md"
        
        with open(rapport_file, 'w', encoding='utf-8') as f:
            f.write(rapport)
        
        self.logger.info(f"📄 Rapport d'alerte généré: {rapport_file}")
    
    def sauvegarder_historique(self):
        """Sauvegarde l'historique des validations"""
        try:
            with open('historique_validation.json', 'w') as f:
                json.dump(self.historique, f, indent=2)
        except Exception as e:
            self.logger.error(f"Erreur sauvegarde historique: {str(e)}")
    
    def charger_historique(self):
        """Charge l'historique des validations"""
        try:
            if os.path.exists('historique_validation.json'):
                with open('historique_validation.json', 'r') as f:
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
            anciennes = self.historique[:len(self.historique)//2]
        
        taux_recent = sum(v['taux_succes'] for v in recentes) / len(recentes)
        taux_ancien = sum(v['taux_succes'] for v in anciennes) / len(anciennes)
        
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
            rapport += "🎉 **Excellent !** Athalia s'améliore. Continue dans cette direction."
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