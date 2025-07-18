#!/bin/bash
# Test manuel de tous les alias Athalia/Arkalia (hors interactifs)

source "$(dirname "$0")/../setup/alias.sh"

ALIASES=(
  ath-clean
  ath-test
  ath-lint
  ath-build
  ath-smart
  ath-cli-main
  ath-unified
  ath-audit
  ath-coverage
)

for alias in "${ALIASES[@]}"; do
  echo "\n=== Test de l'alias : $alias ==="
  if type "$alias" >/dev/null 2>&1; then
    "$alias" --help 2>/dev/null || "$alias"
    echo "[OK] $alias exécuté"
  else
    echo "[ERREUR] Alias $alias non trouvé"
  fi
done

echo "\nTest manuel terminé. Vérifiez les sorties ci-dessus pour détecter d’éventuels problèmes." 