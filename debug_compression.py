#!/usr/bin/env python3
"""
Script de débogage pour la compression du cache
"""
from athalia_core.cache_manager import CacheManager
import tempfile
import os
import gzip

# Créer un répertoire temporaire
temp_dir = tempfile.mkdtemp()
print(f"Temp dir: {temp_dir}")

# Créer le cache manager
cm = CacheManager(temp_dir)

# Tester la compression
key = "compressed_key"
value = {"data": "x" * 1000}  # Données volumineuses

print("Test de mise en cache avec compression...")
result = cm.set_cache(key, value, compress=True)
print(f"Set cache result: {result}")

# Vérifier le fichier de cache
cache_file = os.path.join(temp_dir, 'compressed_key.cache')
print(f"Cache file exists: {os.path.exists(cache_file)}")
print(f"Cache file size: {os.path.getsize(cache_file)}")

# Lire le contenu brut
with open(cache_file, 'rb') as f:
    raw_data = f.read()
print(f"Raw data (first 50 bytes): {raw_data[:50]}")

# Tester les méthodes de détection
print(f"Is encrypted: {cm._is_encrypted(raw_data)}")
print(f"Is compressed: {cm._is_compressed(raw_data)}")

# Essayer de décompresser manuellement
try:
    if cm._is_compressed(raw_data):
        decompressed = gzip.decompress(raw_data)
        print(f"Decompressed data (first 100 bytes): {decompressed[:100]}")
        
        # Essayer de décoder JSON
        import json
        decoded = decompressed.decode('utf-8')
        parsed = json.loads(decoded)
        print(f"Parsed data: {parsed}")
        print(f"Value: {parsed['value']}")
    else:
        print("Data not detected as compressed")
except Exception as e:
    print(f"Error decompressing: {e}")

# Tester la récupération
print("\nTest de récupération du cache...")
cached = cm.get_cache(key)
print(f"Get cache result: {cached}")

# Nettoyer
import shutil
shutil.rmtree(temp_dir) 