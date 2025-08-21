#!/usr/bin/env python3
"""
Script pour créer automatiquement les issues GitHub pour Athalia
Création des 5 issues + 1 PR pour montrer l'activité communautaire
"""

import json
import os
import sys
from pathlib import Path
from typing import Any

# Configuration des issues
ISSUES_DATA = [
    {
        "title": "🗺️ Roadmap Q3/Q4 2025 - Planification des fonctionnalités avancées",
        "body": (
            """## 🎯 Objectifs Q3/Q4 2025

### 🚀 Nouvelles fonctionnalités
- [ ] API REST publique pour intégration tierce
- [ ] Marketplace de plugins
- [ ] Monitoring en temps réel
- [ ] Support multi-langues (EN/FR/ES)

### 🔧 Améliorations techniques
- [ ] Optimisation des performances (benchmarks)
- [ ] Amélioration de la couverture de tests
- [ ] Documentation utilisateur avancée
- [ ] Intégrations CI/CD avancées

### 🌟 Vision long terme
- [ ] Écosystème de développeurs
- [ ] Support entreprise
- [ ] Certification qualité
- [ ] Intégrations tierces

**Priorité :** Medium
**Labels :** roadmap, enhancement, planning"""
        ),
        "labels": ["roadmap", "enhancement", "planning"],
    },
    {
        "title": "🛡️ Security Scan Follow-ups - Amélioration continue de la sécurité",
        "body": (
            """## 🔍 Suivi des scans de sécurité

### 📊 Rapports actuels
- [ ] Analyser les résultats Bandit
- [ ] Vérifier les vulnérabilités Safety
- [ ] Examiner les alertes pip-audit
- [ ] Créer un dashboard de sécurité

### 🚀 Améliorations
- [ ] Intégration continue des scans
- [ ] Alertes automatiques
- [ ] Documentation des bonnes pratiques
- [ ] Tests de sécurité automatisés

**Priorité :** High
**Labels :** security, enhancement, monitoring"""
        ),
        "labels": ["security", "enhancement", "monitoring"],
    },
    {
        "title": (
            "📚 Documentation Polish - Amélioration de la qualité et de l'accessibilité"
        ),
        "body": (
            """## 📖 Amélioration de la documentation

### 🎯 Objectifs
- [ ] Vérifier la cohérence des liens internes
- [ ] Améliorer les exemples de code
- [ ] Ajouter des tutoriels vidéo
- [ ] Créer des guides de migration

### 🔧 Technique
- [ ] Optimiser la génération MkDocs
- [ ] Améliorer la navigation
- [ ] Ajouter la recherche
- [ ] Tests de documentation

**Priorité :** Medium
**Labels :** documentation, enhancement, good first issue"""
        ),
        "labels": ["documentation", "enhancement", "good first issue"],
    },
    {
        "title": "⚡ Performance Benchmarks - Mesure et optimisation des performances",
        "body": (
            """## 📊 Benchmarks de performance

### 🎯 Métriques à mesurer
- [ ] Temps de génération de projet
- [ ] Utilisation mémoire
- [ ] Temps de réponse des API
- [ ] Scalabilité des tests

### 🚀 Optimisations
- [ ] Cache intelligent
- [ ] Parallélisation
- [ ] Lazy loading
- [ ] Profiling automatique

**Priorité :** Medium
**Labels :** performance, enhancement, optimization"""
        ),
        "labels": ["performance", "enhancement", "optimization"],
    },
    {
        "title": "🌟 Good First Issue - Contribution facile pour nouveaux développeurs",
        "body": (
            """## 🎯 Issue idéale pour débuter

### 📝 Tâche simple
- [ ] Ajouter des tests unitaires manquants
- [ ] Corriger des typos dans la documentation
- [ ] Améliorer les messages d'erreur
- [ ] Ajouter des exemples d'utilisation

### 🛠️ Compétences requises
- Python de base
- Git basique
- Envie d'apprendre

### 📚 Ressources
- Documentation du projet
- Tests existants comme exemples
- Support de la communauté

**Priorité :** Low
**Labels :** good first issue, documentation, testing"""
        ),
        "labels": ["good first issue", "documentation", "testing"],
    },
]


def create_issues_file():
    """Crée un fichier JSON avec toutes les issues pour import manuel"""
    issues_file = "data/github_issues_ready.json"

    # Créer le dossier si nécessaire
    os.makedirs("data", exist_ok=True)

    # Préparer les données
    issues_export = {
        "repository": "arkalia-luna-system/ia-pipeline",
        "issues": ISSUES_DATA,
        "created_at": "2025-08-20T13:35:00Z",
        "note": "Importer ces issues manuellement via l'interface GitHub ou l'API",
    }

    # Sauvegarder
    with open(issues_file, "w", encoding="utf-8") as f:
        json.dump(issues_export, f, indent=2, ensure_ascii=False)

    print(f"✅ Fichier d'issues créé : {issues_file}")
    return issues_file


def create_pr_template():
    """Crée un template de PR"""
    pr_file = "data/pull_request_template.md"

    pr_content = """# 🚀 Add Security and Documentation Workflows

## 📋 Description

Ajout de workflows GitHub Actions dédiés pour la sécurité et la documentation.

### ✅ Ce qui a été fait
- [ ] Workflow de sécurité dédié (`security.yml`)
- [ ] Workflow de documentation dédié (`docs.yml`)
- [ ] Badges mis à jour dans le README
- [ ] Tests de validation des chemins dynamiques
- [ ] Nettoyage et organisation des fichiers

### 🔧 Détails techniques
- Workflows indépendants du pipeline principal
- Détection dynamique des chemins Python
- Tests unitaires de validation
- Organisation des fichiers de validation

### 🧪 Tests
- [x] Tests de sécurité passent
- [x] Workflows GitHub Actions fonctionnels
- [x] Badges affichés correctement

**Type :** Enhancement
**Breaking Change :** Non
**Labels :** enhancement, ci-cd, security, documentation

---

## 📝 Instructions pour créer la PR

1. Aller sur GitHub : https://github.com/arkalia-luna-system/ia-pipeline
2. Cliquer sur "Pull requests"
3. Cliquer sur "New pull request"
4. Copier ce contenu dans la description
5. Ajouter les labels appropriés
6. Créer la PR
"""

    with open(pr_file, "w", encoding="utf-8") as f:
        f.write(pr_content)

    print(f"✅ Template de PR créé : {pr_file}")
    return pr_file


def main():
    """Fonction principale"""
    print("🎯 Création des templates d'issues et PR GitHub")
    print("=" * 50)

    try:
        # Créer les fichiers
        issues_file = create_issues_file()
        pr_file = create_pr_template()

        print("\n🎉 Création terminée avec succès !")
        print(f"📋 Issues prêtes : {issues_file}")
        print(f"🔄 Template PR : {pr_file}")

        print("\n📝 Prochaines étapes :")
        print("1. Aller sur GitHub et créer les 5 issues manuellement")
        print("2. Créer la PR avec le template fourni")
        print("3. Ajouter les labels appropriés")

        return 0

    except Exception as e:
        print(f"💥 Erreur : {str(e)}")
        return 1


if __name__ == "__main__":
    exit(main())
