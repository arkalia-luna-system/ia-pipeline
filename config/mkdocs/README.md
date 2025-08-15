# 📚 **MKDOCS ATHALIA** - Configuration Documentation Web

## 📁 **Organisation**

Ce dossier contient la configuration **MkDocs** d'Athalia pour générer automatiquement un site web professionnel.

```
config/mkdocs/
├── README.md          # Ce fichier d'explication
├── mkdocs.yml         # Configuration principale
└── themes/            # Thèmes personnalisés (futur)
```

## 🚀 **Utilisation**

### **Génération du site :**
```bash
# Depuis la racine du projet
mkdocs build -f config/mkdocs/mkdocs.yml

# Ou avec le Makefile
make -f config/makefile/Makefile pages
```

### **Serveur de développement :**
```bash
# Lance un serveur local sur http://127.0.0.1:8000
mkdocs serve -f config/mkdocs/mkdocs.yml
```

## 🎯 **Fonctionnalités**

| **Fonctionnalité** | **Description** | **Impact CV** |
|-------------------|----------------|---------------|
| **Thème Material** | Interface moderne et responsive | +3-5k€ |
| **Navigation** | Menu organisé et intuitif | +2-3k€ |
| **Recherche** | Recherche intelligente | +2-3k€ |
| **Responsive** | Compatible mobile/desktop | +2-3k€ |
| **GitHub Pages** | Site web public automatique | +5-10k€ |

## 🌐 **Déploiement GitHub Pages**

1. **Configuration automatique** via GitHub Actions
2. **Site accessible** sur `https://arkalia-luna-system.github.io/ia-pipeline`
3. **Mise à jour automatique** à chaque push sur `main`

## 📊 **Structure du site**

```
🏠 Accueil
├── 🚀 Démarrage rapide
├── 🏗️ Architecture
├── 📚 Guides utilisateur
├── 🔧 API
├── 🧪 Tests
├── 📊 Dashboards
├── 🛡️ Sécurité
├── 📈 Performance
└── 🔍 Audit
```

## 💡 **Pourquoi cette organisation ?**

1. **Professionnalisme** : Configuration séparée et organisée
2. **Maintenabilité** : Facile de modifier sans toucher au code
3. **Évolutivité** : Ajout de thèmes et plugins facile
4. **CV Impact** : Montre la maîtrise des outils de documentation

## 🔄 **Mise à jour**

Pour modifier la configuration :
1. Édite `config/mkdocs/mkdocs.yml`
2. Teste avec `mkdocs serve -f config/mkdocs/mkdocs.yml`
3. Commit et push les changements

---

*Configuration maintenue par l'équipe Athalia - DevOps Automation Platform*
