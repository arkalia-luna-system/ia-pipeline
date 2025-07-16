import os
import subprocess
import time

def list_projects():
    return [d for d in os.listdir('.') if os.path.isdir(d) and d.startswith('ia_project')]

def run_workflow(proj, workflow='test', agent='default'):
    print(f"[Agent:{agent}] Lancement workflow {workflow} sur {proj}")
    if workflow == 'test':
        test_path = os.path.join(proj, 'tests')
        if os.path.exists(test_path):
            subprocess.run(['pytest', test_path])
    elif workflow == 'dag':
        print(f"[Agent:{agent}] [DAG] Workflow complexe pour {proj}")
        time.sleep(1)
        print(f"[Agent:{agent}] [DAG] Étape 1 OK")
        time.sleep(1)
        print(f"[Agent:{agent}] [DAG] Étape 2 OK")
        time.sleep(1)
        print(f"[Agent:{agent}] [DAG] Notif envoyée (mock)")
    elif workflow == 'monitor':
        print(f"[Agent:{agent}] Monitoring {proj} : OK (mock)")

def main():
    projs = list_projects()
    agents = ['default', 'agent2']
    for agent in agents:
        for p in projs:
            run_workflow(p, 'test', agent)
            run_workflow(p, 'dag', agent)
            run_workflow(p, 'monitor', agent)
if __name__ == "__main__":
    main()
