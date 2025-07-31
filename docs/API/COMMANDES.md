# 📋 Commandes API - Athalia

**Date :** 27 juillet 2025
**Statut :** Guide complet des commandes validées

## 🎯 Vue d'ensemble

Ce document liste toutes les commandes valides d'Athalia avec leurs options et exemples d'usage.

---

## 🚀 **Actions Principales**

### 🔍 **Audit**
```bash
python athalia_unified.py <project_path> --action audit
```
**Description :** Analyse complète d'un projet
**Options :**
- `--dry-run` : Mode simulation
- `--verbose` : Affichage détaillé
- `--lang <fr|en>` : Langue de sortie

**Exemples :**
```bash
# Audit complet
python athalia_unified.py /chemin/projet --action audit

# Audit en simulation
python athalia_unified.py /chemin/projet --action audit --dry-run

# Audit avec détails
python athalia_unified.py /chemin/projet --action audit --verbose
```

### 🔧 **Correction**
```bash
python athalia_unified.py <project_path> --action fix
```
**Description :** Correction automatique des problèmes
**Options :**
- `--dry-run` : Mode simulation
- `--auto-fix` : Correction automatique
- `--verbose` : Affichage détaillé

**Exemples :**
```bash
# Correction automatique
python athalia_unified.py /chemin/projet --action fix

# Correction en simulation
python athalia_unified.py /chemin/projet --action fix --dry-run

# Correction avec auto-fix
python athalia_unified.py /chemin/projet --action fix --auto-fix
```

### 📊 **Dashboard**
```bash
python athalia_unified.py <project_path> --action dashboard
```
**Description :** Lance le dashboard interactif
**Options :**
- `--utilisateur <nom>` : Profil utilisateur
- `--verbose` : Affichage détaillé

**Exemples :**
```bash
# Dashboard standard
python athalia_unified.py /chemin/projet --action dashboard

# Dashboard avec utilisateur
python athalia_unified.py /chemin/projet --action dashboard --utilisateur dev
```

### 🔄 **Industrialisation**
```bash
python athalia_unified.py <project_path> --action complete
```
**Description :** Processus complet d'industrialisation
**Options :**
- `--no-audit` : Sans audit préalable
- `--no-clean` : Sans nettoyage
- `--dry-run` : Mode simulation
- `--verbose` : Affichage détaillé

**Exemples :**
```bash
# Industrialisation complète
python athalia_unified.py /chemin/projet --action complete

# Industrialisation sans audit
python athalia_unified.py /chemin/projet --action complete --no-audit

# Industrialisation sans nettoyage
python athalia_unified.py /chemin/projet --action complete --no-clean
```

---

## 🔍 **Options de Scan**

### 📡 **Scan de Projet**
```bash
python athalia_unified.py <project_path> --scan
```
**Description :** Scanner un projet pour analyse rapide
**Exemples :**
```bash
# Scanner le projet courant
python athalia_unified.py . --scan

# Scanner un projet spécifique
python athalia_unified.py /chemin/projet --scan
```

---

## ⚙️ **Options Globales**

### 🌐 **Langue**
```bash
--lang <fr|en>
```
**Description :** Définir la langue de sortie
**Exemples :**
```bash
python athalia_unified.py . --action audit --lang fr
python athalia_unified.py . --action audit --lang en
```

### 📝 **Mode Verbose**
```bash
--verbose
```
**Description :** Affichage détaillé des opérations
**Exemples :**
```bash
python athalia_unified.py . --action audit --verbose
python athalia_unified.py . --action fix --verbose
```

### 🎭 **Profil Utilisateur**
```bash
--utilisateur <nom>
```
**Description :** Utiliser un profil utilisateur spécifique
**Exemples :**
```bash
python athalia_unified.py . --action dashboard --utilisateur developpeur
python athalia_unified.py . --action dashboard --utilisateur admin
```

### 🔄 **Mode Simulation**
```bash
--dry-run
```
**Description :** Exécuter en mode simulation (sans modification)
**Exemples :**
```bash
python athalia_unified.py . --action audit --dry-run
python athalia_unified.py . --action fix --dry-run
```

### 🔧 **Auto-Correction**
```bash
--auto-fix
```
**Description :** Correction automatique des problèmes
**Exemples :**
```bash
python athalia_unified.py . --action fix --auto-fix
```

### 🚫 **Options d'Exclusion**

#### Exclure l'Audit
```bash
--no-audit
```
**Description :** Exclure l'audit du processus
**Exemples :**
```bash
python athalia_unified.py . --action complete --no-audit
```

#### Exclure le Nettoyage
```bash
--no-clean
```
**Description :** Exclure le nettoyage du processus
**Exemples :**
```bash
python athalia_unified.py . --action complete --no-clean
```

---

## 💡 **Exemples d'Usage Avancés**

### 🔍 **Workflow d'Audit Complet**
```bash
# 1. Scan rapide
python athalia_unified.py . --scan

# 2. Audit en simulation
python athalia_unified.py . --action audit --dry-run --verbose

# 3. Audit réel
python athalia_unified.py . --action audit --verbose

# 4. Correction automatique
python athalia_unified.py . --action fix --auto-fix

# 5. Industrialisation
python athalia_unified.py . --action complete --no-audit
```

### 🚀 **Workflow de Développement**
```bash
# 1. Audit avant commit
python athalia_unified.py . --action audit --dry-run

# 2. Correction si nécessaire
python athalia_unified.py . --action fix --auto-fix

# 3. Industrialisation
python athalia_unified.py . --action complete

# 4. Dashboard pour vérification
python athalia_unified.py . --action dashboard --utilisateur dev
```

### 🔧 **Workflow de Maintenance**
```bash
# 1. Audit de maintenance
python athalia_unified.py . --action audit --verbose

# 2. Correction des problèmes
python athalia_unified.py . --action fix --auto-fix

# 3. Industrialisation sans audit
python athalia_unified.py . --action complete --no-audit

# 4. Dashboard de monitoring
python athalia_unified.py . --action dashboard --utilisateur admin
```

---

## 📊 **Intégration CI/CD**

### 🔄 **Script de Validation**
```bash
#!/bin/bash
echo "🔍 Validation du projet..."

# Audit en simulation
python athalia_unified.py . --action audit --dry-run

if [ $? -eq 0 ]; then
    echo "✅ Audit réussi"
    python athalia_unified.py . --action complete --no-audit
else
    echo "❌ Audit échoué, correction nécessaire"
    python athalia_unified.py . --action fix --auto-fix
    python athalia_unified.py . --action complete --no-audit
fi
```

### 🐳 **Docker Integration**
```dockerfile
# Dans un Dockerfile
RUN python athalia_unified.py /app --action audit --dry-run
RUN python athalia_unified.py /app --action complete --no-audit
```

---

## 🆘 **Aide et Support**

### 📖 **Aide de la Commande**
```bash
python athalia_unified.py --help
```

### 🔍 **Validation de la Documentation**
```bash
python tools/maintenance/validation_documentation.py . --verbose
```

---

## 📚 **Ressources Complémentaires**

- **Guide d'Installation :** `docs/GUIDES/INSTALLATION.md`
- **Guide d'Usage :** `docs/GUIDES/USAGE.md`
- **FAQ :** `docs/GUIDES/FAQ.md`
- **Commandes Avancées :** `docs/API/COMMANDES_AVANCEES.md`

---

*Guide des commandes mis à jour le 27 juillet 2025 avec toutes les commandes validées*
