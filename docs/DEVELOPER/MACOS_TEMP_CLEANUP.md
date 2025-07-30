# Nettoyage des Fichiers Temporaires macOS

## Problème

macOS crée automatiquement des fichiers temporaires avec le préfixe `.!` lors de l'édition de fichiers. Ces fichiers peuvent s'accumuler dans votre projet et polluer votre espace de travail.

Exemple de fichiers temporaires :
- `.!49015!test_continue_models.py`
- `.!92030!__init__.py`
- `.!48990!__init__.py`

## Solution

Le projet inclut un script de nettoyage automatique pour supprimer ces fichiers temporaires.

### Script Principal

**Fichier :** `bin/ath-clean-macos-temp`

**Utilisation :**
```bash
# Mode simulation (recommandé)
./bin/ath-clean-macos-temp

# Mode exécution (suppression réelle)
./bin/ath-clean-macos-temp --execute
```

### Alias Disponibles

**Fichier :** `setup/alias-macos-clean.sh`

**Alias :**
- `ath-clean-macos` - Mode simulation
- `ath-clean-macos-exec` - Mode exécution

### Installation des Alias

```bash
source setup/alias-macos-clean.sh
```

## Fonctionnalités

- ✅ **Mode simulation** : Affiche les fichiers qui seraient supprimés sans les toucher
- ✅ **Mode exécution** : Supprime réellement les fichiers avec confirmation
- ✅ **Sécurité** : Demande confirmation avant suppression
- ✅ **Rapport détaillé** : Affiche le nombre de fichiers supprimés
- ✅ **Gestion d'erreurs** : Gère les erreurs de suppression gracieusement

## Utilisation Recommandée

1. **Nettoyage régulier** : Exécutez le script en mode simulation régulièrement
2. **Avant les commits** : Nettoyez avant de committer pour éviter de polluer le repo
3. **Après l'édition** : Nettoyez après avoir édité de nombreux fichiers

## Exemple d'Utilisation

```bash
# Vérifier s'il y a des fichiers temporaires
./bin/ath-clean-macos-temp

# Supprimer les fichiers temporaires
./bin/ath-clean-macos-temp --execute
```

## Intégration avec le Workflow

Ce script peut être intégré dans votre workflow de développement :

1. Ajoutez-le à vos scripts de pré-commit
2. Exécutez-le régulièrement dans votre routine de maintenance
3. Utilisez-le avant les sauvegardes

## Notes Techniques

- Les fichiers temporaires macOS commencent par `.!`
- Ils sont créés automatiquement par le système de fichiers macOS
- Ils ne sont pas nécessaires au fonctionnement du projet
- Leur suppression est sûre et n'affecte pas les fichiers originaux 