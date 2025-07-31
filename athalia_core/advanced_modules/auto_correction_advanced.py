#!/usr/bin/env python3
"""
Module d'auto-correction avancée pour Athalia
Correction intelligente de code, suggestions d'amélioration, refactoring automatique
"""

import ast
import logging
from pathlib import Path
import re
from typing import Any, Dict, List, Tuple


logger = logging.getLogger(__name__)


class AutoCorrectionAvancee:
    """Module d'auto-correction avancée avec correction intelligente"""

    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.corrections_appliquees: List[Dict[str, Any]] = []
        self.suggestions: List[str] = []

    def analyser_et_corriger(self, dry_run: bool = False) -> Dict[str, Any]:
        """Analyse complète et correction automatique du code"""
        logger.info("🔧 Démarrage de l'auto-correction avancée")

        resultats = {
            "corrections_appliquees": [],
            "suggestions": [],
            "fichiers_traites": 0,
            "erreurs_corrigees": 0,
        }

        # 1. Correction syntaxique avancée
        resultats.update(self._corriger_syntaxe_avancee(dry_run))

        # 2. Optimisation de code
        resultats.update(self._optimiser_code(dry_run))

        # 3. Refactoring automatique
        resultats.update(self._refactoring_automatique(dry_run))

        # 4. Correction de patterns anti-patterns
        resultats.update(self._corriger_anti_patterns(dry_run))

        # 5. Amélioration de la lisibilité
        resultats.update(self._ameliorer_lisibilite(dry_run))

        corrections_appliquees = resultats.get("corrections_appliquees", [])
        if not isinstance(corrections_appliquees, list):
            corrections_appliquees = []
        corrections_count = len(corrections_appliquees)
        logger.info(
            f"✅ Auto-correction terminée: {corrections_count} corrections appliquées"
        )
        retour = resultats.copy()
        retour["resultats"] = resultats
        return retour

    def _corriger_syntaxe_avancee(self, dry_run: bool) -> Dict[str, Any]:
        """Correction syntaxique avancée avec analyse AST"""
        corrections = []
        fichiers_traites = 0
        erreurs_corrigees = 0

        for fichier in self.project_path.rglob("*.py"):
            # Ignorer les fichiers macOS ._*
            if fichier.name.startswith("._"):
                continue

            if "__pycache__" in str(fichier) or ".git" in str(fichier):
                continue

            try:
                with open(fichier, "r", encoding="utf-8") as f:
                    contenu = f.read()

                # Analyse AST pour détecter les erreurs
                try:
                    ast.parse(contenu)
                except SyntaxError as e:
                    correction = self._corriger_erreur_syntaxe(fichier, contenu, e)
                    if correction and not dry_run:
                        with open(fichier, "w", encoding="utf-8") as f:
                            f.write(correction["nouveau_contenu"])
                        corrections.append(correction)
                        erreurs_corrigees += 1
                    elif correction:
                        corrections.append(correction)
                        erreurs_corrigees += 1

                fichiers_traites += 1

            except Exception as e:
                logger.warning(f"Erreur lors de l'analyse de {fichier}: {e}")

        return {
            "corrections_appliquees": corrections,
            "fichiers_traites": fichiers_traites,
            "erreurs_corrigees": erreurs_corrigees,
        }

    def _corriger_erreur_syntaxe(
        self, fichier: Path, contenu: str, erreur: SyntaxError
    ) -> Dict[str, Any]:
        """Correction intelligente d'erreur de syntaxe"""
        lignes = contenu.split("\n")
        ligne_erreur = (erreur.lineno or 1) - 1

        # Corrections communes
        corrections = {
            "indentation": self._corriger_indentation,
            "parentheses": self._corriger_parentheses,
            "guillemets": self._corriger_guillemets,
            "virgules": self._corriger_virgules,
        }

        for type_correction, fonction in corrections.items():
            try:
                nouveau_contenu = fonction(lignes, ligne_erreur)
                if nouveau_contenu:
                    return {
                        "fichier": str(fichier),
                        "type": f"syntaxe_{type_correction}",
                        "ligne": ligne_erreur + 1,
                        "ancien_contenu": lignes[ligne_erreur],
                        "nouveau_contenu": nouveau_contenu,
                        "erreur_originale": lignes[ligne_erreur],
                        "description": f"Correction {type_correction} automatique",
                    }
            except Exception:
                continue

        return {}  # type: ignore

    def _corriger_indentation(self, lignes: List[str], ligne_erreur: int) -> str:
        """Correction automatique de l'indentation"""
        ligne = lignes[ligne_erreur]

        # Détection de l'indentation incorrecte
        if ligne.strip() and not ligne.startswith(" ") and not ligne.startswith("\t"):
            # Ajout d'indentation basée sur le contexte
            if ligne_erreur > 0:
                ligne_precedente = lignes[ligne_erreur - 1]
                if ligne_precedente.strip().endswith(":"):
                    return "    " + ligne
                elif ligne_precedente.strip().startswith(
                    "def "
                ) or ligne_precedente.strip().startswith("class "):
                    return "    " + ligne

        return ""  # type: ignore

    def _corriger_parentheses(self, lignes: List[str], ligne_erreur: int) -> str:
        """Correction automatique des parenthèses"""
        ligne = lignes[ligne_erreur]

        # Comptage des parenthèses
        ouvrantes = ligne.count("(") + ligne.count("[") + ligne.count("{")
        fermantes = ligne.count(")") + ligne.count("]") + ligne.count("}")

        if ouvrantes > fermantes:
            return ligne + ")" * (ouvrantes - fermantes)
        elif fermantes > ouvrantes:
            return "(" * (fermantes - ouvrantes) + ligne

        return ""  # type: ignore

    def _corriger_guillemets(self, lignes: List[str], ligne_erreur: int) -> str:
        """Correction automatique des guillemets"""
        ligne = lignes[ligne_erreur]

        # Correction des guillemets non fermés
        if ligne.count('"') % 2 == 1:
            return ligne + '"'
        elif ligne.count("'") % 2 == 1:
            return ligne + "'"

        return ""  # type: ignore

    def _corriger_virgules(self, lignes: List[str], ligne_erreur: int) -> str:
        """Correction automatique des virgules manquantes"""
        ligne = lignes[ligne_erreur]

        # Ajout de virgule manquante dans les listes/dicts
        if re.search(r"[a-zA-Z0-9_]+$", ligne.strip()):
            if ligne_erreur + 1 < len(lignes):
                ligne_suivante = lignes[ligne_erreur + 1]
                if ligne_suivante.strip().startswith(
                    "["
                ) or ligne_suivante.strip().startswith("{"):
                    return ligne.rstrip() + ","

        return ""  # type: ignore

    def _optimiser_code(self, dry_run: bool) -> Dict[str, Any]:
        """Optimisation automatique du code"""
        optimisations = []
        fichiers_traites = 0
        erreurs_corrigees = 0

        for fichier in self.project_path.rglob("*.py"):
            # Ignorer les fichiers macOS ._*
            if fichier.name.startswith("._"):
                continue

            if "__pycache__" in str(fichier) or ".git" in str(fichier):
                continue

            try:
                with open(fichier, "r", encoding="utf-8") as f:
                    contenu = f.read()

                nouveau_contenu = contenu

                # Optimisations
                optimisations_fichier = []

                # 1. Remplacement de list comprehensions par générateurs
                nouveau_contenu, optims = self._optimiser_list_comprehensions(
                    nouveau_contenu
                )
                optimisations_fichier.extend(optims)

                # 2. Optimisation des imports
                nouveau_contenu, optims = self._optimiser_imports(nouveau_contenu)
                optimisations_fichier.extend(optims)

                # 3. Optimisation des boucles
                nouveau_contenu, optims = self._optimiser_boucles(nouveau_contenu)
                optimisations_fichier.extend(optims)

                if optimisations_fichier and not dry_run:
                    with open(fichier, "w", encoding="utf-8") as f:
                        f.write(nouveau_contenu)

                optimisations.extend(optimisations_fichier)
                if optimisations_fichier:
                    erreurs_corrigees += len(optimisations_fichier)
                fichiers_traites += 1

            except Exception as e:
                logger.warning(f"Erreur lors de l'optimisation de {fichier}: {e}")

        return {
            "corrections_appliquees": optimisations,
            "fichiers_traites": fichiers_traites,
            "erreurs_corrigees": erreurs_corrigees,
        }

    def _optimiser_list_comprehensions(self, contenu: str) -> Tuple[str, List[Dict]]:
        """Optimisation des list comprehensions"""
        optimisations = []

        # Remplacer [x for x in y] par (x for x in y) quand possible
        pattern = r"\[([^\[\]]+for[^\[\]]+)\]"
        matches = re.finditer(pattern, contenu)

        for match in matches:
            expression = match.group(1)
            if "if" not in expression:  # Pas de condition
                nouveau = f"({expression})"
                contenu = contenu.replace(match.group(0), nouveau)
                optimisations.append(
                    {
                        "type": "optimisation",
                        "ancien": match.group(0),
                        "nouveau": nouveau,
                    }
                )

        return contenu, optimisations

    def _optimiser_imports(self, contenu: str) -> Tuple[str, List[Dict]]:
        """Optimisation des imports"""
        optimisations = []

        # Regrouper les imports
        lines = contenu.split("\n")
        import_lines = []
        other_lines = []

        for line in lines:
            if line.strip().startswith(("import ", "from ")):
                import_lines.append(line)
            else:
                other_lines.append(line)

        if len(import_lines) > 1:
            # Regrouper par type
            stdlib_imports = []
            third_party_imports = []
            local_imports = []

            for imp in import_lines:
                if any(pkg in imp for pkg in ["os", "sys", "json", "re", "pathlib"]):
                    stdlib_imports.append(imp)
                elif any(pkg in imp for pkg in ["numpy", "pandas", "requests"]):
                    third_party_imports.append(imp)
                else:
                    local_imports.append(imp)

            # Réorganiser
            new_imports = (
                stdlib_imports + [""] + third_party_imports + [""] + local_imports
            )
            optimisations.append(
                {
                    "type": "optimisation",
                    "description": "Imports regroupés par catégorie",
                }
            )

            return "\n".join(new_imports + other_lines), optimisations

        return contenu, optimisations

    def _optimiser_boucles(self, contenu: str) -> Tuple[str, List[Dict]]:
        """Optimisation des boucles"""
        optimisations = []

        # Remplacer for i in range(len(x)) par for i, item in enumerate(x)
        pattern = r"for\s+(\w+)\s+in\s+range\(len\(([^)]+)\)\):"
        matches = re.finditer(pattern, contenu)

        for match in matches:
            index_var = match.group(1)
            list_var = match.group(2)
            nouveau = f"for {index_var}, item in enumerate({list_var}):"
            contenu = contenu.replace(match.group(0), nouveau)
            optimisations.append(
                {
                    "type": "optimisation",
                    "ancien": match.group(0),
                    "nouveau": nouveau,
                }
            )

        return contenu, optimisations

    def _refactoring_automatique(self, dry_run: bool) -> Dict[str, Any]:
        """Refactoring automatique du code"""
        refactorings = []
        fichiers_traites = 0
        erreurs_corrigees = 0

        for fichier in self.project_path.rglob("*.py"):
            # Ignorer les fichiers macOS ._*
            if fichier.name.startswith("._"):
                continue

            if "__pycache__" in str(fichier) or ".git" in str(fichier):
                continue

            try:
                with open(fichier, "r", encoding="utf-8") as f:
                    contenu = f.read()

                nouveau_contenu = contenu

                # Refactorings
                refactorings_fichier = []

                # 1. Extraction de méthodes
                nouveau_contenu, refs = self._extraire_methodes(nouveau_contenu)
                refactorings_fichier.extend(refs)

                # 2. Renommage de variables
                nouveau_contenu, refs = self._renommer_variables(nouveau_contenu)
                refactorings_fichier.extend(refs)

                # 3. Simplification de conditions
                nouveau_contenu, refs = self._simplifier_conditions(nouveau_contenu)
                refactorings_fichier.extend(refs)

                if refactorings_fichier and not dry_run:
                    with open(fichier, "w", encoding="utf-8") as f:
                        f.write(nouveau_contenu)

                refactorings.extend(refactorings_fichier)
                if refactorings_fichier:
                    erreurs_corrigees += len(refactorings_fichier)
                fichiers_traites += 1

            except Exception as e:
                logger.warning(f"Erreur lors du refactoring de {fichier}: {e}")

        return {
            "corrections_appliquees": refactorings,
            "fichiers_traites": fichiers_traites,
            "erreurs_corrigees": erreurs_corrigees,
        }

    def _extraire_methodes(self, contenu: str) -> Tuple[str, List[Dict]]:
        """Extraction automatique de méthodes"""
        refactorings = []

        # Détecter les blocs de code répétitifs
        lines = contenu.split("\n")
        i = 0
        while i < len(lines):
            line = lines[i].strip()

            # Détecter les blocs de plus de 5 lignes
            if line.startswith("def ") or line.startswith("class "):
                # Compter les lignes du bloc
                j = i + 1
                indent_level = len(lines[i]) - len(lines[i].lstrip())

                while j < len(lines):
                    if (
                        lines[j].strip()
                        and len(lines[j]) - len(lines[j].lstrip()) <= indent_level
                    ):
                        break
                    j += 1

                block_size = j - i
                if block_size > 10:  # Bloc trop long
                    refactorings.append(
                        {
                            "type": "refactoring",
                            "description": f"Méthode de {block_size} lignes détectée",
                            "ligne": i + 1,
                        }
                    )

                i = j
            else:
                i += 1

        return contenu, refactorings

    def _renommer_variables(self, contenu: str) -> Tuple[str, List[Dict]]:
        """Renommage automatique de variables"""
        refactorings = []

        # Détecter les variables avec des noms non descriptifs
        patterns = [
            (r"\b([a-z])\b", "Variable à une lettre"),
            (r"\b(x|y|z)\b", "Variable mathématique"),
            (r"\b(temp|tmp)\b", "Variable temporaire"),
        ]

        for pattern, description in patterns:
            matches = re.finditer(pattern, contenu)
            for match in matches:
                var_name = match.group(1)
                refactorings.append(
                    {
                        "type": "refactoring",
                        "variable": var_name,
                        "suggestion": f"renommer {var_name} en nom plus descriptif",
                        "description": description,
                    }
                )

        return contenu, refactorings

    def _simplifier_conditions(self, contenu: str) -> Tuple[str, List[Dict]]:
        """Simplification automatique de conditions"""
        refactorings = []

        # Simplifier if x == True par if x
        pattern = r"if\s+([^:]+)\s*==\s*True\s*:"
        matches = re.finditer(pattern, contenu)

        for match in matches:
            condition = match.group(1).strip()
            nouveau = f"if {condition}:"
            contenu = contenu.replace(match.group(0), nouveau)
            refactorings.append(
                {
                    "type": "refactoring",
                    "ancien": match.group(0),
                    "nouveau": nouveau,
                }
            )

        return contenu, refactorings

    def _corriger_anti_patterns(self, dry_run: bool) -> Dict[str, Any]:
        """Correction des anti-patterns"""
        corrections = []
        fichiers_traites = 0
        erreurs_corrigees = 0

        for fichier in self.project_path.rglob("*.py"):
            # Ignorer les fichiers macOS ._*
            if fichier.name.startswith("._"):
                continue

            if "__pycache__" in str(fichier) or ".git" in str(fichier):
                continue

            try:
                with open(fichier, "r", encoding="utf-8") as f:
                    contenu = f.read()

                corrections_fichier = []

                # Anti-patterns à corriger
                anti_patterns = [
                    (
                        r"except\s*:",
                        "except Exception:",
                        "Exception trop générique",
                    ),
                    (r"print\s*\(", "logging.info(", "Utilisation de print()"),
                    (
                        r"os\.system\s*\(",
                        "subprocess.run(",
                        "Appel shell non sécurisé",
                    ),
                    (r"import \*", "import spécifique", "Import wildcard"),
                ]

                for pattern, replacement, description in anti_patterns:
                    if re.search(pattern, contenu):
                        corrections_fichier.append(
                            {
                                "type": "anti_pattern",
                                "pattern": pattern,
                                "description": description,
                            }
                        )

                corrections.extend(corrections_fichier)
                if corrections_fichier:
                    erreurs_corrigees += len(corrections_fichier)
                fichiers_traites += 1

            except Exception as e:
                logger.warning(
                    f"Erreur lors de la correction d'anti-patterns de {fichier}: {e}"
                )

        return {
            "corrections_appliquees": corrections,
            "fichiers_traites": fichiers_traites,
            "erreurs_corrigees": erreurs_corrigees,
        }

    def _ameliorer_lisibilite(self, dry_run: bool) -> Dict[str, Any]:
        """Amélioration de la lisibilité"""
        ameliorations = []
        fichiers_traites = 0
        erreurs_corrigees = 0

        for fichier in self.project_path.rglob("*.py"):
            # Ignorer les fichiers macOS ._*
            if fichier.name.startswith("._"):
                continue

            if "__pycache__" in str(fichier) or ".git" in str(fichier):
                continue

            try:
                with open(fichier, "r", encoding="utf-8") as f:
                    contenu = f.read()

                ameliorations_fichier = []

                # Améliorations de lisibilité
                lines = contenu.split("\n")

                # 1. Ajouter des docstrings manquantes
                for i, line in enumerate(lines):
                    if line.strip().startswith("def ") and i + 1 < len(lines):
                        next_line = lines[i + 1].strip()
                        if not next_line.startswith('"""') and not next_line.startswith(
                            "'''"
                        ):
                            ameliorations_fichier.append(
                                {
                                    "type": "lisibilite",
                                    "ligne": i + 1,
                                    "description": "Fonction sans docstring",
                                }
                            )

                # 2. Détecter les lignes trop longues
                for i, line in enumerate(lines):
                    if len(line) > 120:
                        ameliorations_fichier.append(
                            {
                                "type": "lisibilite",
                                "ligne": i + 1,
                                "description": f"Ligne de {len(line)} caractères",
                            }
                        )

                ameliorations.extend(ameliorations_fichier)
                if ameliorations_fichier:
                    erreurs_corrigees += len(ameliorations_fichier)
                fichiers_traites += 1

            except Exception as e:
                logger.warning(f"Erreur lors de l'amélioration de {fichier}: {e}")

        return {
            "corrections_appliquees": ameliorations,
            "fichiers_traites": fichiers_traites,
            "erreurs_corrigees": erreurs_corrigees,
        }

    def generer_rapport(self, resultats: Dict[str, Any]) -> str:
        """Génération d'un rapport détaillé"""
        rapport = """
Rapport d'Auto-Correction
========================
"""
        rapport += f"\n📊 RAPPORT D'AUTO-CORRECTION - {self.project_path}\n"
        rapport += f"{'=' * 60}\n\n"

        # Utiliser le dictionnaire 'resultats' pour générer le rapport
        corrections_appliquees = resultats.get("corrections_appliquees", [])
        suggestions = resultats.get("suggestions", [])
        fichiers_traites = resultats.get("fichiers_traites", 0)
        erreurs_corrigees = resultats.get("erreurs_corrigees", 0)

        rapport += "🔧 CORRECTIONS APPLIQUÉES:\n"
        if corrections_appliquees:
            for i, correction in enumerate(corrections_appliquees, 1):
                rapport += (
                    f"{i}. {correction.get('type', 'N/A')} - "
                    f"{correction.get('description', 'N/A')}\n"
                )
        else:
            rapport += "Aucune correction appliquée\n"

        rapport += "\n💡 SUGGESTIONS:\n"
        if suggestions:
            for i, suggestion in enumerate(suggestions, 1):
                rapport += f"{i}. {suggestion}\n"
        else:
            rapport += "Aucune suggestion\n"

        rapport += "\n📈 STATISTIQUES:\n"
        rapport += f"- Fichiers traités: {fichiers_traites}\n"
        rapport += f"- Erreurs corrigées: {erreurs_corrigees}\n"
        rapport += f"- Corrections appliquées: {len(corrections_appliquees)}\n"

        return rapport


def main():
    """Fonction principale pour test"""
    import argparse

    parser = argparse.ArgumentParser(description="Auto-correction avancée pour Athalia")
    parser.add_argument("project_path", help="Chemin du projet à corriger")
    parser.add_argument("--dry-run", action="store_true", help="Mode simulation")

    args = parser.parse_args()

    corrector = AutoCorrectionAvancee(args.project_path)
    resultats = corrector.analyser_et_corriger(dry_run=args.dry_run)

    print(corrector.generer_rapport(resultats))


if __name__ == "__main__":
    main()
