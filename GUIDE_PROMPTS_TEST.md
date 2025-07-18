# 🎯 Guide Pratique - Prompts pour Tester Athalia

## 📋 Vue d'ensemble

Ce guide vous aide à choisir les bons prompts pour tester efficacement toutes les fonctionnalités d'Athalia.

---

## 🚀 **Prompts Recommandés par Catégorie**

### **1. Génération de Blueprints** 📋
**Objectif :** Tester la création de projets complets

#### Prompts Simples (Débutants)
```
"Crée un projet d'API REST simple"
"Génère un jeu vidéo 2D basique"
"Développe une application web simple"
```

#### Prompts Moyens (Intermédiaires)
```
"Crée un projet d'API REST avec authentification JWT"
"Génère un jeu vidéo 2D avec système de score"
"Développe une application web de gestion de tâches"
```

#### Prompts Complexes (Avancés)
```
"Conçois un système d'IA pour la classification d'images avec interface web"
"Crée un jeu vidéo 2D multijoueur avec base de données"
"Développe une plateforme e-commerce complète avec paiement"
```

### **2. Revue de Code** 🔍
**Objectif :** Tester l'analyse et l'amélioration de code

#### Prompts Basiques
```
"Analyse ce code Python"
"Vérifie la qualité de ce code"
"Propose des améliorations"
```

#### Prompts Spécifiques
```
"Analyse ce code Python et propose des améliorations"
"Vérifie la sécurité de cette fonction d'authentification"
"Optimise cette boucle de traitement de données"
"Refactorise ce code pour améliorer la lisibilité"
"Identifie les bugs potentiels dans ce code"
```

### **3. Documentation** 📚
**Objectif :** Tester la génération de documentation

#### Prompts Généraux
```
"Génère la documentation technique pour ce projet"
"Crée un guide d'installation et d'utilisation"
"Écris un README professionnel"
```

#### Prompts Spécifiques
```
"Documente l'API REST de cette application"
"Crée la documentation des tests"
"Génère un guide de contribution"
"Documente l'architecture du projet"
```

### **4. Sécurité** 🔒
**Objectif :** Tester l'audit de sécurité

#### Prompts Généraux
```
"Audite la sécurité de ce code web"
"Vérifie les vulnérabilités"
"Analyse la sécurité"
```

#### Prompts Spécifiques
```
"Vérifie les vulnérabilités d'injection SQL"
"Analyse la gestion des mots de passe"
"Contrôle la validation des entrées utilisateur"
"Vérifie la sécurité des sessions"
"Audite la sécurité des API"
```

### **5. Tests** 🧪
**Objectif :** Tester la génération de stratégies de tests

#### Prompts Généraux
```
"Propose une stratégie de tests pour ce projet"
"Génère des tests unitaires"
"Crée des tests d'intégration"
```

#### Prompts Spécifiques
```
"Génère des tests unitaires pour ces fonctions"
"Crée des tests d'intégration pour cette API"
"Planifie les tests de performance"
"Conçois des tests de sécurité"
"Crée des tests end-to-end"
```

### **6. Projets Spécifiques** 🎯
**Objectif :** Tester des domaines spécialisés

#### IA/Machine Learning
```
"Conçois un système de recommandation"
"Crée un pipeline de machine learning"
"Optimise ce modèle de classification"
```

#### Applications Mobiles
```
"Crée une application mobile avec Kivy"
"Développe une app mobile avec React Native"
"Conçois une interface mobile responsive"
```

#### IoT et Systèmes Embarqués
```
"Développe un système de monitoring IoT"
"Crée un contrôleur pour capteurs"
"Conçois un système de domotique"
```

#### Web et APIs
```
"Conçois une API REST scalable"
"Crée une application web progressive"
"Développe un système de microservices"
```

---

## 🎯 **Stratégies de Test**

### **Test Progressif**
1. **Commencez simple** : "Crée un projet simple"
2. **Ajoutez de la complexité** : "Crée un projet avec authentification"
3. **Testez les cas limites** : "Crée un projet très complexe"

### **Test par Type de Projet**
1. **Web** : APIs, sites, applications
2. **Desktop** : Applications, outils
3. **Mobile** : Apps, interfaces
4. **IA/ML** : Modèles, pipelines
5. **Jeux** : 2D, 3D, multijoueur

### **Test de Robustesse**
1. **Prompts longs** : Test de timeout
2. **Caractères spéciaux** : Test de parsing
3. **Langues multiples** : Test d'internationalisation
4. **Prompts vides** : Test de gestion d'erreurs

---

## 🛠️ **Outils de Test**

### **1. CLI Athalia**
```bash
# Test simple
python3 -m athalia_core.cli test-ai "votre prompt"

# Test avec verbose
python3 -m athalia_core.cli test-ai "votre prompt" --verbose

# Statut de l'IA
python3 -m athalia_core.cli ai-status
```

### **2. Script de Benchmark**
```bash
# Test de distillation
python setup/benchmark_distillation.py

# Test complet de tous les prompts
python setup/test_prompts_complet.py
```

### **3. API REST**
```bash
# Test d'autocomplétion
curl -X POST http://localhost:8000/autocomplete \
     -H "Content-Type: application/json" \
     -d '{"prompt": "votre prompt", "max_suggestions": 5}'
```

### **4. Dashboard Web**
- Ouvrir : `http://localhost:8080`
- Interface graphique pour tester

---

## 📊 **Métriques à Surveiller**

### **Performance**
- ⏱️ Temps de réponse
- 🔄 Ratio distillation/IA
- 📈 Débit (prompts/seconde)

### **Qualité**
- ✅ Taux de réussite
- 🎯 Pertinence des réponses
- 🔍 Cohérence des résultats

### **Robustesse**
- ❌ Taux d'erreurs
- 🔧 Gestion des cas limites
- 🛡️ Sécurité des réponses

---

## 🎯 **Prompts de Test Recommandés**

### **Pour Commencer (5 prompts)**
1. `"Crée un projet d'API REST simple"`
2. `"Analyse ce code Python"`
3. `"Génère la documentation"`
4. `"Audite la sécurité"`
5. `"Propose une stratégie de tests"`

### **Pour Test Complet (15 prompts)**
1. `"Crée un projet d'API REST avec authentification"`
2. `"Génère un jeu vidéo 2D avec Pygame"`
3. `"Développe une application web de gestion de tâches"`
4. `"Conçois un système d'IA pour la classification d'images"`
5. `"Crée un bot Discord avec Python"`
6. `"Analyse ce code Python et propose des améliorations"`
7. `"Vérifie la sécurité de cette fonction d'authentification"`
8. `"Optimise cette boucle de traitement de données"`
9. `"Génère la documentation technique pour ce projet"`
10. `"Crée un guide d'installation et d'utilisation"`
11. `"Audite la sécurité de ce code web"`
12. `"Vérifie les vulnérabilités d'injection SQL"`
13. `"Propose une stratégie de tests pour ce projet"`
14. `"Génère des tests unitaires pour ces fonctions"`
15. `"Conçois un système de recommandation"`

### **Pour Test Avancé (30 prompts)**
Utilisez le script `setup/test_prompts_complet.py` qui teste automatiquement 30 prompts répartis en 6 catégories.

---

## 🚨 **Dépannage**

### **Problèmes Courants**

#### **Réponse vide ou erreur**
- Vérifiez que l'IA est disponible : `python3 -m athalia_core.cli ai-status`
- Testez avec un prompt simple : `"test simple"`
- Vérifiez les logs : `tail -f athalia.log`

#### **Réponse corrompue**
- Le problème vient souvent d'Ollama
- Redémarrez Ollama : `ollama restart`
- Testez avec un autre modèle

#### **Timeout**
- Réduisez la complexité du prompt
- Vérifiez la connexion réseau
- Testez avec le mode mock

#### **Erreur de distillation**
- Vérifiez que l'orchestrateur fonctionne
- Testez avec un prompt simple
- Vérifiez les dépendances

---

## 🎉 **Conclusion**

Avec ces prompts et stratégies, vous pouvez tester efficacement toutes les fonctionnalités d'Athalia. Commencez simple, progressez vers la complexité, et surveillez les métriques pour optimiser les performances.

**Bonne exploration ! 🚀** 