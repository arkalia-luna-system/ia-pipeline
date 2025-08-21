# Configuration de Protection des Branches

## 🛡️ **Branches à Protéger**

### **main** (Production)
- ✅ **Require pull request reviews before merging**
- ✅ **Require status checks to pass before merging**
- ✅ **Require branches to be up to date before merging**
- ✅ **Require conversation resolution before merging**
- ✅ **Require signed commits**
- ✅ **Require linear history**
- ✅ **Require deployments to succeed before merging**

### **develop** (Développement)
- ✅ **Require pull request reviews before merging**
- ✅ **Require status checks to pass before merging**
- ✅ **Require branches to be up to date before merging**
- ✅ **Require conversation resolution before merging**

---

## 🔍 **Status Checks Requis**

### **Tests et Qualité**
- `ci-matrix` (tests, lint, coverage)
- `security` (security scan)
- `docs` (documentation build)
- `sbom` (SBOM generation)

### **Couverture de Tests**
- **Minimum**: 80%
- **Recommandé**: 85%
- **Objectif**: 90%

---

## 📋 **Configuration GitHub**

### **Étapes de Configuration**

1. **Aller dans Settings > Branches**
2. **Cliquer sur "Add rule"**
3. **Nommer la branche** (main ou develop)
4. **Configurer les protections** :
   - ✅ Require a pull request before merging
   - ✅ Require approvals (1 minimum)
   - ✅ Require status checks to pass before merging
   - ✅ Require branches to be up to date before merging
   - ✅ Require conversation resolution before merging
   - ✅ Require signed commits (pour main)
   - ✅ Require linear history (pour main)

### **Status Checks à Activer**
- `ci-matrix`
- `security`
- `docs`
- `sbom`

---

## 🚨 **En Cas de Problème**

### **Bypass Temporaire**
- **Admin uniquement** peut bypass temporairement
- **Log obligatoire** de la raison
- **Review post-merge** obligatoire

### **Urgences**
- **Hotfix** : branche temporaire depuis main
- **Merge back** : PR vers develop après correction
- **Tag** : version patch immédiate

---

*Configuration recommandée pour un niveau de sécurité professionnel*
