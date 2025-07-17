import tempfile
import os
from athalia_core.ready_check import check_ready

def test_check_ready_ok():
    with tempfile.TemporaryDirectory() as d:
        for f in ["README.md", "DOC.md", "requirements.txt"]:
            open(os.path.join(d, f), "w").close()
        os.mkdir(os.path.join(d, "tests"))
        report = check_ready(d)
        assert report["ready"]
        assert not report["missing"]

def test_check_ready_missing():
    with tempfile.TemporaryDirectory() as d:
        # Manque tout
        report = check_ready(d)
        assert not report["ready"]
        assert "README.md" in report["missing"]
        assert "tests/" in report["missing"] 