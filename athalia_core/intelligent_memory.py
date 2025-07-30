#!/usr/bin/env python3
"""
🧠 MÉMOIRE INTELLIGENTE ATHALIA
===============================
Système de mémoire qui :
- Apprend de chaque erreur et correction
- Prédit les problèmes futurs
- Suggère des corrections automatiques
- Maintient un historique d'apprentissage
- Améliore la qualité du code continuellement
"""

import difflib
import hashlib
import json
import logging
import re
import sqlite3
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


@dataclass
class LearningEvent:
    """Événement d'apprentissage"""

    event_type: str  # 'error', 'correction', 'pattern', 'duplicate'
    description: str
    code_snippet: str
    location: str
    timestamp: datetime
    severity: str  # 'low', 'medium', 'high', 'critical'
    resolution: Optional[str] = None
    success: bool = True
    context: Dict[str, Any] = None


@dataclass
class Prediction:
    """Prédiction basée sur l'apprentissage"""

    prediction_type: str  # 'error', 'duplicate', 'optimization'
    confidence: float  # 0.0 - 1.0
    description: str
    suggested_action: str
    estimated_impact: str
    code_pattern: str


@dataclass
class CorrectionSuggestion:
    """Suggestion de correction"""

    original_code: str
    suggested_code: str
    reason: str
    confidence: float
    based_on_previous_corrections: List[str]


class IntelligentMemory:
    """Système de mémoire intelligente pour Athalia"""

    def __init__(self, root_path: str = None):
        self.root_path = Path(root_path or Path.cwd())
        self.db_path = self.root_path / "data" / "intelligent_memory.db"
        self.memory_file = self.root_path / "data" / "memory_insights.json"

        # Créer les dossiers nécessaires
        self.db_path.parent.mkdir(parents=True, exist_ok=True)

        # Initialiser la base de données
        self._init_database()

        # Cache pour les performances
        self._pattern_cache = {}
        self._prediction_cache = {}
        self._correction_cache = {}

        logger.info(f"🧠 Intelligent Memory initialisé dans {self.root_path}")

    def _init_database(self):
        """Initialiser la base de données de mémoire"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Table des événements d'apprentissage
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS learning_events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    event_type TEXT NOT NULL,
                    description TEXT NOT NULL,
                    code_snippet TEXT NOT NULL,
                    location TEXT NOT NULL,
                    timestamp TEXT NOT NULL,
                    severity TEXT NOT NULL,
                    resolution TEXT,
                    success BOOLEAN DEFAULT 1,
                    context TEXT,
                    pattern_hash TEXT
                )
            """
            )

            # Table des patterns appris
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS learned_patterns (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    pattern_hash TEXT UNIQUE NOT NULL,
                    pattern_type TEXT NOT NULL,
                    occurrences INTEGER DEFAULT 1,
                    first_seen TEXT NOT NULL,
                    last_seen TEXT NOT NULL,
                    success_rate REAL DEFAULT 1.0,
                    correction_history TEXT
                )
            """
            )

            # Table des prédictions
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS predictions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    prediction_type TEXT NOT NULL,
                    confidence REAL NOT NULL,
                    description TEXT NOT NULL,
                    suggested_action TEXT NOT NULL,
                    estimated_impact TEXT NOT NULL,
                    code_pattern TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    validated BOOLEAN DEFAULT 0,
                    validation_result TEXT
                )
            """
            )

            # Table des corrections suggérées
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS correction_suggestions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    original_code TEXT NOT NULL,
                    suggested_code TEXT NOT NULL,
                    reason TEXT NOT NULL,
                    confidence REAL NOT NULL,
                    based_on_corrections TEXT,
                    created_at TEXT NOT NULL,
                    applied BOOLEAN DEFAULT 0,
                    applied_at TEXT,
                    success BOOLEAN
                )
            """
            )

            # Table des métriques d'apprentissage
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS learning_metrics (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    metric_name TEXT NOT NULL,
                    metric_value REAL NOT NULL,
                    timestamp TEXT NOT NULL,
                    context TEXT
                )
            """
            )

            conn.commit()

    def learn_from_error(
        self,
        error_description: str,
        code_snippet: str,
        location: str,
        severity: str = "medium",
        context: Dict[str, Any] = None,
    ) -> str:
        """Apprendre d'une erreur"""
        event_id = self._record_learning_event(
            event_type="error",
            description=error_description,
            code_snippet=code_snippet,
            location=location,
            severity=severity,
            success=False,
            context=context,
        )

        # Analyser le pattern de l'erreur
        pattern_hash = self._analyze_code_pattern(code_snippet)
        self._update_pattern_learning(pattern_hash, "error", success=False)

        # Générer des prédictions basées sur cette erreur
        self._generate_predictions_from_error(
            error_description, code_snippet, pattern_hash
        )

        logger.info(f"📚 Apprentissage d'une erreur: {error_description}")
        return event_id

    def learn_from_correction(
        self,
        original_code: str,
        corrected_code: str,
        reason: str,
        location: str,
        success: bool = True,
        context: Dict[str, Any] = None,
    ) -> str:
        """Apprendre d'une correction"""
        event_id = self._record_learning_event(
            event_type="correction",
            description=f"Correction: {reason}",
            code_snippet=f"Original: {original_code}\nCorrected: {corrected_code}",
            location=location,
            severity="medium",
            resolution=corrected_code,
            success=success,
            context=context,
        )

        # Analyser les patterns
        original_pattern = self._analyze_code_pattern(original_code)
        corrected_pattern = self._analyze_code_pattern(corrected_code)

        # Mettre à jour l'apprentissage des patterns
        self._update_pattern_learning(original_pattern, "correction", success=False)
        self._update_pattern_learning(corrected_pattern, "correction", success=success)

        # Sauvegarder la suggestion de correction
        self._save_correction_suggestion(original_code, corrected_code, reason, success)

        logger.info(f"📚 Apprentissage d'une correction: {reason}")
        return event_id

    def learn_from_duplicate(
        self,
        duplicate_items: List[str],
        locations: List[str],
        similarity_score: float,
        context: Dict[str, Any] = None,
    ) -> str:
        """Apprendre d'un doublon détecté"""
        event_id = self._record_learning_event(
            event_type="duplicate",
            description=f"Doublon détecté (similarité: {similarity_score:.2f})",
            code_snippet=f"Items: {', '.join(duplicate_items)}",
            location=f"Locations: {', '.join(locations)}",
            severity="high" if similarity_score > 0.9 else "medium",
            success=False,
            context=context,
        )

        # Analyser le pattern du doublon
        for item in duplicate_items:
            pattern_hash = self._analyze_code_pattern(item)
            self._update_pattern_learning(pattern_hash, "duplicate", success=False)

        logger.info(f"📚 Apprentissage d'un doublon: {len(duplicate_items)} items")
        return event_id

    def predict_issues(
        self, code_snippet: str, context: Dict[str, Any] = None
    ) -> List[Prediction]:
        """Prédire les problèmes potentiels"""
        predictions = []

        # Analyser le pattern du code
        pattern_hash = self._analyze_code_pattern(code_snippet)

        # Chercher des patterns similaires dans l'historique
        similar_patterns = self._find_similar_patterns(pattern_hash)

        for pattern in similar_patterns:
            if pattern["success_rate"] < 0.7:  # Pattern problématique
                prediction = Prediction(
                    prediction_type="error",
                    confidence=1.0 - pattern["success_rate"],
                    description=(
                        f"Pattern similaire à un problème précédent "
                        f"(taux de succès: {pattern['success_rate']:.2f})"
                    ),
                    suggested_action="Vérifier la logique et considérer une refactorisation",
                    estimated_impact="Moyen",
                    code_pattern=pattern_hash,
                )
                predictions.append(prediction)

        # Vérifier les anti-patterns connus
        antipattern_predictions = self._check_antipatterns(code_snippet)
        predictions.extend(antipattern_predictions)

        # Vérifier les doublons potentiels
        duplicate_predictions = self._check_potential_duplicates(code_snippet)
        predictions.extend(duplicate_predictions)

        return predictions

    def suggest_corrections(
        self, problematic_code: str, issue_description: str
    ) -> List[CorrectionSuggestion]:
        """Suggérer des corrections basées sur l'apprentissage"""
        suggestions = []

        # Chercher des corrections similaires dans l'historique
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT original_code, suggested_code, reason, confidence, based_on_corrections
                FROM correction_suggestions
                WHERE applied = 1 AND success = 1
                ORDER BY confidence DESC
                LIMIT 5
            """
            )

            rows = cursor.fetchall()

            for row in rows:
                original, suggested, reason, confidence, based_on = row

                # Calculer la similarité avec le code problématique
                similarity = self._calculate_code_similarity(problematic_code, original)

                if similarity > 0.7:  # Seuil de similarité
                    suggestion = CorrectionSuggestion(
                        original_code=problematic_code,
                        suggested_code=suggested,
                        reason=f"Basé sur une correction similaire: {reason}",
                        confidence=confidence * similarity,
                        based_on_previous_corrections=(
                            json.loads(based_on) if based_on else []
                        ),
                    )
                    suggestions.append(suggestion)

        return suggestions

    def get_learning_insights(self) -> Dict[str, Any]:
        """Obtenir des insights d'apprentissage"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Statistiques générales
            cursor.execute("SELECT COUNT(*) FROM learning_events")
            total_events = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM learning_events WHERE success = 0")
            total_errors = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM learning_events WHERE success = 1")
            total_successes = cursor.fetchone()[0]

            # Patterns appris
            cursor.execute("SELECT COUNT(*) FROM learned_patterns")
            total_patterns = cursor.fetchone()[0]

            # Prédictions
            cursor.execute("SELECT COUNT(*) FROM predictions")
            total_predictions = cursor.fetchone()[0]

            # Corrections suggérées
            cursor.execute("SELECT COUNT(*) FROM correction_suggestions")
            total_corrections = cursor.fetchone()[0]

            # Calculer les taux de succès
            error_rate = total_errors / total_events if total_events > 0 else 0

            return {
                "total_events": total_events,
                "total_errors": total_errors,
                "total_successes": total_successes,
                "error_rate": error_rate,
                "total_patterns": total_patterns,
                "total_predictions": total_predictions,
                "total_corrections": total_corrections,
                "learning_progress": "Système d'apprentissage actif",
            }

    def _record_learning_event(
        self,
        event_type: str,
        description: str,
        code_snippet: str,
        location: str,
        severity: str,
        success: bool = True,
        resolution: str = None,
        context: Dict[str, Any] = None,
    ) -> str:
        """Enregistrer un événement d'apprentissage"""
        pattern_hash = self._analyze_code_pattern(code_snippet)

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO learning_events
                (event_type, description, code_snippet, location, timestamp,
                 severity, resolution, success, context, pattern_hash)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    event_type,
                    description,
                    code_snippet,
                    location,
                    datetime.now().isoformat(),
                    severity,
                    resolution,
                    success,
                    json.dumps(context) if context else None,
                    pattern_hash,
                ),
            )

            event_id = cursor.lastrowid
            conn.commit()

            return str(event_id)

    def _analyze_code_pattern(self, code: str) -> str:
        """Analyser et créer un hash du pattern de code"""
        # Normaliser le code
        normalized = self._normalize_code(code)

        # Créer un hash
        return hashlib.md5(normalized.encode()).hexdigest()

    def _normalize_code(self, code: str) -> str:
        """Normaliser le code pour la comparaison"""
        # Supprimer les commentaires
        code = re.sub(r"#.*$", "", code, flags=re.MULTILINE)

        # Supprimer les docstrings
        code = re.sub(r'""".*?"""', "", code, flags=re.DOTALL)
        code = re.sub(r"'''.*?'''", "", code, flags=re.DOTALL)

        # Supprimer les espaces en début de ligne
        lines = [line.strip() for line in code.split("\n")]

        # Supprimer les lignes vides
        lines = [line for line in lines if line]

        return "\n".join(lines)

    def _update_pattern_learning(
        self, pattern_hash: str, pattern_type: str, success: bool
    ):
        """Mettre à jour l'apprentissage d'un pattern"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Vérifier si le pattern existe déjà
            cursor.execute(
                "SELECT * FROM learned_patterns WHERE pattern_hash = ?", (pattern_hash,)
            )
            existing = cursor.fetchone()

            if existing:
                # Mettre à jour le pattern existant
                occurrences = existing[3] + 1
                success_count = int(float(existing[6]) * existing[3]) + (
                    1 if success else 0
                )
                success_rate = success_count / occurrences

                cursor.execute(
                    """
                    UPDATE learned_patterns
                    SET occurrences = ?, last_seen = ?, success_rate = ?
                    WHERE pattern_hash = ?
                """,
                    (
                        occurrences,
                        datetime.now().isoformat(),
                        success_rate,
                        pattern_hash,
                    ),
                )
            else:
                # Créer un nouveau pattern
                cursor.execute(
                    """
                    INSERT INTO learned_patterns
                    (pattern_hash, pattern_type, occurrences, first_seen, last_seen, success_rate)
                    VALUES (?, ?, ?, ?, ?, ?)
                """,
                    (
                        pattern_hash,
                        pattern_type,
                        1,
                        datetime.now().isoformat(),
                        datetime.now().isoformat(),
                        1.0 if success else 0.0,
                    ),
                )

            conn.commit()

    def _generate_predictions_from_error(
        self, error_description: str, code_snippet: str, pattern_hash: str
    ):
        """Générer des prédictions basées sur une erreur"""
        # Analyser le type d'erreur et générer des prédictions
        if "duplicate" in error_description.lower():
            prediction = {
                "prediction_type": "duplicate",
                "confidence": 0.8,
                "description": "Risque de duplication de code",
                "suggested_action": "Vérifier s'il existe déjà une fonction/module similaire",
                "estimated_impact": "Moyen",
                "code_pattern": pattern_hash,
            }
        elif "complexity" in error_description.lower():
            prediction = {
                "prediction_type": "complexity",
                "confidence": 0.7,
                "description": "Code potentiellement trop complexe",
                "suggested_action": "Considérer la refactorisation en fonctions plus petites",
                "estimated_impact": "Élevé",
                "code_pattern": pattern_hash,
            }
        else:
            prediction = {
                "prediction_type": "error",
                "confidence": 0.6,
                "description": "Pattern similaire à une erreur précédente",
                "suggested_action": "Vérifier la logique et les bonnes pratiques",
                "estimated_impact": "Moyen",
                "code_pattern": pattern_hash,
            }

        # Sauvegarder la prédiction
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO predictions
                (prediction_type, confidence, description, suggested_action,
                 estimated_impact, code_pattern, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    prediction["prediction_type"],
                    prediction["confidence"],
                    prediction["description"],
                    prediction["suggested_action"],
                    prediction["estimated_impact"],
                    prediction["code_pattern"],
                    datetime.now().isoformat(),
                ),
            )
            conn.commit()

    def _find_similar_patterns(self, pattern_hash: str) -> List[Dict[str, Any]]:
        """Trouver des patterns similaires"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT pattern_hash, pattern_type, occurrences, success_rate, last_seen
                FROM learned_patterns
                WHERE pattern_hash != ?
                ORDER BY success_rate ASC
                LIMIT 10
            """,
                (pattern_hash,),
            )

            rows = cursor.fetchall()
            return [
                {
                    "pattern_hash": row[0],
                    "pattern_type": row[1],
                    "occurrences": row[2],
                    "success_rate": row[3],
                    "last_seen": row[4],
                }
                for row in rows
            ]

    def _check_antipatterns(self, code_snippet: str) -> List[Prediction]:
        """Vérifier les anti-patterns connus"""
        predictions = []

        # Anti-patterns à vérifier
        antipatterns = [
            (
                r"eval\s*\(",
                "Utilisation de eval() - Risque de sécurité",
                "Remplacer par une alternative sécurisée",
            ),
            (
                r"exec\s*\(",
                "Utilisation de exec() - Risque de sécurité",
                "Remplacer par une alternative sécurisée",
            ),
            (
                r"for\s+\w+\s+in\s+\w+:\s*\n\s*for\s+\w+\s+in\s+\w+:",
                "Boucles imbriquées - Complexité élevée",
                "Considérer l'utilisation de list comprehensions ou itertools",
            ),
            (
                r"if\s+\w+:\s*\n\s*if\s+\w+:\s*\n\s*if\s+\w+:",
                "Conditions imbriquées - Complexité élevée",
                "Refactoriser en utilisant des early returns ou des guard clauses",
            ),
            (
                r'password\s*=\s*["\'][^"\']+["\']',
                "Mot de passe en dur",
                "Utiliser des variables d'environnement ou un gestionnaire de secrets",
            ),
        ]

        for pattern, description, suggestion in antipatterns:
            if re.search(pattern, code_snippet):
                prediction = Prediction(
                    prediction_type="antipattern",
                    confidence=0.9,
                    description=description,
                    suggested_action=suggestion,
                    estimated_impact="Élevé",
                    code_pattern=self._analyze_code_pattern(code_snippet),
                )
                predictions.append(prediction)

        return predictions

    def _check_potential_duplicates(self, code_snippet: str) -> List[Prediction]:
        """Vérifier les doublons potentiels"""
        predictions = []

        # Chercher des patterns similaires dans l'historique
        pattern_hash = self._analyze_code_pattern(code_snippet)
        similar_patterns = self._find_similar_patterns(pattern_hash)

        for pattern in similar_patterns:
            if pattern["occurrences"] > 2:  # Pattern répété
                prediction = Prediction(
                    prediction_type="duplicate",
                    confidence=0.7,
                    description=f"Pattern similaire détecté {pattern['occurrences']} fois",
                    suggested_action=(
                        "Considérer l'extraction en fonction/" "module commun"
                    ),
                    estimated_impact="Moyen",
                    code_pattern=pattern_hash,
                )
                predictions.append(prediction)

        return predictions

    def _calculate_code_similarity(self, code1: str, code2: str) -> float:
        """Calculer la similarité entre deux codes"""
        # Normaliser les codes
        norm1 = self._normalize_code(code1)
        norm2 = self._normalize_code(code2)

        # Utiliser difflib pour calculer la similarité
        similarity = difflib.SequenceMatcher(None, norm1, norm2).ratio()
        return similarity

    def _save_correction_suggestion(
        self, original_code: str, corrected_code: str, reason: str, success: bool
    ):
        """Sauvegarder une suggestion de correction"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO correction_suggestions
                (original_code, suggested_code, reason, confidence,
                 based_on_corrections, created_at, applied, success)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    original_code,
                    corrected_code,
                    reason,
                    0.8 if success else 0.3,
                    json.dumps([]),  # Pour l'instant, pas de corrections basées
                    datetime.now().isoformat(),
                    True,
                    success,
                ),
            )
            conn.commit()


def main():
    """Test du système de mémoire intelligente"""
    memory = IntelligentMemory()

    # Simuler l'apprentissage d'une erreur
    error_id = memory.learn_from_error(
        error_description="Fonction trop longue détectée",
        code_snippet="def very_long_function():\n    # 100 lignes de code...",
        location="test_file.py:10",
        severity="medium",
    )

    # Simuler l'apprentissage d'une correction
    correction_id = memory.learn_from_correction(
        original_code="def very_long_function():\n    # 100 lignes...",
        corrected_code=(
            "def short_function1():\n    # 30 lignes...\n\n"
            "def short_function2():\n    # 30 lignes..."
        ),
        reason="Division en fonctions plus petites",
        location="test_file.py:10",
        success=True,
    )

    # Tester les prédictions
    predictions = memory.predict_issues(
        "def another_long_function():\n    # 80 lignes de code..."
    )

    print("🧠 Test du système de mémoire intelligente:")
    print(f"  • Erreur apprise: {error_id}")
    print(f"  • Correction apprise: {correction_id}")
    print(f"  • Prédictions générées: {len(predictions)}")

    for pred in predictions:
        print(f"    - {pred.description} (confiance: {pred.confidence:.2f})")

    # Obtenir les insights
    insights = memory.get_learning_insights()
    print("\n📊 Insights d'apprentissage:")
    print(f"  • Événements totaux: {insights['total_events']}")
    print(f"  • Taux d'erreur: {insights['error_rate']:.2f}")
    print(f"  • Patterns appris: {insights['total_patterns']}")
    print(f"  • Précision des prédictions: {insights['prediction_accuracy']:.2f}")


if __name__ == "__main__":
    main()
