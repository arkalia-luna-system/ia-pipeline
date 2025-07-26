#!/bin/bash
PROMPT_DIR="$(dirname "$0")/../prompts"

function show_menu() {
  echo "Choisis un booster IA :"
  echo "1) Débogage (dev_debug)"
  echo "2) Booster UX/Fun (ux_fun_boost)"
  echo "3) Audit Design (design_review)"
  echo "4) Stratégie de tests (test_strategy)"
  echo "5) Refactorisation (code_refactor)"
  read -p "Numéro ou nom : " choix
  case $choix in
    1|dev_debug) cat "$PROMPT_DIR/dev_debug.yaml" ;;
    2|ux_fun_boost) cat "$PROMPT_DIR/ux_fun_boost.md" ;;
    3|design_review) cat "$PROMPT_DIR/design_review.md" ;;
    4|test_strategy) cat "$PROMPT_DIR/test_strategy.md" ;;
    5|code_refactor) cat "$PROMPT_DIR/code_refactor.yaml" ;;
    *) echo "Choix invalide"; exit 1;;
  esac
}

if [ -z "$1" ]; then
  show_menu
else
  case $1 in
    debug) cat "$PROMPT_DIR/dev_debug.yaml" ;;
    ux) cat "$PROMPT_DIR/ux_fun_boost.md" ;;
    design) cat "$PROMPT_DIR/design_review.md" ;;
    test) cat "$PROMPT_DIR/test_strategy.md" ;;
    refactor) cat "$PROMPT_DIR/code_refactor.yaml" ;;
    *) echo "Usage : $0 [debug|ux|design|test|refactor]"; exit 1;;
  esac
fi 