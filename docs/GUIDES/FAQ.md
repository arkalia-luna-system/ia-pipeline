# ❓ FAQ - Athalia

**Date :** 27 juillet 2025
**Statut :** FAQ complète avec commandes validées

## 🎯 Questions Fréquentes

Ce document répond aux questions les plus courantes sur l'utilisation d'Athalia.

---

## 🔧 **Configuration**

### Q: Comment configurer Athalia pour mon projet ?
**R:** Utilisez les commandes suivantes :
```bash
# Audit en simulation pour vérifier la configuration
python athalia_unified.py . --action audit --dry-run

# Industrialisation complète pour configurer automatiquement
python athalia_unified.py . --action complete
```

### Q: Comment changer la langue d'Athalia ?
**R:** Utilisez l'option `--lang` :
```bash
# Français
python athalia_unified.py . --action audit --lang fr

# Anglais
python athalia_unified.py . --action audit --lang en
```

---

## 🔍 **Audit et Analyse**

### Q: Comment auditer mon projet ?
**R:** Utilisez l'action `audit` :
```bash
# Audit complet
python athalia_unified.py /chemin/vers/projet --action audit

# Audit en simulation (sans modification)
python athalia_unified.py /chemin/vers/projet --action audit --dry-run

# Audit avec détails
python athalia_unified.py /chemin/vers/projet --action audit --verbose
```

### Q: Comment corriger automatiquement les problèmes ?
**R:** Utilisez l'action `fix` :
```bash
# Correction automatique
python athalia_unified.py /chemin/vers/projet --action fix

# Correction en simulation
python athalia_unified.py /chemin/vers/projet --action fix --dry-run

# Correction avec auto-fix
python athalia_unified.py /chemin/vers/projet --action fix --auto-fix
```

---

## 📊 **Dashboard et Visualisation**

### Q: Comment ouvrir le dashboard ?
**R:** Utilisez l'action `dashboard` :
```bash
# Dashboard standard
python athalia_unified.py /chemin/vers/projet --action dashboard

# Dashboard avec utilisateur spécifique
python athalia_unified.py /chemin/vers/projet --action dashboard --utilisateur nom_utilisateur
```

### Q: Le dashboard ne démarre pas, que faire ?
**R:** Essayez ces solutions :
```bash
# Tuer les processus existants
lsof -ti:8501 | xargs kill -9

# Relancer le dashboard
python athalia_unified.py . --action dashboard
```

---

## 🔄 **Industrialisation**

### Q: Comment industrialiser mon projet ?
**R:** Utilisez l'action `complete` :
```bash
# Industrialisation complète
python athalia_unified.py /chemin/vers/projet --action complete

# Industrialisation sans audit
python athalia_unified.py /chemin/vers/projet --action complete --no-audit

# Industrialisation sans nettoyage
python athalia_unified.py /chemin/vers/projet --action complete --no-clean
```

### Q: Comment scanner mon projet ?
**R:** Utilisez l'option `--scan` :
```bash
# Scanner le projet
python athalia_unified.py /chemin/vers/projet --scan
```

---

## 🐛 **Dépannage**

### Q: Comment diagnostiquer les problèmes ?
**R:** Utilisez le mode verbose :
```bash
# Mode détaillé pour diagnostiquer
python athalia_unified.py . --action audit --verbose --dry-run
```

### Q: Comment voir les logs ?
**R:** Utilisez les commandes système :
```bash
# Voir les logs en temps réel
tail -f logs/athalia.log

# Voir les erreurs
grep "ERROR" logs/athalia.log
```

### Q: Comment réparer l'installation ?
**R:** Utilisez ces commandes :
```bash
# Réinstaller les dépendances
pip install -r requirements.txt --force-reinstall

# Vérifier l'installation
python athalia_unified.py . --action audit --dry-run
```

---

## 🔒 **Sécurité**

### Q: Comment sécuriser mon projet ?
**R:** Utilisez l'audit de sécurité :
```bash
# Audit de sécurité
python athalia_unified.py /chemin/vers/projet --action audit --verbose
```

---

## 📈 **Performance**

### Q: Comment optimiser les performances ?
**R:** Utilisez ces options :
```bash
# Audit avec optimisation
python athalia_unified.py /chemin/vers/projet --action audit --dry-run

# Industrialisation optimisée
python athalia_unified.py /chemin/vers/projet --action complete --no-audit
```

---

## 🔄 **Sauvegarde et Restauration**

### Q: Comment sauvegarder mon projet ?
**R:** Utilisez les commandes système :
```bash
# Sauvegarde manuelle
cp -r /chemin/projet /chemin/backup/

# Sauvegarde avec tar
tar -czf backup_$(date +%Y%m%d_%H%M%S).tar.gz /chemin/projet
```

### Q: Comment restaurer une sauvegarde ?
**R:** Utilisez les commandes système :
```bash
# Restaurer depuis une sauvegarde
cp -r /chemin/backup/* /chemin/restauration/

# Restaurer depuis un tar
tar -xzf backup_20250727_143022.tar.gz -C /chemin/restauration/
```

---

## 🧪 **Tests**

### Q: Comment lancer les tests ?
**R:** Utilisez pytest :
```bash
# Tous les tests
python -m pytest tests/ -v

# Tests avec couverture
python -m pytest tests/ --cov=athalia_core

# Tests spécifiques
python -m pytest tests/test_audit.py -v
```

---

## 📊 **Rapports et Métriques**

### Q: Comment générer des rapports ?
**R:** Utilisez l'audit avec sortie :
```bash
# Rapport JSON
python athalia_unified.py . --action audit > rapport.json

# Rapport CSV
python athalia_unified.py . --action audit | grep -v "INFO" > rapport.csv
```

### Q: Comment exporter les métriques ?
**R:** Utilisez ces commandes :
```bash
# Métriques système
ps aux | grep python > system_metrics.txt

# Métriques réseau
ping -c 5 google.com > network_metrics.txt
```

---

## 🔧 **Maintenance**

### Q: Comment nettoyer le projet ?
**R:** Utilisez les commandes système :
```bash
# Nettoyer les fichiers Python compilés
find . -name "*.pyc" -delete
find . -name "__pycache__" -type d -exec rm -rf {} +

# Nettoyer les caches
rm -rf .pytest_cache/
rm -rf .mypy_cache/
```

### Q: Comment mettre à jour Athalia ?
**R:** Utilisez pip :
```bash
# Mettre à jour les dépendances
pip install -r requirements.txt --upgrade

# Vérifier la mise à jour
python athalia_unified.py . --action audit --dry-run
```

---

## 🆘 **Support**

### Q: Comment obtenir de l'aide ?
**R:** Utilisez ces ressources :
```bash
# Aide de la commande
python athalia_unified.py --help

# Documentation
ls docs/GUIDES/
```

### Q: Comment signaler un bug ?
**R:** Collectez ces informations :
```bash
# Informations système
uname -a > bug_report.txt
python --version >> bug_report.txt

# Logs récents
tail -n 100 logs/athalia.log >> bug_report.txt 2>/dev/null || echo "Pas de logs" >> bug_report.txt
```

---

*FAQ mise à jour le 27 juillet 2025 avec toutes les commandes validées*
