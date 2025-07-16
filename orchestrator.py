import os
import subprocess
import time

def list_projects(filter_mod=None):
    projs = [d for d in os.listdir('.') if os.path.isdir(d) and d.startswith('ia_project')]
    if filter_mod:
        projs = [p for p in projs if filter_mod in open(os.path.join(p, 'blueprint.yaml')).read()]
    return projs

def run_workflow(proj, workflow='test'):
    if workflow == 'test':
        test_path = os.path.join(proj, 'tests')
        if os.path.exists(test_path):
            subprocess.run(['pytest', test_path])
    elif workflow == 'doc':
        doc_path = os.path.join(proj, 'DOC.md')
        if os.path.exists(doc_path):
            print(open(doc_path).read())
    elif workflow == 'dag':
        print(f"[DAG] Workflow complexe pour {proj}")
        time.sleep(1)
        print(f"[DAG] Étape 1 OK")
        time.sleep(1)
        print(f"[DAG] Étape 2 OK")
        time.sleep(1)
        print(f"[DAG] Notif envoyée (mock)")

def main():
    projs = list_projects()
    print(f"Projets détectés : {projs}")
    for p in projs:
        print(f"Tests pour {p} :")
        run_workflow(p, 'test')
        run_workflow(p, 'dag')
if __name__ == "__main__":
    main()
