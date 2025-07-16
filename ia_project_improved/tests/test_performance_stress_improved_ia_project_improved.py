import time
import os

def test_generation_time():
    start = time.time()
    # Simule une opération lourde
    for _ in range(1000000): pass
    elapsed = time.time() - start
    assert elapsed < 2, f"Génération trop lente : {elapsed:.2f}s"

def test_disk_usage():
    total = 0
    for root, dirs, files in os.walk(os.path.dirname(__file__)):
        for f in files:
            try:
                total += os.path.getsize(os.path.join(root, f))
            except Exception:
                pass
    assert total < 100*1024*1024, f"Projet trop volumineux : {total/1024/1024:.2f} Mo"
