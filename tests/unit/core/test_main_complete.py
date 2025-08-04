#!/usr/bin/env python3
"""
Tests complets pour main.py (326 lignes)
POINT D'ENTRÉE PRINCIPAL D'ATHALIA - PRIORITÉ MAXIMALE

Couverture actuelle: 30% → Objectif: 85%
Standards: Black + Ruff + MyPy + Bandit
"""

import pytest
import tempfile
import shutil
import signal
import time
import logging
from unittest.mock import Mock, patch, MagicMock, call
from pathlib import Path
import io
import sys

from athalia_core.main import (
    main,
    menu,
    signal_handler,
    running,
    execute_pipeline_phase,
    process_project,
    handle_user_choice,
    run_interactive_mode,
    run_batch_mode,
    setup_logging,
    cleanup_on_exit,
)


class TestMainModule:
    """Tests pour le module main principal."""

    def setup_method(self):
        """Configuration avant chaque test."""
        self.temp_dir = tempfile.mkdtemp()
        self.project_path = Path(self.temp_dir) / "test_project"
        self.project_path.mkdir(parents=True)
        
        # Créer structure projet de test
        (self.project_path / "src").mkdir()
        (self.project_path / "tests").mkdir()
        (self.project_path / "docs").mkdir()
        
        # Fichiers de test
        (self.project_path / "src" / "main.py").write_text("def main(): pass")
        (self.project_path / "README.md").write_text("# Test Project")
        (self.project_path / "requirements.txt").write_text("pytest>=7.0.0")

    def teardown_method(self):
        """Nettoyage après chaque test."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)
        # Réinitialiser le flag global
        global running
        running = True

    def test_signal_handler_sets_running_false(self):
        """Test que le gestionnaire de signal arrête la boucle."""
        global running
        running = True
        
        # Simuler signal
        signal_handler(signal.SIGINT, None)
        
        assert running is False

    def test_signal_handler_logs_message(self):
        """Test que le gestionnaire de signal log un message."""
        with patch('athalia_core.main.logger') as mock_logger:
            signal_handler(signal.SIGTERM, None)
            
            mock_logger.info.assert_called_once()
            call_args = mock_logger.info.call_args[0][0]
            assert "arrêt" in call_args.lower() or "stop" in call_args.lower()

    def test_setup_logging_configures_logger(self):
        """Test configuration du logging."""
        with patch('logging.basicConfig') as mock_config:
            setup_logging()
            
            mock_config.assert_called_once()

    def test_setup_logging_with_debug_level(self):
        """Test configuration logging avec niveau debug."""
        with patch('logging.basicConfig') as mock_config:
            setup_logging(debug=True)
            
            mock_config.assert_called_once()
            # Vérifier que le niveau debug est configuré
            call_kwargs = mock_config.call_args[1]
            assert call_kwargs.get('level') == logging.DEBUG

    def test_menu_displays_options(self):
        """Test affichage du menu principal."""
        # Capturer la sortie
        captured_output = io.StringIO()
        
        with patch('athalia_core.main.logger') as mock_logger:
            menu()
            
            # Vérifier que le menu est affiché
            mock_logger.info.assert_called()
            menu_calls = [call[0][0] for call in mock_logger.info.call_args_list]
            menu_text = " ".join(menu_calls)
            assert "athalia" in menu_text.lower()

    def test_execute_pipeline_phase_generation(self):
        """Test exécution phase génération."""
        with patch('athalia_core.main.log_main') as mock_log:
            with patch('athalia_core.generation.generate_project') as mock_generate:
                mock_generate.return_value = {"status": "success"}
                
                result = execute_pipeline_phase("generation", str(self.project_path))
                
                assert isinstance(result, dict)
                mock_log.assert_called()
                mock_generate.assert_called_once()

    def test_execute_pipeline_phase_testing(self):
        """Test exécution phase tests."""
        with patch('athalia_core.main.log_main') as mock_log:
            with patch('athalia_core.auto_tester.AutoTester') as mock_tester:
                mock_instance = Mock()
                mock_instance.run.return_value = {"tests_created": 5}
                mock_tester.return_value = mock_instance
                
                result = execute_pipeline_phase("testing", str(self.project_path))
                
                assert isinstance(result, dict)
                mock_log.assert_called()
                mock_tester.assert_called_once()

    def test_execute_pipeline_phase_documentation(self):
        """Test exécution phase documentation."""
        with patch('athalia_core.main.log_main') as mock_log:
            with patch('athalia_core.auto_documenter.AutoDocumenter') as mock_doc:
                mock_instance = Mock()
                mock_instance.generate_documentation.return_value = {"docs_created": 3}
                mock_doc.return_value = mock_instance
                
                result = execute_pipeline_phase("documentation", str(self.project_path))
                
                assert isinstance(result, dict)
                mock_log.assert_called()
                mock_doc.assert_called_once()

    def test_execute_pipeline_phase_security(self):
        """Test exécution phase sécurité."""
        with patch('athalia_core.main.log_main') as mock_log:
            with patch('athalia_core.security.security_audit_project') as mock_security:
                mock_security.return_value = {"vulnerabilities": 0}
                
                result = execute_pipeline_phase("security", str(self.project_path))
                
                assert isinstance(result, dict)
                mock_log.assert_called()
                mock_security.assert_called_once()

    def test_execute_pipeline_phase_cleanup(self):
        """Test exécution phase nettoyage."""
        with patch('athalia_core.main.log_main') as mock_log:
            with patch('athalia_core.cleanup.clean_old_tests_and_caches') as mock_cleanup:
                mock_cleanup.return_value = {"files_cleaned": 10}
                
                result = execute_pipeline_phase("cleanup", str(self.project_path))
                
                assert isinstance(result, dict)
                mock_log.assert_called()
                mock_cleanup.assert_called_once()

    def test_execute_pipeline_phase_ci(self):
        """Test exécution phase CI."""
        with patch('athalia_core.main.log_main') as mock_log:
            with patch('athalia_core.ci.generate_github_ci_yaml') as mock_ci:
                with patch('athalia_core.ci.add_coverage_badge') as mock_badge:
                    mock_ci.return_value = True
                    mock_badge.return_value = True
                    
                    result = execute_pipeline_phase("ci", str(self.project_path))
                    
                    assert isinstance(result, dict)
                    mock_log.assert_called()
                    mock_ci.assert_called_once()
                    mock_badge.assert_called_once()

    def test_execute_pipeline_phase_onboarding(self):
        """Test exécution phase onboarding."""
        with patch('athalia_core.main.log_main') as mock_log:
            with patch('athalia_core.onboarding.generate_onboard_cli') as mock_cli:
                with patch('athalia_core.onboarding.generate_onboarding_html_advanced') as mock_html:
                    mock_cli.return_value = True
                    mock_html.return_value = True
                    
                    result = execute_pipeline_phase("onboarding", str(self.project_path))
                    
                    assert isinstance(result, dict)
                    mock_log.assert_called()
                    mock_cli.assert_called_once()
                    mock_html.assert_called_once()

    def test_execute_pipeline_phase_invalid(self):
        """Test exécution phase invalide."""
        with patch('athalia_core.main.log_main') as mock_log:
            result = execute_pipeline_phase("invalid_phase", str(self.project_path))
            
            assert isinstance(result, dict)
            assert "error" in result
            mock_log.assert_called()

    def test_process_project_with_all_phases(self):
        """Test traitement projet avec toutes les phases."""
        phases = ["generation", "testing", "documentation", "security", "cleanup"]
        
        with patch('athalia_core.main.execute_pipeline_phase') as mock_phase:
            mock_phase.return_value = {"status": "success"}
            
            results = process_project(str(self.project_path), phases)
            
            assert isinstance(results, dict)
            assert len(results) == len(phases)
            assert mock_phase.call_count == len(phases)

    def test_process_project_with_single_phase(self):
        """Test traitement projet avec une seule phase."""
        with patch('athalia_core.main.execute_pipeline_phase') as mock_phase:
            mock_phase.return_value = {"status": "success"}
            
            results = process_project(str(self.project_path), ["testing"])
            
            assert isinstance(results, dict)
            assert "testing" in results
            mock_phase.assert_called_once()

    def test_process_project_error_handling(self):
        """Test gestion erreurs lors du traitement."""
        with patch('athalia_core.main.execute_pipeline_phase') as mock_phase:
            mock_phase.side_effect = Exception("Test error")
            
            results = process_project(str(self.project_path), ["testing"])
            
            assert isinstance(results, dict)
            assert "testing" in results
            assert "error" in results["testing"]

    def test_handle_user_choice_valid_number(self):
        """Test gestion choix utilisateur numéro valide."""
        with patch('builtins.input', return_value="1"):
            with patch('athalia_core.main.execute_pipeline_phase') as mock_phase:
                mock_phase.return_value = {"status": "success"}
                
                result = handle_user_choice(str(self.project_path))
                
                assert isinstance(result, (dict, bool))

    def test_handle_user_choice_all_phases(self):
        """Test gestion choix utilisateur toutes phases."""
        with patch('builtins.input', return_value="8"):  # Option "Tout exécuter"
            with patch('athalia_core.main.process_project') as mock_process:
                mock_process.return_value = {"all_phases": "success"}
                
                result = handle_user_choice(str(self.project_path))
                
                assert isinstance(result, (dict, bool))
                mock_process.assert_called_once()

    def test_handle_user_choice_quit(self):
        """Test gestion choix utilisateur quitter."""
        with patch('builtins.input', return_value="9"):  # Option quitter
            result = handle_user_choice(str(self.project_path))
            
            assert result is False

    def test_handle_user_choice_invalid_input(self):
        """Test gestion choix utilisateur entrée invalide."""
        with patch('builtins.input', return_value="invalid"):
            with patch('athalia_core.main.logger') as mock_logger:
                result = handle_user_choice(str(self.project_path))
                
                # Devrait gérer gracieusement
                assert isinstance(result, (dict, bool, type(None)))
                mock_logger.error.assert_called()

    def test_run_interactive_mode(self):
        """Test mode interactif."""
        global running
        running = True
        
        # Simuler quelques itérations puis arrêt
        call_count = 0
        def mock_handle_choice(project_path):
            nonlocal call_count
            call_count += 1
            if call_count >= 2:
                global running
                running = False
            return {"status": "success"}
        
        with patch('athalia_core.main.menu'):
            with patch('athalia_core.main.handle_user_choice', side_effect=mock_handle_choice):
                with patch('time.sleep'):  # Accélérer le test
                    result = run_interactive_mode(str(self.project_path))
                    
                    assert isinstance(result, dict)
                    assert call_count >= 2

    def test_run_interactive_mode_with_quit(self):
        """Test mode interactif avec commande quitter."""
        with patch('athalia_core.main.menu'):
            with patch('athalia_core.main.handle_user_choice', return_value=False):
                result = run_interactive_mode(str(self.project_path))
                
                assert isinstance(result, dict)

    def test_run_batch_mode_single_phase(self):
        """Test mode batch avec une phase."""
        with patch('athalia_core.main.execute_pipeline_phase') as mock_phase:
            mock_phase.return_value = {"status": "success"}
            
            result = run_batch_mode(str(self.project_path), ["testing"])
            
            assert isinstance(result, dict)
            mock_phase.assert_called_once()

    def test_run_batch_mode_multiple_phases(self):
        """Test mode batch avec plusieurs phases."""
        phases = ["generation", "testing", "documentation"]
        
        with patch('athalia_core.main.process_project') as mock_process:
            mock_process.return_value = {"batch_result": "success"}
            
            result = run_batch_mode(str(self.project_path), phases)
            
            assert isinstance(result, dict)
            mock_process.assert_called_once_with(str(self.project_path), phases)

    def test_cleanup_on_exit_normal(self):
        """Test nettoyage normal à la sortie."""
        with patch('athalia_core.main.log_main') as mock_log:
            cleanup_on_exit()
            
            mock_log.assert_called()

    def test_cleanup_on_exit_with_temp_files(self):
        """Test nettoyage avec fichiers temporaires."""
        # Créer fichiers temporaires
        temp_file = self.project_path / "temp_athalia.tmp"
        temp_file.write_text("temporary data")
        
        with patch('athalia_core.main.log_main') as mock_log:
            with patch('pathlib.Path.glob') as mock_glob:
                mock_glob.return_value = [temp_file]
                
                cleanup_on_exit()
                
                mock_log.assert_called()

    def test_main_function_test_mode(self):
        """Test fonction main en mode test."""
        result = main(test_mode=True)
        
        # En mode test, devrait retourner rapidement
        assert isinstance(result, (dict, type(None)))

    def test_main_function_with_project_path(self):
        """Test fonction main avec chemin projet."""
        with patch('athalia_core.main.run_interactive_mode') as mock_interactive:
            mock_interactive.return_value = {"interactive_result": "success"}
            
            result = main(project_path=str(self.project_path), test_mode=True)
            
            assert isinstance(result, (dict, type(None)))

    def test_main_function_with_batch_mode(self):
        """Test fonction main en mode batch."""
        with patch('athalia_core.main.run_batch_mode') as mock_batch:
            mock_batch.return_value = {"batch_result": "success"}
            
            result = main(
                project_path=str(self.project_path), 
                batch_mode=True, 
                phases=["testing"],
                test_mode=True
            )
            
            assert isinstance(result, (dict, type(None)))
            mock_batch.assert_called_once()

    def test_main_function_with_debug(self):
        """Test fonction main avec mode debug."""
        with patch('athalia_core.main.setup_logging') as mock_setup:
            result = main(debug=True, test_mode=True)
            
            mock_setup.assert_called_with(debug=True)
            assert isinstance(result, (dict, type(None)))

    def test_main_function_signal_setup(self):
        """Test configuration des signaux dans main."""
        with patch('signal.signal') as mock_signal:
            main(test_mode=True)
            
            # Vérifier que les signaux sont configurés
            mock_signal.assert_called()

    def test_main_function_error_handling(self):
        """Test gestion erreurs dans main."""
        with patch('athalia_core.main.setup_logging', side_effect=Exception("Setup error")):
            result = main(test_mode=True)
            
            # Devrait gérer l'erreur gracieusement
            assert isinstance(result, (dict, type(None)))

    @pytest.mark.parametrize("phase", [
        "generation", "testing", "documentation", 
        "security", "cleanup", "ci", "onboarding"
    ])
    def test_execute_pipeline_phase_all_phases(self, phase):
        """Test exécution de toutes les phases individuellement."""
        with patch('athalia_core.main.log_main'):
            # Mock tous les modules potentiels
            with patch('athalia_core.generation.generate_project', return_value={}):
                with patch('athalia_core.auto_tester.AutoTester') as mock_tester:
                    mock_tester.return_value.run.return_value = {}
                    with patch('athalia_core.auto_documenter.AutoDocumenter') as mock_doc:
                        mock_doc.return_value.generate_documentation.return_value = {}
                        with patch('athalia_core.security.security_audit_project', return_value={}):
                            with patch('athalia_core.cleanup.clean_old_tests_and_caches', return_value={}):
                                with patch('athalia_core.ci.generate_github_ci_yaml', return_value=True):
                                    with patch('athalia_core.ci.add_coverage_badge', return_value=True):
                                        with patch('athalia_core.onboarding.generate_onboard_cli', return_value=True):
                                            with patch('athalia_core.onboarding.generate_onboarding_html_advanced', return_value=True):
                                                result = execute_pipeline_phase(phase, str(self.project_path))
                                                
                                                assert isinstance(result, dict)

    def test_performance_main_execution(self):
        """Test performance exécution main."""
        import time
        
        start_time = time.time()
        result = main(test_mode=True)
        execution_time = time.time() - start_time
        
        # En mode test, devrait être très rapide
        assert execution_time < 1.0  # Moins d'une seconde
        assert isinstance(result, (dict, type(None)))

    def test_memory_usage_main_execution(self):
        """Test utilisation mémoire main."""
        import psutil
        import os
        
        process = psutil.Process(os.getpid())
        memory_before = process.memory_info().rss
        
        result = main(test_mode=True)
        
        memory_after = process.memory_info().rss
        memory_increase = memory_after - memory_before
        
        # L'augmentation mémoire devrait être raisonnable
        assert memory_increase < 50 * 1024 * 1024  # Moins de 50MB
        assert isinstance(result, (dict, type(None)))

    def test_concurrent_main_execution(self):
        """Test exécution concurrente de main."""
        import threading
        
        results = []
        errors = []
        
        def run_main():
            try:
                result = main(test_mode=True)
                results.append(result)
            except Exception as e:
                errors.append(e)
        
        # Lancer plusieurs threads
        threads = []
        for i in range(3):
            thread = threading.Thread(target=run_main)
            threads.append(thread)
            thread.start()
        
        # Attendre fin
        for thread in threads:
            thread.join()
        
        # Vérifier résultats
        assert len(errors) == 0  # Aucune erreur
        assert len(results) == 3  # 3 résultats


class TestMainIntegration:
    """Tests d'intégration pour le module main."""

    def setup_method(self):
        """Configuration tests intégration."""
        self.temp_dir = tempfile.mkdtemp()
        self.project_path = Path(self.temp_dir) / "integration_project"
        self.project_path.mkdir()

    def teardown_method(self):
        """Nettoyage tests intégration."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_full_pipeline_workflow(self):
        """Test workflow complet du pipeline."""
        # Créer projet complet
        (self.project_path / "src").mkdir()
        (self.project_path / "tests").mkdir()
        (self.project_path / "docs").mkdir()
        
        # Fichiers projet
        (self.project_path / "src" / "main.py").write_text('''
def main():
    """Point d'entrée principal."""
    return "Hello World"

if __name__ == "__main__":
    main()
''')
        
        (self.project_path / "README.md").write_text("# Integration Test Project")
        (self.project_path / "setup.py").write_text("from setuptools import setup; setup()")
        
        # Mock toutes les phases
        with patch('athalia_core.main.execute_pipeline_phase') as mock_phase:
            mock_phase.return_value = {"status": "success", "details": "Phase completed"}
            
            # Test mode batch complet
            result = main(
                project_path=str(self.project_path),
                batch_mode=True,
                phases=["generation", "testing", "documentation"],
                test_mode=True
            )
            
            assert isinstance(result, (dict, type(None)))

    def test_error_recovery_workflow(self):
        """Test récupération d'erreurs dans le workflow."""
        # Simuler erreurs dans différentes phases
        def mock_phase_with_error(phase, project_path):
            if phase == "testing":
                raise Exception("Test phase error")
            return {"status": "success"}
        
        with patch('athalia_core.main.execute_pipeline_phase', side_effect=mock_phase_with_error):
            result = process_project(str(self.project_path), ["generation", "testing", "documentation"])
            
            assert isinstance(result, dict)
            assert "testing" in result
            assert "error" in result["testing"]
            # Les autres phases devraient continuer
            assert "generation" in result
            assert "documentation" in result