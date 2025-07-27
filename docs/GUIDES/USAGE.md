# 🚀 Guide d'Utilisation - Athalia

**Date :** 27 juillet 2025  
**Statut :** Guide d'utilisation complet avec commandes validées

## 🎯 Vue d'ensemble

Ce guide présente toutes les commandes valides d'Athalia pour analyser, corriger et gérer vos projets.

---

## 📋 **Commandes Principales**

### 🔍 **Audit de Projet**
```bash
# Audit complet d'un projet
python athalia_unified.py /chemin/vers/projet --action audit

# Audit en mode simulation
python athalia_unified.py /chemin/vers/projet --action audit --dry-run

# Audit avec auto-correction
python athalia_unified.py /chemin/vers/projet --action audit --auto-fix
```

### 🔧 **Correction Automatique**
```bash
# Correction automatique
python athalia_unified.py /chemin/vers/projet --action fix

# Correction en simulation
python athalia_unified.py /chemin/vers/projet --action fix --dry-run

# Correction avec auto-fix
python athalia_unified.py /chemin/vers/projet --action fix --auto-fix
```

### 📊 **Dashboard Interactif**
```bash
# Lancer le dashboard
python athalia_unified.py /chemin/vers/projet --action dashboard

# Dashboard avec utilisateur spécifique
python athalia_unified.py /chemin/vers/projet --action dashboard --utilisateur nom_utilisateur
```

### 🔄 **Industrialisation Complète**
```bash
# Processus complet (audit + correction + tests)
python athalia_unified.py /chemin/vers/projet --action complete

# Industrialisation sans audit
python athalia_unified.py /chemin/vers/projet --action complete --no-audit

# Industrialisation sans nettoyage
python athalia_unified.py /chemin/vers/projet --action complete --no-clean
```

### 🔍 **Scan de Projet**
```bash
# Scanner un projet
python athalia_unified.py /chemin/vers/projet --scan
```

---

## ⚙️ **Options Avancées**

### 🌐 **Langue**
```bash
# Utiliser le français
python athalia_unified.py /chemin/vers/projet --action audit --lang fr

# Utiliser l'anglais
python athalia_unified.py /chemin/vers/projet --action audit --lang en
```

### 📝 **Mode Verbose**
```bash
# Affichage détaillé
python athalia_unified.py /chemin/vers/projet --action audit --verbose
```

### 🎭 **Profil Utilisateur**
```bash
# Utiliser un profil spécifique
python athalia_unified.py /chemin/vers/projet --action dashboard --utilisateur developpeur
```

---

## 💡 **Exemples d'Usage**

### 🔍 **Analyse d'un Projet Python**
```bash
# Analyser un projet Python
python athalia_unified.py ./mon-projet-python --action audit --verbose

# Corriger automatiquement
python athalia_unified.py ./mon-projet-python --action fix --auto-fix
```

### 🚀 **Industrialisation d'un Projet**
```bash
# Industrialisation complète
python athalia_unified.py ./mon-projet --action complete

# Industrialisation en simulation
python athalia_unified.py ./mon-projet --action complete --dry-run
```

### 📊 **Visualisation des Données**
```bash
# Ouvrir le dashboard
python athalia_unified.py ./mon-projet --action dashboard

# Dashboard avec profil développeur
python athalia_unified.py ./mon-projet --action dashboard --utilisateur dev --verbose
```

---

## 🔧 **Intégration CI/CD**

### 📋 **Script de Validation**
```bash
#!/bin/bash
echo "🔍 Validation du projet..."

# Audit en mode simulation
python athalia_unified.py . --action audit --dry-run

# Si l'audit passe, lancer l'industrialisation
if [ $? -eq 0 ]; then
    echo "✅ Audit réussi, lancement de l'industrialisation..."
    python athalia_unified.py . --action complete --no-audit
else
    echo "❌ Audit échoué, correction nécessaire"
    python athalia_unified.py . --action fix --auto-fix
fi
```

### 🐳 **Docker Integration**
```bash
# Dans un Dockerfile
RUN python athalia_unified.py /app --action audit --dry-run
RUN python athalia_unified.py /app --action complete --no-audit
```

---

## 📚 **Bonnes Pratiques**

### ✅ **Avant de Commiter**
```bash
# Vérifier la qualité du code
python athalia_unified.py . --action audit --dry-run

# Corriger automatiquement si nécessaire
python athalia_unified.py . --action fix --auto-fix
```

### 🔄 **Workflow Quotidien**
```bash
# 1. Scanner le projet
python athalia_unified.py . --scan

# 2. Audit en simulation
python athalia_unified.py . --action audit --dry-run

# 3. Correction si nécessaire
python athalia_unified.py . --action fix --auto-fix

# 4. Industrialisation
python athalia_unified.py . --action complete --no-audit
```

### 📊 **Monitoring**
```bash
# Ouvrir le dashboard pour surveiller
python athalia_unified.py . --action dashboard --utilisateur admin
```

---

## 🆘 **Dépannage**

### ❌ **Erreurs Communes**
```bash
# Si le dashboard ne démarre pas
lsof -ti:8501 | xargs kill -9
python athalia_unified.py . --action dashboard

# Si l'audit échoue
python athalia_unified.py . --action audit --dry-run --verbose
```

### 🔍 **Debug Mode**
```bash
# Mode verbose pour diagnostiquer
python athalia_unified.py . --action audit --verbose --dry-run
```

---

## 📖 **Ressources**

- **Documentation API :** `docs/API/`
- **Guide d'Installation :** `docs/GUIDES/INSTALLATION.md`
- **Démarrage Rapide :** `docs/QUICK_START.md`

---

*Guide mis à jour le 27 juillet 2025 avec toutes les commandes validées* 