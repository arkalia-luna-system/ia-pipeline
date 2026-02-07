# Style de la documentation

Règles pour garder les `.md` **professionnels**, **cohérents** et lisibles en thème clair ou sombre.

## Principes

- **Titres** : courts, sans emojis en excès. Un emoji par section principale acceptable.
- **Corps** : phrases courtes, listes à puces pour les énumérations.
- **Liens** : relatifs (`[Texte](path/to/file.md)`), vérifier qu’ils ciblent des fichiers existants.
- **Pas de doublon** : un seul document “source” par sujet (ex. installation → USER_GUIDES/INSTALLATION.md). Les autres renvoient vers lui.
- **Thème sombre** : éviter les blocs de code ou diagrammes qui supposent un fond clair uniquement. Les diagrammes Mermaid s’adaptent au thème MkDocs.

## Structure type

1. Titre (H1)
2. Ligne de métadonnées optionnelle (date, statut)
3. Résumé en 1–2 phrases
4. `---`
5. Sections H2/H3 avec contenu
6. Références / liens en fin de document

Template minimal : [DEVELOPER/TEMPLATE_STANDARD_MARKDOWN.md](DEVELOPER/TEMPLATE_STANDARD_MARKDOWN.md).

## MkDocs

Le site est généré avec **Material** ; le thème **sombre (slate)** est utilisé lorsque la préférence système est “dark”. Consulter [config/mkdocs/mkdocs.yml](../config/mkdocs/mkdocs.yml) pour la palette.

---

*Documentation Athalia*
