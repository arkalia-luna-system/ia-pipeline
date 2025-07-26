# Guide de dépannage Athalia

## Problèmes d'API et crédits

### Erreur "credit balance is too low"

**Symptôme :**
```
WARNING:root:Crédits API insuffisants - utilisation du mode mock
```

**Solutions :**

1. **Recharger les crédits Anthropic**
   - Allez sur [Anthropic Console](https://console.anthropic.com/)
   - Section "Plans & Billing"
   - Achetez des crédits ou mettez à jour votre plan

2. **Utiliser le mode mock (temporaire)**
   - Le pipeline fonctionne en mode dégradé
   - Génération de projets basiques mais fonctionnels
   - Pas d'IA avancée mais structure complète

3. **Configurer une API alternative**
   ```bash
   export CONTINUE_URL="http://localhost:65432/v1/chat"
   export CONTINUE_MODEL="claude-3-sonnet-20240229"
   ```

### Abonnements Anthropic - Clarification

**Abonnement de base (20€/mois) :**
- ✅ Inclut des crédits mensuels
- ✅ Accès à Claude 3.5 Sonnet
- ✅ API disponible
- ❌ Crédits limités (peuvent s'épuiser)

**Alternatives gratuites :**
- **Continue (local)** : Utilise Claude localement sans coût
- **Ollama** : Modèles open source gratuits
- **Hugging Face** : Modèles gratuits avec limitations

**Configuration Continue (recommandée) :**
```bash
# Installer Continue
curl -L https://continue.dev/install.sh | sh

# Démarrer le serveur
continue start

# Configurer Athalia
export CONTINUE_URL="http://localhost:65432/v1/chat"
export CONTINUE_MODEL="claude-3-sonnet-20240229"
```

### Erreur de connexion API

**Symptôme :**
```
WARNING:root:Connexion API impossible
```

**Solutions :**

1. **Vérifier la connectivité**
   ```bash
   curl -X POST http://localhost:65432/v1/chat
   ```

2. **Redémarrer le service Continue**
   ```bash
   # Si vous utilisez Continue
   continue restart
   ```

3. **Vérifier les variables d'environnement**
   ```bash
   echo $CONTINUE_URL
   echo $CONTINE_MODEL
   ```

## Problèmes de génération

### Fichiers YAML invalides

**Symptôme :**
```
mapping values are not allowed here
```

**Solutions :**

1. **Nettoyer les caractères invisibles**
   ```bash
   find . -name "*.yaml" -exec sed -i '' 's/[[:space:]]*$//' {} \;
   ```

2. **Valider le YAML**
   ```bash
   python3 -c "import yaml; yaml.safe_load(open('openapi.yaml'))"
   ```

3. **Régénérer le projet**
   ```bash
   python3 -m athalia_core.main
   # Option 1 pour régénérer
   ```

### Tests qui échouent

**Symptôme :**
```
pytest: command not found
```

**Solutions :**

1. **Installer pytest**
   ```bash
   pip install pytest
   ```

2. **Vérifier les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

3. **Lancer les tests manuellement**
   ```bash
   cd ia_project
   python -m pytest tests/
   ```

## Problèmes de structure

### Fichiers cachés macOS

**Symptôme :**
```
._blueprint.yaml
._DOC.md
```

**Solutions :**

1. **Nettoyer automatiquement**
   ```bash
   find . -name "._*" -delete
   ```

2. **Prévenir avec .gitignore**
   ```bash
   # Déjà configuré dans .gitignore
   ```

3. **Utiliser rsync pour copier**
   ```bash
   rsync -av --exclude='._*' source/ destination/
   ```

## Mode dégradé

Quand l'API n'est pas disponible, Athalia utilise le **mode mock** :

- ✅ Génération de structure complète
- ✅ Tests unitaires
- ✅ Documentation technique
- ✅ CI/CD
- ❌ Pas d'IA avancée
- ❌ Pas de personnalisation poussée

**Pour revenir au mode IA complet :**
1. Rechargez vos crédits Anthropic
2. Vérifiez la connectivité API
3. Régénérez votre projet

## Solutions recommandées par ordre de priorité

1. **Continue (gratuit)** : Installation locale, pas de coût
2. **Abonnement Anthropic** : Si vous voulez l'API cloud
3. **Mode mock** : Fonctionne déjà, pas de coût

---

*Guide mis à jour le 2024-06-27* 