"""
Configuration pytest pour Athalia
Gestion automatique du nettoyage des processus et ressources
"""

import os
import subprocess
import time
import psutil
import pytest


def kill_athalia_processes():
    """Arrête tous les processus Athalia en cours"""
    patterns = [
        "athalia_core.main",
        "athalia_core.cli",
        "ath-audit",
        "python.*athalia",
        "python3.*athalia",
    ]

    killed_count = 0
    for pattern in patterns:
        try:
            # Trouver les processus
            for proc in psutil.process_iter(["pid", "name", "cmdline"]):
                try:
                    if proc.info["cmdline"]:
                        cmdline = " ".join(proc.info["cmdline"])
                        if pattern in cmdline and "conftest.py" not in cmdline:
                            print(
                                f"🔄 Arrêt du processus {proc.info['pid']}: {cmdline[:100]}..."
                            )
                            proc.terminate()
                            killed_count += 1
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue

            # Attendre un peu pour les processus qui se terminent proprement
            if killed_count > 0:
                time.sleep(1)

        except Exception as e:
            print(f"⚠️ Erreur lors de l'arrêt des processus {pattern}: {e}")

    return killed_count


def cleanup_athalia_resources():
    """Nettoie les ressources Athalia (fichiers temporaires, etc.)"""
    try:
        # Nettoyer les fichiers temporaires Athalia
        temp_patterns = [
            "athalia_*.tmp",
            "athalia_*.log",
            "*.athalia_cache",
            "athalia_audit_*.json",
        ]

        for pattern in temp_patterns:
            subprocess.run(
                f"find . -name '{pattern}' -delete 2>/dev/null",
                shell=True,
                capture_output=True,
            )

    except Exception as e:
        print(f"⚠️ Erreur lors du nettoyage des ressources: {e}")


@pytest.fixture(scope="session", autouse=True)
def setup_test_session():
    """Configuration de la session de test"""
    print("\n🚀 Démarrage de la session de tests Athalia")

    # Arrêter les processus Athalia existants au début
    killed = kill_athalia_processes()
    if killed > 0:
        print(f"✅ {killed} processus Athalia arrêtés avant les tests")

    yield

    # Nettoyage final de la session
    print("\n🧹 Nettoyage final de la session de tests")
    kill_athalia_processes()
    cleanup_athalia_resources()


@pytest.fixture(autouse=True)
def cleanup_after_test():
    """Nettoyage automatique après chaque test"""
    yield

    # Arrêter les processus Athalia après chaque test
    killed = kill_athalia_processes()
    if killed > 0:
        print(f"🧹 {killed} processus Athalia arrêtés après le test")

    # Nettoyer les ressources
    cleanup_athalia_resources()


@pytest.fixture(scope="function")
def athalia_clean_environment():
    """Environnement propre pour les tests Athalia"""
    # Sauvegarder l'environnement original
    original_env = os.environ.copy()

    # Configurer l'environnement de test
    os.environ["ATHALIA_TEST_MODE"] = "1"
    os.environ["ATHALIA_VERBOSE"] = "0"
    os.environ["ATHALIA_LOG_LEVEL"] = "ERROR"

    yield

    # Restaurer l'environnement original
    os.environ.clear()
    os.environ.update(original_env)


@pytest.fixture(scope="function")
def athalia_process_monitor():
    """Moniteur de processus pour les tests Athalia"""

    class ProcessMonitor:
        def __init__(self):
            self.processes = []

        def track_process(self, pid):
            """Suivre un processus"""
            self.processes.append(pid)

        def cleanup(self):
            """Nettoyer tous les processus suivis"""
            for pid in self.processes:
                try:
                    proc = psutil.Process(pid)
                    if proc.is_running():
                        proc.terminate()
                        time.sleep(0.5)
                        if proc.is_running():
                            proc.kill()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            self.processes.clear()

    monitor = ProcessMonitor()
    yield monitor
    monitor.cleanup()


def pytest_configure(config):
    """Configuration pytest"""
    # Ajouter des marqueurs personnalisés
    config.addinivalue_line("markers", "athalia: marque un test comme test Athalia")
    config.addinivalue_line(
        "markers", "integration: marque un test comme test d'intégration"
    )
    config.addinivalue_line(
        "markers", "performance: marque un test comme test de performance"
    )


def pytest_collection_modifyitems(config, items):
    """Modifier les items de collection"""
    for item in items:
        # Ajouter automatiquement le marqueur athalia aux tests Athalia
        if "athalia" in item.nodeid.lower():
            item.add_marker(pytest.mark.athalia)


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """Résumé terminal après les tests"""
    print("\n" + "=" * 60)
    print("🧹 NETTOYAGE FINAL DES TESTS ATHALIA")
    print("=" * 60)

    # Arrêter tous les processus Athalia
    killed = kill_athalia_processes()
    if killed > 0:
        print(f"✅ {killed} processus Athalia arrêtés")
    else:
        print("✅ Aucun processus Athalia à arrêter")

    # Nettoyer les ressources
    cleanup_athalia_resources()
    print("✅ Ressources Athalia nettoyées")

    print("=" * 60)
    print("🎉 Tests Athalia terminés avec nettoyage automatique")
    print("=" * 60)
