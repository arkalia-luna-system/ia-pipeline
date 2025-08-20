#!/bin/bash
# Alias Robotique Athalia
# À sourcer dans votre .bashrc ou .zshrc

# Audit robotique complet
alias ath-robotics='python3 $(git rev-parse --show-toplevel)/bin/core/athalia_unified.py . --action audit'

# Modules spécifiques
alias ath-reachy-audit='python3 $(git rev-parse --show-toplevel)/athalia_core/robotics/reachy_auditor.py .'
alias ath-ros2-validate='python3 $(git rev-parse --show-toplevel)/athalia_core/robotics/ros2_validator.py .'
alias ath-docker-robotics='python3 $(git rev-parse --show-toplevel)/athalia_core/robotics/docker_robotics.py .'
alias ath-rust-analyze='python3 $(git rev-parse --show-toplevel)/athalia_core/robotics/rust_analyzer.py .'
alias ath-robotics-ci='python3 $(git rev-parse --show-toplevel)/athalia_core/automation/robotics_ci.py .'

# Démonstration
alias ath-robotics-demo='python3 $(git rev-parse --show-toplevel)/bin/core/ath-demo.py'

# Tests robotiques
alias ath-test-robotics='python3 -m pytest $(git rev-parse --show-toplevel)/tests/robotics/ -v'

# Setup automatique
alias ath-setup-robotics='python3 $(git rev-parse --show-toplevel)/bin/core/athalia_unified.py . --action setup && echo "✅ Module robotique configuré!"'

# Aide
alias ath-robotics-help='echo "Alias robotiques disponibles:" && echo "  ath-robotics        - Audit complet" && echo "  ath-reachy-audit    - Audit Reachy" && echo "  ath-ros2-validate   - Validation ROS2" && echo "  ath-docker-robotics - Gestion Docker" && echo "  ath-rust-analyze    - Analyse Rust" && echo "  ath-robotics-ci     - CI/CD robotique" && echo "  ath-robotics-demo   - Démonstration" && echo "  ath-test-robotics   - Tests" && echo "  ath-setup-robotics  - Setup automatique"'
