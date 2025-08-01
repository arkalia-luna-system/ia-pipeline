# 🚀 Guide d'Optimisation RAM pour Cursor

## 📊 Analyse de l'utilisation actuelle

**Utilisation RAM Cursor : ~1.3GB**
- Cursor Helper (Renderer) : 355MB
- Cursor Helper (Plugin) : 494MB  
- Cursor Helper (GPU) : 328MB
- Cursor principal : 108MB

## 🎯 Solutions d'optimisation

### 1. **Extensions à désactiver/désinstaller (Gain : 200-400MB)**

#### Extensions gourmandes identifiées :
- `continue.continue-1.0.19` - IA complète (très gourmande)
- `anysphere.cursorpyright-1.0.8` - TypeScript avancé
- `github.vscode-github-actions-0.27.2` - GitHub Actions
- `eamodio.gitlens-17.3.3` - Git avancé

#### Extensions à garder absolument :
- `ms-python.python` - Python LSP
- `charliermarsh.ruff` - Linting Python
- `ms-python.black-formatter` - Formatage
- `ms-python.isort` - Import sorting

### 2. **Configuration mémoire optimisée**

Créer le fichier : `~/.cursor/User/settings.json`

```json
{
  "files.watcherExclude": {
    "**/node_modules/**": true,
    "**/venv/**": true,
    "**/.git/**": true,
    "**/__pycache__/**": true,
    "**/build/**": true,
    "**/dist/**": true
  },
  "search.exclude": {
    "**/node_modules": true,
    "**/venv": true,
    "**/.git": true,
    "**/__pycache__": true
  },
  "files.exclude": {
    "**/__pycache__": true,
    "**/*.pyc": true,
    "**/.pytest_cache": true
  },
  "python.analysis.memory.keepLibraryAst": false,
  "python.analysis.autoImportCompletions": false,
  "typescript.preferences.includePackageJsonAutoImports": "off",
  "editor.suggest.showKeywords": false,
  "editor.quickSuggestions": {
    "other": false,
    "comments": false,
    "strings": false
  },
  "workbench.editor.enablePreview": false,
  "workbench.editor.enablePreviewFromQuickOpen": false,
  "extensions.autoUpdate": false,
  "extensions.autoCheckUpdates": false
}
```

### 3. **Optimisations système**

#### Script de nettoyage mémoire :
```bash
#!/bin/bash
# ath-clean-cursor-memory.sh
echo "🧹 Nettoyage mémoire Cursor..."

# Redémarrage des processus Cursor
pkill -f "Cursor Helper"
sleep 2

# Nettoyage cache
rm -rf ~/Library/Caches/Cursor
rm -rf ~/Library/Application\ Support/Cursor/Cache

# Nettoyage logs
find ~/Library/Logs/Cursor -name "*.log" -delete

echo "✅ Nettoyage terminé"
```

### 4. **Workflow d'optimisation recommandé**

#### Phase 1 : Nettoyage extensions (Gain immédiat)
1. Désactiver `continue.continue` temporairement
2. Désactiver `github.vscode-github-actions`
3. Désactiver `eamodio.gitlens` si pas utilisé

#### Phase 2 : Configuration (Gain progressif)
1. Appliquer les paramètres de configuration
2. Redémarrer Cursor
3. Tester les performances

#### Phase 3 : Maintenance (Gain continu)
1. Exécuter le script de nettoyage hebdomadaire
2. Surveiller l'utilisation mémoire
3. Désactiver les extensions inutilisées

## 📈 Résultats attendus

- **Réduction RAM** : 30-50% (400-600MB économisés)
- **Démarrage plus rapide** : 20-30% plus rapide
- **Réactivité améliorée** : Moins de lag lors de l'édition
- **Stabilité** : Moins de plantages

## 🔧 Commandes utiles

### Scripts créés automatiquement :

```bash
# Nettoyage mémoire complet
./bin/ath-clean-cursor-memory

# Monitoring mémoire en temps réel
./bin/ath-monitor-cursor-memory

# Monitoring continu (rafraîchissement automatique)
./bin/ath-monitor-cursor-memory --continuous

# Optimisation automatique complète
./bin/ath-optimize-cursor

# Optimisation rapide (sans questions)
./bin/ath-optimize-cursor --quick
```

### Commandes manuelles :

```bash
# Voir l'utilisation mémoire en temps réel
top -l 1 -o mem | grep -i cursor

# Nettoyer le cache Cursor
rm -rf ~/Library/Caches/Cursor

# Lister les extensions
ls ~/.cursor/extensions/

# Redémarrer Cursor proprement
pkill -f Cursor && open /Applications/Cursor.app
```

### Alias disponibles (après optimisation) :

```bash
cursor-clean     # Nettoyage mémoire
cursor-monitor   # Monitoring mémoire
cursor-optimize  # Optimisation complète
```

## ⚠️ Précautions

- Sauvegarder les paramètres avant modification
- Tester chaque changement individuellement
- Garder une liste des extensions essentielles
- Surveiller les performances après chaque modification 