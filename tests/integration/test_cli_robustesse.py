import subprocess
import sys

def test_cli_robustesse():
    # Test simple de la CLI sans interaction complexe
    result = subprocess.run([sys.executable, "athalia_core/main.py", "--help"], 
                          capture_output=True, text=True, timeout=10)
    # Vérifie que la CLI répond sans crash
    assert result.returncode in [0, 1]  # 0=succès, 1=erreur d'usage
    assert "Traceback" not in result.stderr 