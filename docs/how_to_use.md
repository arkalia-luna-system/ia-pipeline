# Arkalia/Athalia – Alias & Boosters Dev

## Alias disponibles

- `ath-chat` : Lancer Continue (Cursor) avec Claude ou Mistral
- `ath-clean` : Nettoyer le projet (`__pycache__`, `.DS_Store`, logs)
- `ath-dev-boost` : Activer les outils IA pour le projet (analyse, prompt, config)
- `ath-perplex` : Ouvrir Perplexity dans le navigateur

## Exemples de prompts à tester

**Claude** :
> Explique-moi ce que fait ce code Python et propose une optimisation.

**Mistral** :
> Génère un script bash pour sauvegarder tous les fichiers .py modifiés aujourd’hui.

## Ajouter un projet (exemple Arkalia Quest)
1. Copier le dossier du jeu dans le workspace
2. Lancer `ath-chat` ou ouvrir Cursor
3. Utiliser Claude ou Mistral pour analyser le code, générer des tests, etc.

---

Pour toute nouvelle commande, ajoute-la dans `setup/alias.sh` et documente-la ici !

## Bonnes pratiques d’intégration dans un projet existant

- Toujours lancer un **scan du projet** avant toute génération (pour éviter les doublons ou l’écrasement)
- Utiliser le **mode dry-run** pour simuler les modifications
- Vérifier les logs et le rapport d’intégration généré
- En cas de fichier déjà existant, préférer la **fusion intelligente** ou le suffixe (_auto)
- Sauvegarder les fichiers critiques avant toute action
- Ne jamais injecter de secrets ou de tokens dans les artefacts générés
- Utiliser l’audit sécurité pour vérifier le code et les dépendances
- En cas de doute, demander confirmation à chaque étape critique

Ces pratiques garantissent une intégration sans risque, sans perte, et en toute confiance, même dans des projets professionnels ou critiques.
