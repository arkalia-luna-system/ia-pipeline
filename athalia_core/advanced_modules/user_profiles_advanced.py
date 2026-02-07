#!/usr/bin/env python3
"""
Module de gestion des profils utilisateur avancés pour Athalia
Gestion des préférences, historique, statistiques et personnalisation
"""

import json
import logging
import sqlite3
from datetime import datetime
from typing import Any

logger = logging.getLogger(__name__)


class ProfilUtilisateur:
    """Profil utilisateur avec préférences et historique"""

    def __init__(self, nom: str, email: str = "", preferences: dict = None):
        self.nom = nom
        self.email = email
        self.preferences = preferences or {}
        self.date_creation = datetime.now()
        self.derniere_connexion = datetime.now()
        self.projets_consultes: list[str] = []
        self.actions_frequentes: dict[str, int] = {}

    def to_dict(self) -> dict[str, Any]:
        """Conversion en dictionnaire"""
        return {
            "nom": self.nom,
            "email": self.email,
            "preferences": self.preferences,
            "date_creation": self.date_creation.isoformat(),
            "derniere_connexion": self.derniere_connexion.isoformat(),
            "projets_consultes": self.projets_consultes,
            "actions_frequentes": self.actions_frequentes,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ProfilUtilisateur":
        """Création depuis un dictionnaire"""
        profil = cls(data["nom"], data.get("email", ""))
        profil.preferences = data.get("preferences", {})
        profil.date_creation = datetime.fromisoformat(data["date_creation"])
        profil.derniere_connexion = datetime.fromisoformat(data["derniere_connexion"])
        profil.projets_consultes = data.get("projets_consultes", [])
        profil.actions_frequentes = data.get("actions_frequentes", {})
        return profil


class GestionnaireProfils:
    """Gestionnaire de profils utilisateur avancé"""

    def __init__(self, db_path: str = "profils_utilisateur.db"):
        self.db_path = db_path
        self._init_database()

    def _init_database(self):
        """Initialisation de la base de données"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Table des profils
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS profils (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom TEXT UNIQUE NOT NULL,
                    email TEXT,
                    preferences TEXT,
                    date_creation TEXT,
                    derniere_connexion TEXT
                )
            """)

            # Table des actions
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS actions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    profil_id INTEGER,
                    action TEXT,
                    timestamp TEXT,
                    details TEXT,
                    FOREIGN KEY (profil_id) REFERENCES profils (id)
                )
            """)

            # Table des projets consultés
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS projets_consultes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    profil_id INTEGER,
                    chemin_projet TEXT,
                    date_consultation TEXT,
                    duree_consultation INTEGER,
                    FOREIGN KEY (profil_id) REFERENCES profils (id)
                )
            """)

            conn.commit()

    def creer_profil(
        self, nom: str, email: str = "", preferences: dict = None
    ) -> ProfilUtilisateur:
        """Création d'un nouveau profil"""
        logger.info(f"Création du profil utilisateur: {nom}")

        profil = ProfilUtilisateur(nom, email, preferences)

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO profils (nom, email, preferences, date_creation,
                derniere_connexion) VALUES (?, ?, ?, ?, ?)
            """,
                (
                    profil.nom,
                    profil.email,
                    json.dumps(profil.preferences),
                    profil.date_creation.isoformat(),
                    profil.derniere_connexion.isoformat(),
                ),
            )
            conn.commit()

        return profil

    def obtenir_profil(self, nom: str) -> ProfilUtilisateur | None:
        """Récupération d'un profil par nom"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT nom, email, preferences, date_creation,
                derniere_connexion FROM profils WHERE nom = ?
            """,
                (nom,),
            )

            row = cursor.fetchone()
            if row:
                profil = ProfilUtilisateur(row[0], row[1])
                profil.preferences = json.loads(row[2]) if row[2] else {}
                profil.date_creation = datetime.fromisoformat(row[3])
                profil.derniere_connexion = datetime.fromisoformat(row[4])

                # Récupération des actions fréquentes
                cursor.execute(
                    """
                    SELECT action, COUNT(*) as count
                    FROM actions
                    WHERE profil_id = (SELECT id FROM profils WHERE nom = ?)
                    GROUP BY action ORDER BY count DESC LIMIT 10
                """,
                    (nom,),
                )

                for action, count in cursor.fetchall():
                    profil.actions_frequentes[action] = count

                # Récupération des projets consultés
                cursor.execute(
                    """
                    SELECT chemin_projet, date_consultation
                    FROM projets_consultes
                    WHERE profil_id = (SELECT id FROM profils WHERE nom = ?)
                    ORDER BY date_consultation DESC LIMIT 20
                """,
                    (nom,),
                )

                profil.projets_consultes = [row[0] for row in cursor.fetchall()]

                return profil

        return None

    def mettre_a_jour_profil(self, profil: ProfilUtilisateur):
        """Mise à jour d'un profil"""
        profil.derniere_connexion = datetime.now()

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE profils
                SET email = ?, preferences = ?, derniere_connexion = ?
                WHERE nom = ?
            """,
                (
                    profil.email,
                    json.dumps(profil.preferences),
                    profil.derniere_connexion.isoformat(),
                    profil.nom,
                ),
            )
            conn.commit()

    def enregistrer_action(self, nom_profil: str, action: str, details: dict = None):
        """Enregistrement d'une action utilisateur"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM profils WHERE nom = ?", (nom_profil,))
            profil_id = cursor.fetchone()

            if profil_id:
                cursor.execute(
                    """
                    INSERT INTO actions (profil_id, action, timestamp, details)
                    VALUES (?, ?, ?, ?)
                """,
                    (
                        profil_id[0],
                        action,
                        datetime.now().isoformat(),
                        json.dumps(details) if details else None,
                    ),
                )
                conn.commit()

    def enregistrer_consultation_projet(
        self, nom_profil: str, chemin_projet: str, duree: int = 0
    ):
        """Enregistrement de la consultation d'un projet"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM profils WHERE nom = ?", (nom_profil,))
            profil_id = cursor.fetchone()

            if profil_id:
                cursor.execute(
                    """
                    INSERT INTO projets_consultes
                    (profil_id, chemin_projet, date_consultation, duree_consultation)
                    VALUES (?, ?, ?, ?)
                """,
                    (
                        profil_id[0],
                        chemin_projet,
                        datetime.now().isoformat(),
                        duree,
                    ),
                )
                conn.commit()

    def obtenir_statistiques(self, nom_profil: str) -> dict[str, Any]:
        """Obtention des statistiques d'un profil"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Actions les plus fréquentes
            cursor.execute(
                """
                SELECT action, COUNT(*) as count
                FROM actions a
                JOIN profils p ON a.profil_id = p.id
                WHERE p.nom = ?
                GROUP BY action
                ORDER BY count DESC
                LIMIT 10
            """,
                (nom_profil,),
            )

            actions_frequentes = {row[0]: row[1] for row in cursor.fetchall()}

            # Projets les plus consultés
            cursor.execute(
                """
                SELECT chemin_projet, COUNT(*) as count
                FROM projets_consultes pc
                JOIN profils p ON pc.profil_id = p.id
                WHERE p.nom = ?
                GROUP BY chemin_projet
                ORDER BY count DESC
                LIMIT 10
            """,
                (nom_profil,),
            )

            projets_frequents = {row[0]: row[1] for row in cursor.fetchall()}
            projets_consultes = list(projets_frequents.keys())

            # Temps total passé
            cursor.execute(
                """
                SELECT SUM(duree_consultation) as total_time
                FROM projets_consultes pc
                JOIN profils p ON pc.profil_id = p.id
                WHERE p.nom = ?
            """,
                (nom_profil,),
            )

            temps_total = cursor.fetchone()[0] or 0

            return {
                "actions_frequentes": actions_frequentes,
                "projets_frequents": projets_frequents,
                "projets_consultes": projets_consultes,
                "temps_total": temps_total,
                "duree_totale": temps_total,
                "total_actions": sum(actions_frequentes.values()),
                "total_projets": len(projets_frequents),
                "connexion": actions_frequentes.get("connexion", 0),
            }

    def generer_rapport_profil(self, nom_profil: str) -> str:
        """Génération d'un rapport détaillé pour un profil"""
        profil = self.obtenir_profil(nom_profil)
        if not profil:
            return f" Profil '{nom_profil}' non trouvé"

        stats = self.obtenir_statistiques(nom_profil)

        rapport = f"""
 RAPPORT PROFIL UTILISATEUR - {nom_profil}
{"=" * 50}

👤 INFORMATIONS GÉNÉRALES:
• Email: {profil.email}
• Date de création: {profil.date_creation.strftime("%d/%m/%Y %H:%M")}
• Dernière connexion: {profil.derniere_connexion.strftime("%d/%m/%Y %H:%M")}

📈 STATISTIQUES:
• Actions totales: {stats["total_actions"]}
• Projets consultés: {stats["total_projets"]}
• Temps total: {stats["temps_total"]} minutes

🔝 ACTIONS LES PLUS FRÉQUENTES:
"""

        for action, count in list(stats["actions_frequentes"].items())[:5]:
            rapport += f"• {action}: {count} fois\n"

        rapport += """
 PROJETS LES PLUS CONSULTÉS:
"""

        for projet, count in list(stats["projets_frequents"].items())[:5]:
            rapport += f"• {projet}: {count} consultations\n"

        rapport += """
⚙ PRÉFÉRENCES:
"""

        for pref, valeur in profil.preferences.items():
            rapport += f"• {pref}: {valeur}\n"

        return rapport

    def lister_profils(self) -> list[str]:
        """Liste de tous les profils"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT nom FROM profils ORDER BY derniere_connexion DESC")
            return [row[0] for row in cursor.fetchall()]

    def supprimer_profil(self, nom: str) -> bool:
        """Suppression d'un profil"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM profils WHERE nom = ?", (nom,))
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            logger.error(f"Erreur lors de la suppression du profil {nom}: {e}")
            return False

    def exporter_profil(self, nom: str, fichier_destination: str) -> bool:
        """Export d'un profil vers un fichier JSON"""
        try:
            profil = self.obtenir_profil(nom)
            if not profil:
                return False

            with open(fichier_destination, "w", encoding="utf-8") as f:
                json.dump(profil.to_dict(), f, indent=2, ensure_ascii=False)

            return True
        except Exception as e:
            logger.error(f"Erreur lors de l'export du profil {nom}: {e}")
            return False

    def importer_profil(self, fichier_source: str) -> bool:
        """Import d'un profil depuis un fichier JSON"""
        try:
            with open(fichier_source, encoding="utf-8") as f:
                data = json.load(f)

            profil = ProfilUtilisateur.from_dict(data)
            self.creer_profil(profil.nom, profil.email, profil.preferences)
            return True
        except Exception as e:
            logger.error(f"Erreur lors de l'import du profil: {e}")
            return False


def main():
    """Fonction principale pour test"""
    import argparse

    parser = argparse.ArgumentParser(description="Gestionnaire de profils utilisateur")
    parser.add_argument(
        "action",
        choices=["creer", "obtenir", "lister", "rapport"],
        help="Action à effectuer",
    )
    parser.add_argument("nom", nargs="?", help="Nom du profil")
    parser.add_argument("--email", help="Email du profil")

    args = parser.parse_args()

    gestionnaire = GestionnaireProfils()

    if args.action == "creer":
        if not args.nom:
            print(" Nom du profil requis")
            return
        profil_creer = gestionnaire.creer_profil(args.nom, args.email or "")
        print(f" Profil '{profil_creer.nom}' créé avec succès")

    elif args.action == "obtenir":
        if not args.nom:
            print(" Nom du profil requis")
            return
        profil: ProfilUtilisateur | None = gestionnaire.obtenir_profil(args.nom)
        if profil is not None:
            print(f" Profil trouvé: {profil.nom} ({profil.email})")
        else:
            print(f" Profil '{args.nom}' non trouvé")

    elif args.action == "lister":
        profils = gestionnaire.lister_profils()
        print("📋 Profils disponibles:")
        for nom_profil in profils:
            print(f"• {nom_profil}")

    elif args.action == "rapport":
        if not args.nom:
            print(" Nom du profil requis")
            return
        rapport = gestionnaire.generer_rapport_profil(args.nom)
        print(rapport)


if __name__ == "__main__":
    main()
