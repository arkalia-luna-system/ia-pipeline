# 🚀 Guide de Test du Plugin VS Code Athalia

## 📋 Prérequis Vérifiés ✅

- ✅ VS Code installé (version 1.2.4)
- ✅ Plugin compilé (`dist/extension.js` présent)
- ✅ Serveur d'autocomplétion IA démarré (port 8000)
- ✅ Fichiers AppleDouble nettoyés

## 🎯 Étapes de Test

### 1. Ouvrir VS Code
```bash
code .
```

### 2. Aller dans le dossier du plugin
Dans VS Code, ouvrir le dossier : `/Volumes/T7/athalia-dev-setup/athalia-vs-code`

### 3. Lancer le mode développement
**Option A - Raccourci clavier :**
- Appuyer sur `F5`

**Option B - Menu :**
- Aller dans `Exécuter` > `Démarrer le débogage`

**Option C - Palette de commandes :**
- `Cmd+Shift+P` puis taper "Debug: Start Debugging"

### 4. Vérifier l'ouverture de la fenêtre "Extension Development Host"
- Une **nouvelle fenêtre VS Code** devrait s'ouvrir
- Le titre devrait contenir "Extension Development Host"
- Cette fenêtre est **différente** de votre VS Code principal

### 5. Tester les commandes Athalia
Dans la fenêtre "Extension Development Host" :

1. **Ouvrir la palette de commandes :** `Cmd+Shift+P`
2. **Chercher "Athalia"** - vous devriez voir :
   - `Athalia: Autocomplétion IA`
   - `Athalia: Test Activation`

### 6. Tester la commande de test
1. Sélectionner `Athalia: Test Activation`
2. Vous devriez voir : "✅ Extension Athalia activée et fonctionnelle !"

### 7. Tester l'autocomplétion IA
1. Sélectionner `Athalia: Autocomplétion IA`
2. Entrer un texte (ex: "def hello")
3. Choisir une suggestion dans la liste
4. La suggestion devrait être copiée dans le presse-papiers

## 🔧 Diagnostic en cas de problème

### Si la fenêtre "Extension Development Host" ne s'ouvre pas :

1. **Vérifier les logs VS Code :**
   - `Cmd+Shift+P` > "Developer: Toggle Developer Tools"
   - Regarder la console pour les erreurs

2. **Vérifier le fichier de log :**
   ```bash
   cat athalia-vs-code/activation.log
   ```

3. **Réinstaller VS Code :**
   ```bash
   # Désinstaller VS Code
   rm -rf /Applications/Visual\ Studio\ Code.app
   
   # Télécharger et réinstaller depuis https://code.visualstudio.com/
   ```

### Si les commandes n'apparaissent pas :

1. **Vérifier la compilation :**
   ```bash
   cd athalia-vs-code
   npm run compile
   ```

2. **Vérifier le package.json :**
   - Les commandes doivent être dans `contributes.commands`
   - Les activationEvents doivent être corrects

3. **Redémarrer VS Code complètement**

### Si l'autocomplétion ne fonctionne pas :

1. **Vérifier le serveur IA :**
   ```bash
   curl -X POST http://localhost:8000/autocomplete \
     -H "Content-Type: application/json" \
     -d '{"prompt": "test", "max_suggestions": 3}'
   ```

2. **Redémarrer le serveur si nécessaire :**
   ```bash
   # Arrêter le serveur (Ctrl+C)
   # Puis redémarrer :
   python -c "from athalia_core.autocomplete_server import app; import uvicorn; uvicorn.run(app, host='0.0.0.0', port=8000)" &
   ```

## 🎉 Succès !

Si tout fonctionne, vous devriez voir :
- ✅ Fenêtre "Extension Development Host" ouverte
- ✅ Commandes "Athalia" dans la palette
- ✅ Test d'activation qui fonctionne
- ✅ Autocomplétion IA qui retourne des suggestions

## 📞 Support

En cas de problème persistant :
1. Vérifier les logs VS Code (Developer Tools)
2. Vérifier le fichier `activation.log`
3. Tester sur un autre Mac/utilisateur
4. Réinstaller VS Code proprement

---

**🚀 Une fois que cela fonctionne, nous pourrons continuer le développement des fonctionnalités avancées !** 