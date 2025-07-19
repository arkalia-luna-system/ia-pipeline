#!/usr/bin/env python3
"""
📚 ATHALIA DOCUMENTATION GENERATOR
==================================
Générateur automatique de documentation qui :
- Met à jour tous les fichiers de documentation
- Génère des guides d'utilisation
- Crée des index automatiques
- Synchronise la documentation avec le code
"""

import os
import json
import yaml
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
import subprocess
import re

class AthaliaDocGenerator:
    """Générateur de documentation automatique"""
    
    def __init__(self, root_path: Optional[str] = None):
        self.root_path = Path(root_path or os.getcwd())
        self.docs_path = self.root_path / "docs"
        self.docs_path.mkdir(exist_ok=True)
        
        # Configuration de la documentation
        self.doc_config = {
            "project_name": "Athalia/Arkalia",
            "version": "1.0.0",
            "description": "Système d'industrialisation IA complet",
            "author": "Équipe Athalia",
            "last_update": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    
    def generate_main_index(self) -> None:
        """Générer l'index principal de la documentation"""
        index_content = f"""# 📚 Documentation Athalia/Arkalia

## 🚀 Vue d'ensemble

**{self.doc_config['project_name']}** - {self.doc_config['description']}

**Version :** {self.doc_config['version']}  
**Dernière mise à jour :** {self.doc_config['last_update']}

## 📋 Table des Matières

### 🎯 Guides Utilisateur
- [Guide d'Installation](INSTALL.md) - Installation et configuration
- [Guide d'Utilisation](USAGE.md) - Utilisation quotidienne
- [Guide des Alias](ALIAS.md) - Tous les alias disponibles
- [Guide des Tests](TESTS_GUIDE.md) - Tests et qualité
- [Guide des Plugins](PLUGINS_GUIDE.md) - Système de plugins

### 🔧 Guides Développeur
- [Guide du Développeur](DEVELOPER_GUIDE.md) - Développement et contribution
- [Guide API](API_REFERENCE.md) - Référence API complète
- [Guide CI/CD](CI_PROBLEMS_ANALYSIS.md) - Intégration continue
- [Guide de Déploiement](DEPLOYMENT.md) - Déploiement et production

### 📊 Documentation Technique
- [Architecture](ARCHITECTURE.md) - Architecture du système
- [Modules](MODULES.md) - Documentation des modules
- [Configuration](CONFIGURATION.md) - Configuration avancée
- [Troubleshooting](TROUBLESHOOTING.md) - Résolution de problèmes

### 🎨 Guides Spécialisés
- [Guide des Prompts](GUIDE_PROMPTS_TEST.md) - Prompts IA et tests
- [Guide des Templates](TEMPLATES.md) - Templates et génération
- [Guide de Sécurité](SECURITY.md) - Sécurité et audit
- [Guide de Performance](PERFORMANCE.md) - Optimisation et benchmarks

### 📈 Rapports et Analyses
- [Rapport Final](FINAL_SUMMARY.md) - Résumé du projet
- [Inventaire](INVENTAIRE_COMPLET.md) - Inventaire complet
- [Roadmap](ROADMAP.md) - Feuille de route
- [Changelog](CHANGELOG.md) - Historique des changements

## 🚀 Démarrage Rapide

### Installation
```bash
# Cloner le repository
git clone <repository-url>
cd athalia-dev-setup

# Installer les dépendances
pip install -r config/requirements.txt

# Charger les alias
source setup/alias-unified.sh
```

### Utilisation Basique
```bash
# Générer un projet
ath-generate 'mon-projet'

# Industrialiser un projet
ath-unified mon-projet --action complete

# Ouvrir le dashboard
ath-dashboard
```

### Système Intelligent
```bash
# Charger le système intelligent
ath-intelligent

# Obtenir de l'aide contextuelle
ath-help-intelligent

# Diagnostic du système
ath-diagnostic
```

## 🔗 Liens Utiles

- **Dashboard :** [Dashboard Interactif](../dashboard/dashboard.html)
- **Configuration :** [Fichier de Config](../config/athalia_config.yaml)
- **Tests :** [Suite de Tests](../tests/)
- **Modules :** [Modules Avancés](../modules/)

## 📞 Support

Pour toute question ou problème :
1. Consultez le [Guide de Troubleshooting](TROUBLESHOOTING.md)
2. Vérifiez les [Issues GitHub](https://github.com/your-repo/issues)
3. Contactez l'équipe de développement

---

*Documentation générée automatiquement par Athalia Doc Generator*
"""
        
        index_file = self.docs_path / "README.md"
        index_file.write_text(index_content, encoding='utf-8')
        print(f"✅ Index principal généré : {index_file}")
    
    def generate_alias_documentation(self) -> None:
        """Générer la documentation des alias"""
        alias_file = self.root_path / "setup" / "alias-unified.sh"
        if not alias_file.exists():
            print("❌ Fichier d'alias non trouvé")
            return
        
        # Lire les alias
        aliases = []
        categories = {}
        current_category = "Général"
        
        with open(alias_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('=== ') and line.endswith(' ==='):
                    current_category = line.replace('=== ', '').replace(' ===', '')
                    categories[current_category] = []
                elif line.startswith('alias ath-'):
                    alias_name = line.split('=')[0].replace('alias ', '').strip()
                    aliases.append(alias_name)
                    if current_category not in categories:
                        categories[current_category] = []
                    categories[current_category].append(alias_name)
        
        # Générer la documentation
        doc_content = f"""# 🚀 Guide des Alias Athalia/Arkalia

## 📋 Vue d'ensemble

Ce guide liste tous les alias disponibles dans le système Athalia/Arkalia.

**Dernière mise à jour :** {self.doc_config['last_update']}

## 🎯 Alias par Catégorie

"""
        
        for category, category_aliases in categories.items():
            if category_aliases:
                doc_content += f"\n### {category}\n\n"
                doc_content += "| Alias | Description |\n"
                doc_content += "|-------|-------------|\n"
                
                for alias in sorted(category_aliases):
                    doc_content += f"| `{alias}` | À documenter |\n"
        
        # Ajouter les statistiques d'usage si disponibles
        learning_db = self.root_path / "data" / "athalia_learning.json"
        if learning_db.exists():
            try:
                learning_data = json.loads(learning_db.read_text())
                usage_stats = learning_data.get("module_usage", {})
                
                if usage_stats:
                    doc_content += "\n## 📊 Statistiques d'Usage\n\n"
                    doc_content += "| Alias | Utilisations |\n"
                    doc_content += "|-------|--------------|\n"
                    
                    sorted_usage = sorted(usage_stats.items(), key=lambda x: x[1], reverse=True)
                    for alias, count in sorted_usage[:15]:
                        doc_content += f"| `{alias}` | {count} |\n"
            except Exception as e:
                print(f"⚠️  Erreur lors de la lecture des statistiques : {e}")
        
        # Ajouter les exemples d'utilisation
        doc_content += """

## 💡 Exemples d'Utilisation

### 🚀 Démarrage Rapide
```bash
# Charger le système
source setup/alias-unified.sh

# Générer un projet
ath-generate 'mon-projet'

# Industrialiser
ath-unified mon-projet --action complete
```

### 🧪 Tests et Qualité
```bash
# Lancer les tests
ath-test

# Vérifier la qualité
ath-lint

# Couverture de tests
ath-coverage
```

### 🔧 Développement
```bash
# Menu de développement
ath-dev-boost

# Dashboard interactif
ath-dashboard

# Audit intelligent
ath-audit
```

### 🎯 Système Intelligent
```bash
# Charger le système intelligent
ath-intelligent

# Aide contextuelle
ath-help-intelligent

# Diagnostic
ath-diagnostic
```

## 🔗 Voir Aussi

- [Guide d'Installation](INSTALL.md)
- [Guide d'Utilisation](USAGE.md)
- [Guide du Développeur](DEVELOPER_GUIDE.md)

---

*Documentation générée automatiquement*
"""
        
        alias_doc_file = self.docs_path / "ALIAS.md"
        alias_doc_file.write_text(doc_content, encoding='utf-8')
        print(f"✅ Documentation des alias générée : {alias_doc_file}")
    
    def generate_modules_documentation(self) -> None:
        """Générer la documentation des modules"""
        modules_content = f"""# 📦 Modules Athalia/Arkalia

## 🚀 Vue d'ensemble

Documentation de tous les modules du système Athalia/Arkalia.

**Dernière mise à jour :** {self.doc_config['last_update']}

## 📋 Modules par Type

"""
        
        # Découvrir les modules
        module_types = {
            "Core": self.root_path / "athalia_core",
            "Modules Avancés": self.root_path / "modules",
            "Agents": self.root_path / "agents",
            "Plugins": self.root_path / "plugins"
        }
        
        for type_name, type_path in module_types.items():
            if type_path.exists():
                modules_content += f"\n### {type_name}\n\n"
                
                # Lister les modules de ce type
                if type_path.is_dir():
                    for py_file in type_path.glob("*.py"):
                        if py_file.name != "__init__.py":
                            module_name = py_file.stem
                            module_path = py_file.relative_to(self.root_path)
                            
                            # Essayer d'extraire la docstring
                            try:
                                with open(py_file, 'r', encoding='utf-8') as f:
                                    content = f.read()
                                    # Chercher la docstring
                                    doc_match = re.search(r'"""(.*?)"""', content, re.DOTALL)
                                    description = doc_match.group(1).strip() if doc_match else "Module sans description"
                            except Exception:
                                description = "Module sans description"
                            
                            modules_content += f"#### {module_name}\n\n"
                            modules_content += f"**Fichier :** `{module_path}`\n\n"
                            modules_content += f"**Description :** {description}\n\n"
                            modules_content += "---\n\n"
        
        modules_content += """
## 🔗 Utilisation

### Charger un module
```python
# Module core
from athalia_core import audit, analytics

# Module avancé
from modules import auto_correction_avancee

# Agent
from agents import ath_context_prompt
```

### Exemple d'utilisation
```python
# Audit intelligent
from athalia_core.audit import audit_project_intelligent
result = audit_project_intelligent("./mon-projet")

# Auto-correction
from modules.auto_correction_avancee import AutoCorrectionAvancee
corrector = AutoCorrectionAvancee()
corrector.corriger_projet("./mon-projet")
```

## 📊 Statistiques

- **Modules Core :** Gestion des fonctionnalités principales
- **Modules Avancés :** Fonctionnalités spécialisées
- **Agents :** IA et automatisation
- **Plugins :** Extensions du système

---

*Documentation générée automatiquement*
"""
        
        modules_doc_file = self.docs_path / "MODULES.md"
        modules_doc_file.write_text(modules_content, encoding='utf-8')
        print(f"✅ Documentation des modules générée : {modules_doc_file}")
    
    def generate_usage_guide(self) -> None:
        """Générer le guide d'utilisation"""
        usage_content = f"""# 💻 Guide d'Utilisation Athalia/Arkalia

## 🚀 Démarrage Rapide

### Prérequis
- Python 3.8+
- Git
- pip

### Installation
```bash
# Cloner le repository
git clone <repository-url>
cd athalia-dev-setup

# Installer les dépendances
pip install -r config/requirements.txt

# Charger les alias
source setup/alias-unified.sh
```

## 🎯 Utilisation Quotidienne

### 1. Génération de Projet
```bash
# Générer un projet simple
ath-generate 'calculatrice simple'

# Générer avec industrialisation automatique
ath-generate 'API REST pour gestion de tâches' -o mon-projet -i

# Mode simulation
ath-generate 'dashboard web interactif' -d
```

### 2. Industrialisation de Projet
```bash
# Industrialisation complète
ath-unified mon-projet --action complete

# Audit uniquement
ath-unified mon-projet --action audit

# Tests uniquement
ath-unified mon-projet --action test
```

### 3. Développement
```bash
# Menu de développement
ath-dev-boost

# Dashboard interactif
ath-dashboard

# Tests rapides
ath-test
```

## 🔧 Fonctionnalités Avancées

### Système Intelligent
```bash
# Charger le système intelligent
ath-intelligent

# Aide contextuelle
ath-help-intelligent

# Diagnostic du système
ath-diagnostic

# Mise à jour automatique
ath-update-intelligent
```

### Coordination Intelligente
```bash
# Analyser le système
ath-coordinator-analyze

# Obtenir des insights
ath-coordinator-insights

# Mettre à jour la documentation
ath-coordinator-update-docs
```

### Modules Spécialisés
```bash
# Auto-correction avancée
ath-auto-correct

# Dashboard unifié
ath-dashboard-unified

# Profils utilisateur avancés
ath-profile-advanced
```

## 📊 Workflow Recommandé

### 1. Création de Projet
```bash
# 1. Générer le projet
ath-generate 'mon-projet' -o ./mon-projet -i

# 2. Vérifier le résultat
cd mon-projet
ls -la

# 3. Tester le projet
python main.py
```

### 2. Développement
```bash
# 1. Charger les alias
source ../setup/alias-unified.sh

# 2. Menu de développement
ath-dev-boost

# 3. Tests continus
ath-test
```

### 3. Industrialisation
```bash
# 1. Industrialisation complète
ath-unified . --action complete

# 2. Vérifier les résultats
open athalia_report_*.json
open analytics_dashboard.html
```

## 🎨 Personnalisation

### Configuration
Le fichier de configuration principal se trouve dans `config/athalia_config.yaml`.

### Alias Personnalisés
Vous pouvez ajouter vos propres alias dans `setup/alias.sh`.

### Prompts Personnalisés
Créez vos prompts dans le dossier `prompts/`.

## 🔗 Ressources

- [Guide des Alias](ALIAS.md) - Tous les alias disponibles
- [Guide du Développeur](DEVELOPER_GUIDE.md) - Développement avancé
- [Guide des Tests](TESTS_GUIDE.md) - Tests et qualité
- [Troubleshooting](TROUBLESHOOTING.md) - Résolution de problèmes

---

*Guide généré automatiquement*
"""
        
        usage_doc_file = self.docs_path / "USAGE.md"
        usage_doc_file.write_text(usage_content, encoding='utf-8')
        print(f"✅ Guide d'utilisation généré : {usage_doc_file}")
    
    def generate_all_documentation(self) -> None:
        """Générer toute la documentation"""
        print("🚀 Génération de la documentation complète...")
        
        # Générer les différents types de documentation
        self.generate_main_index()
        self.generate_alias_documentation()
        self.generate_modules_documentation()
        self.generate_usage_guide()
        
        print("✅ Documentation complète générée !")
    
    def update_documentation(self) -> None:
        """Mettre à jour la documentation existante"""
        print("🔄 Mise à jour de la documentation...")
        
        # Vérifier quels fichiers existent et les mettre à jour
        if (self.docs_path / "README.md").exists():
            self.generate_main_index()
        
        if (self.docs_path / "ALIAS.md").exists():
            self.generate_alias_documentation()
        
        if (self.docs_path / "MODULES.md").exists():
            self.generate_modules_documentation()
        
        if (self.docs_path / "USAGE.md").exists():
            self.generate_usage_guide()
        
        print("✅ Documentation mise à jour !")

def main():
    """Fonction principale"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Athalia Documentation Generator")
    parser.add_argument("--action", choices=["generate", "update"], 
                       default="generate", help="Action à effectuer")
    parser.add_argument("--root", help="Racine du projet Athalia")
    
    args = parser.parse_args()
    
    # Initialiser le générateur
    generator = AthaliaDocGenerator(args.root)
    
    if args.action == "generate":
        generator.generate_all_documentation()
    elif args.action == "update":
        generator.update_documentation()

if __name__ == "__main__":
    main() 