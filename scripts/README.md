# Scripts Utilitaires Athalia

Ce dossier contient tous les scripts utilitaires organisés par catégorie.

## 📁 **Structure**

### `robotics/` - Scripts Robotiques
- `athalia_robotics_integration.py` - Intégration avec les robots
- `demo_robotics.py` - Démonstrations robotiques

### `debug/` - Scripts de Débogage
- `debug_correction.py` - Outils de correction et débogage

## 🚀 **Utilisation**

### Scripts Robotiques
```bash
# Intégration robotique
python3 scripts/robotics/athalia_robotics_integration.py

# Démonstration
python3 scripts/robotics/demo_robotics.py
```

### Scripts de Débogage
```bash
# Correction automatique
python3 scripts/debug/debug_correction.py
```

## 📋 **Conventions**

- **Nommage** : `[domaine]_[fonction].py`
- **Documentation** : Chaque script doit avoir un docstring
- **Tests** : Scripts testés avant intégration
- **Logs** : Utilisation du système de logging centralisé

## 🔧 **Ajout de Nouveaux Scripts**

1. Créer le dossier approprié si nécessaire
2. Suivre les conventions de nommage
3. Ajouter la documentation
4. Tester le script
5. Mettre à jour ce README 