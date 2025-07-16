import os
import shutil
import subprocess

def test_ath_architect_generation():
    # Nettoyage avant test
    if os.path.exists('ia_project'):
        for root, dirs, files in os.walk('ia_project', topdown=False):
            for name in files:
                try:
                    os.remove(os.path.join(root, name))
                except FileNotFoundError:
                    pass
            for name in dirs:
                try:
                    os.rmdir(os.path.join(root, name))
                except FileNotFoundError:
                    pass
        try:
            os.rmdir('ia_project')
        except FileNotFoundError:
            pass
    # Simule une entrée utilisateur
    script_path = os.path.join(os.path.dirname(__file__), '../ath-architect.py')
    process = subprocess.Popen(['python3', script_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input='Projet test IA avec API et mémoire\n')
    assert process.returncode == 0, f"Erreur à l'exécution : {stderr}"
    # Vérifie la génération des fichiers clés
    assert os.path.exists('ia_project/GENESIS.md'), "GENESIS.md manquant"
    assert os.path.exists('ia_project/blueprint.yaml'), "blueprint.yaml manquant"
    assert os.path.exists('ia_project/src/'), "Dossier src/ manquant"
    assert os.path.exists('ia_project/tests/'), "Dossier tests/ manquant"
    # Vérifie la génération des fichiers templates
    assert os.path.exists('ia_project/api/main.py'), "api/main.py manquant"
    assert os.path.exists('ia_project/tts/tts.py'), "tts/tts.py manquant"
    assert os.path.exists('ia_project/memory/memory.py'), "memory/memory.py manquant"
    print("Test Architecte IA : génération OK (avec templates)")

if __name__ == "__main__":
    test_ath_architect_generation() 