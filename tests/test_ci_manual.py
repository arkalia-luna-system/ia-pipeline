from athalia_core import generate_github_ci_yaml
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as tmpdir:
    outdir = Path(tmpdir) / "f"
    outdir.mkdir(parents=True, exist_ok=True)
    generate_github_ci_yaml(outdir)
    ci_file = outdir / ".f" / "f" / "ci.f(f"
    print("CI file exists:", ci_file.exists())
    print("CI file path:", ci_file) 