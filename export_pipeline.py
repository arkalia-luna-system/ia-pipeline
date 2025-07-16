import shutil
import os
import tarfile

def export_pipeline():
    files = [f for f in os.listdir('.') if f.startswith('ia_project') or f in ['dashboard.html','orchestrator.py','export_pipeline.py']]
    with tarfile.open('pipeline_export.tar.gz', 'w:gz') as tar:
        for f in files:
            tar.add(f)
    print("Export pipeline -> pipeline_export.tar.gz")

if __name__ == "__main__":
    export_pipeline()
