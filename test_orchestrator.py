import subprocess
def test_orchestrator():
    result = subprocess.run(["python3", "orchestrator.py"], capture_output=True, text=True)
    assert "Projets détectés" in result.stdout and "[DAG]" in result.stdout
