import subprocess, os
def test_export_pipeline():
    subprocess.run(["python3", "export_pipeline.py"])
    assert os.path.exists("pipeline_export.tar.gz")
