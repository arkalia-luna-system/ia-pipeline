import os
import signal
import subprocess
import sys
import time
from pathlib import Path

import pytest
import requests


@pytest.fixture(scope="module")
def server_process():
    project_root = Path("/Volumes/T7/athalia-dev-setup")
    env = os.environ.copy()
    env["PYTHONPATH"] = str(project_root)

    proc = subprocess.Popen(
        [
            sys.executable,
            "-m",
            "uvicorn",
            "athalia_core.api.main_api_server:app",
            "--host",
            "127.0.0.1",
            "--port",
            "8001",
        ],
        cwd=project_root,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    # Attente démarrage
    timeout_s = 20
    start = time.time()
    while time.time() - start < timeout_s:
        try:
            r = requests.get("http://127.0.0.1:8001/health", timeout=1)
            if r.status_code == 200:
                break
        except Exception:
            pass
        time.sleep(0.5)

    yield proc

    # Teardown
    try:
        proc.send_signal(signal.SIGINT)
        proc.wait(timeout=5)
    except Exception:
        proc.kill()


def test_health_ok(server_process):
    r = requests.get("http://127.0.0.1:8001/health", timeout=5)
    assert r.status_code == 200
    data = r.json()
    assert data.get("status") == "healthy"


def test_docs_available(server_process):
    r = requests.get("http://127.0.0.1:8001/docs", timeout=5)
    assert r.status_code == 200
    assert "text/html" in r.headers.get("content-type", "")


@pytest.mark.e2e
def test_metrics_endpoint(server_process):
    r = requests.get("http://127.0.0.1:8001/metrics", timeout=5)
    assert r.status_code in (200, 503)  # 503 si Prometheus non dispo
    if r.status_code == 200:
        assert "athalia_http_requests_total" in r.text
