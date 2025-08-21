# 🤝 **Directives de Contribution - Athalia**

## 📋 **Processus de Contribution**

### **1. Fork du Repository**
- Créer un fork du repository principal
- Cloner votre fork localement
- Configurer l'origine distante

### **2. Création de Branche Feature**
```bash
git checkout -b feature/nom-de-la-fonctionnalite
git push -u origin feature/nom-de-la-fonctionnalite
```

### **3. Ajout de Tests Complets**
- **Tests unitaires** : Couvrir toutes les nouvelles fonctionnalités
- **Tests d'intégration** : Vérifier l'interopérabilité
- **Tests de régression** : S'assurer qu'aucune fonctionnalité existante n'est cassée

### **4. Documentation des Changements**
- **Docstrings** : Toutes les nouvelles fonctions
- **README** : Mise à jour si nécessaire
- **CHANGELOG** : Ajouter les modifications

### **5. Soumission de Pull Request**
- **Description claire** : Expliquer le but et l'impact
- **Tests** : S'assurer que tous les tests passent
- **Revue de code** : Attendre l'approbation

## 🧪 **Standards de Qualité**

### **Tests**
- **Couverture minimale** : 80%
- **Tous les tests** doivent passer
- **Nouveaux tests** pour nouvelles fonctionnalités

### **Code**
- **Black** : Formatage automatique
- **Ruff** : Linting sans erreurs
- **Type hints** : Pour toutes les fonctions publiques

### **Documentation**
- **Français** : Langue principale du projet
- **Clarté** : Explications compréhensibles
- **Exemples** : Cas d'usage concrets

## 🔒 **Sécurité**

### **Validation des Commandes**
- **Whitelist** : Seules les commandes autorisées
- **Validation** : Vérification des entrées utilisateur
- **Audit** : Logs de toutes les opérations

### **Tests de Sécurité**
- **Injection** : Protection contre les injections
- **Chemins** : Validation des chemins de fichiers
- **Permissions** : Vérification des droits d'accès

---

## 🔗 **Liens Rapides**

- **[Guide de Développement](DEVELOPER_GUIDE.md)**
- **[Standards de Code](CODE_STANDARDS.md)**
- **[Tests](TESTING_GUIDE.md)**
- **[Sécurité](SECURITY_GUIDE.md)**

---

*Dernière mise à jour : 21 août 2025*
