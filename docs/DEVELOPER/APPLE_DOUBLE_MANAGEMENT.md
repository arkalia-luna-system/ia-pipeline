# Gestion des Fichiers AppleDouble dans Athalia

## Qu'est-ce qu'un fichier AppleDouble ?

Les fichiers AppleDouble (préfixés par `._`) sont des fichiers système créés automatiquement par macOS pour stocker les métadonnées des fichiers sur des systèmes de fichiers qui ne supportent pas nativement les attributs étendus de macOS (comme FAT32, NFS, etc.).

## Problème dans le projet Athalia

Dans le projet Athalia, ces fichiers peuvent causer des problèmes :
- Pollution du répertoire de travail
- Confusion lors du développement
- Problèmes de synchronisation avec Git
- Erreurs de linting ou de tests

## Solution : Script ath-clean amélioré

Le script `bin/ath-clean` a été amélioré pour gérer efficacement ces fichiers :

### Fonctionnalités ajoutées

1. **Désactivation automatique** : Le script désactive la création de fichiers AppleDouble sur les volumes réseau et USB
2. **Nettoyage spécifique** : Suppression ciblée des fichiers AppleDouble dans `athalia_core`
3. **Mode forcé** : Option `--force-appledouble` pour une suppression plus agressive
4. **Prévention** : Configuration système pour éviter la recréation

### Utilisation

```bash
# Nettoyage standard
./bin/ath-clean

# Nettoyage avec suppression forcée des AppleDouble
./bin/ath-clean --force-appledouble

# Mode simulation (dry-run)
./bin/ath-clean --dry-run

# Combinaison d'options
./bin/ath-clean --force-appledouble --kill-processes
```

### Options disponibles

- `--dry-run, -d` : Mode simulation (ne supprime rien)
- `--kill-processes, -k` : Arrête tous les processus Athalia
- `--force-appledouble, -f` : Force la suppression des fichiers AppleDouble
- `--help, -h` : Affiche l'aide

## Configuration système

Le script configure automatiquement macOS pour éviter la création de fichiers AppleDouble :

```bash
# Désactiver sur les volumes réseau
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool true

# Désactiver sur les volumes USB
defaults write com.apple.desktopservices DSDontWriteUSBStores -bool true
```

## Gestion manuelle

Si vous devez gérer manuellement ces fichiers :

```bash
# Supprimer tous les fichiers AppleDouble
find . -name "._*" -delete

# Supprimer seulement dans athalia_core
find ./athalia_core -name "._*" -delete

# Vérifier les fichiers AppleDouble
find . -name "._*" | head -10
```

## Recommandations

1. **Exécution régulière** : Lancez `./bin/ath-clean` régulièrement pour maintenir un environnement propre
2. **Avant les commits** : Utilisez le script avant de committer pour éviter de polluer le repository
3. **Configuration permanente** : Les paramètres système sont appliqués automatiquement par le script
4. **Surveillance** : Surveillez l'apparition de nouveaux fichiers AppleDouble

## Dépannage

### Les fichiers réapparaissent après suppression

C'est normal ! macOS recrée automatiquement ces fichiers. Utilisez l'option `--force-appledouble` pour une suppression plus agressive.

### Erreurs de permissions

Si vous obtenez des erreurs de permissions lors de la configuration système, le script continuera le nettoyage mais n'appliquera pas les paramètres de prévention.

### Fichiers importants supprimés par erreur

Le script est conçu pour ne supprimer que les fichiers système et temporaires. Il exclut :
- Le répertoire `.git`
- Les environnements virtuels (`.venv`, `venv`)
- Le répertoire `archive`
- Les `node_modules`

## Intégration avec le workflow de développement

Ajoutez le script à votre workflow de développement :

```bash
# Dans votre .gitignore ou scripts de pré-commit
./bin/ath-clean --force-appledouble

# Ou dans un script de build
./bin/ath-clean && python -m pytest
```

## Support

Pour toute question ou problème lié à la gestion des fichiers AppleDouble, consultez :
- La documentation du script `bin/ath-clean`
- Les logs de nettoyage générés par le script
- La configuration système macOS 