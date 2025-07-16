import subprocess
def test_orchestrator_multi_agents():
    result = subprocess.run(["python3", "orchestrator_multi_agents.py"], capture_output=True, text=True)
    assert "[Agent:default]" in result.stdout and "[Agent:agent2]" in result.stdout and "Monitoring" in result.stdout
