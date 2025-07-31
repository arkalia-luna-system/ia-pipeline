#!/usr/bin/env python3
"""
Tests pour le module context_prompt.py
Amélioration de la couverture de code de 16.55% à 80%+
"""

from unittest.mock import MagicMock, mock_open, patch

from athalia_core.agents.context_prompt import (
    PROMPTS,
    detect_prompt_semantic,
    detect_prompts_scoring,
    score_prompt,
    show_prompts,
)


class TestPromptScoring:
    """Tests pour le système de scoring des prompts"""

    def test_score_prompt_basic(self):
        """Test de scoring basique d'un prompt"""
        prompt = {"name": "Test Prompt", "patterns": [r"test", r"assert"], "weight": 1}

        filename = "test_file.py"
        content = "def test_function(): assert True"

        score, explanations = score_prompt(prompt, filename, content)

        assert isinstance(score, int)
        assert isinstance(explanations, list)
        assert score >= 0

    def test_score_prompt_with_patterns(self):
        """Test de scoring avec patterns spécifiques"""
        prompt = {
            "name": "Testing Prompt",
            "patterns": [r"test_.*\.py", r"assert", r"pytest"],
            "weight": 2,
        }

        filename = "test_validation.py"
        content = "import pytest\ndef test_validation(): assert True"

        score, explanations = score_prompt(prompt, filename, content)

        assert isinstance(score, int)
        assert isinstance(explanations, list)
        assert score > 0

    def test_score_prompt_no_matches(self):
        """Test de scoring sans correspondances"""
        prompt = {
            "name": "Security Prompt",
            "patterns": [r"password", r"secret", r"key"],
            "weight": 1,
        }

        filename = "math_utils.py"
        content = "def add(a, b): return a + b"

        score, explanations = score_prompt(prompt, filename, content)

        assert isinstance(score, int)
        assert isinstance(explanations, list)
        assert score == 0

    def test_score_prompt_filename_match(self):
        """Test de scoring avec correspondance de nom de fichier"""
        prompt = {
            "name": "Markdown Prompt",
            "patterns": [r"\.md$", r"# ", r"## "],
            "weight": 1,
        }

        filename = "README.md"
        content = "# Project Title\n## Description"

        score, explanations = score_prompt(prompt, filename, content)

        assert isinstance(score, int)
        assert isinstance(explanations, list)
        assert score > 0


class TestPromptDetection:
    """Tests pour la détection de prompts"""

    @patch("builtins.open", new_callable=mock_open, read_data="def test_function(): pass")
    def test_detect_prompts_scoring(self, mock_file):
        """Test de détection de prompts avec scoring"""
        filepath = "test_file.py"
        
        scored_prompts = detect_prompts_scoring(filepath)
        
        assert isinstance(scored_prompts, list)
        assert len(scored_prompts) > 0
        # Les prompts sont des tuples (score, prompt, explanations)
        assert all(isinstance(p, tuple) for p in scored_prompts)
        assert all(len(p) == 3 for p in scored_prompts)  # (score, prompt, explanations)

    @patch("builtins.open", new_callable=mock_open, read_data="import pytest\ndef test_validation(): assert True")
    def test_detect_prompts_scoring_with_test_content(self, mock_file):
        """Test de détection avec contenu de test"""
        filepath = "test_validation.py"
        
        scored_prompts = detect_prompts_scoring(filepath)
        
        assert isinstance(scored_prompts, list)
        # Vérifier qu'au moins un prompt de test a un score > 0
        assert any(score > 0 for score, prompt, explanations in scored_prompts if "test" in prompt["name"].lower())

    @patch("builtins.open", new_callable=mock_open, read_data="# Project Documentation\n## Features")
    def test_detect_prompts_scoring_with_markdown(self, mock_file):
        """Test de détection avec contenu markdown"""
        filepath = "README.md"
        
        scored_prompts = detect_prompts_scoring(filepath)
        
        assert isinstance(scored_prompts, list)
        # Vérifier qu'au moins un prompt de design a un score > 0
        assert any(score > 0 for score, prompt, explanations in scored_prompts if "design" in prompt["name"].lower())


class TestSemanticPromptDetection:
    """Tests pour la détection sémantique de prompts"""

    @patch("subprocess.run")
    def test_detect_prompt_semantic(self, mock_run):
        """Test de détection sémantique de prompt"""
        mock_run.return_value = MagicMock(
            returncode=0, stdout=b"test_strategy.md", stderr=b""
        )

        filepath = "test_file.py"

        semantic_prompt = detect_prompt_semantic(filepath)

        assert isinstance(semantic_prompt, str)
        assert semantic_prompt in [
            "test_strategy.md",
            "code_refactor.yaml",
            "design_review.md",
            "ux_fun_boost.md",
            "dev_debug.yaml",
        ]

    @patch("subprocess.run")
    def test_detect_prompt_semantic_error(self, mock_run):
        """Test de détection sémantique avec erreur"""
        mock_run.return_value = MagicMock(returncode=1, stdout=b"", stderr=b"Error")

        filepath = "test_file.py"

        semantic_prompt = detect_prompt_semantic(filepath)

        assert semantic_prompt is None

    @patch("subprocess.run")
    def test_detect_prompt_semantic_timeout(self, mock_run):
        """Test de détection sémantique avec timeout"""
        mock_run.side_effect = TimeoutError("Timeout")

        filepath = "test_file.py"

        semantic_prompt = detect_prompt_semantic(filepath)

        assert semantic_prompt is None


class TestPromptDisplay:
    """Tests pour l'affichage des prompts"""

    def test_show_prompts_basic(self):
        """Test d'affichage basique des prompts"""
        scored_prompts = [
            ({"name": "Test Prompt", "file": "test_strategy.md"}, 0.8),
            ({"name": "Design Prompt", "file": "design_review.md"}, 0.3),
        ]

        result = show_prompts(scored_prompts)

        assert isinstance(result, str)
        assert "Test Prompt" in result
        assert "Design Prompt" in result

    def test_show_prompts_with_semantic(self):
        """Test d'affichage avec prompt sémantique"""
        scored_prompts = [
            ({"name": "Test Prompt", "file": "test_strategy.md"}, 0.8),
            ({"name": "Design Prompt", "file": "design_review.md"}, 0.3),
        ]
        semantic_prompt = "test_strategy.md"

        result = show_prompts(scored_prompts, semantic_prompt)

        assert isinstance(result, str)
        assert "Test Prompt" in result
        assert "IA Sémantique" in result

    def test_show_prompts_empty(self):
        """Test d'affichage avec liste vide"""
        scored_prompts = []

        result = show_prompts(scored_prompts)

        assert isinstance(result, str)
        assert "Aucun prompt" in result or len(result) == 0


class TestPromptConstants:
    """Tests pour les constantes de prompts"""

    def test_prompts_structure(self):
        """Test de la structure des prompts"""
        assert isinstance(PROMPTS, list)
        assert len(PROMPTS) > 0

        for prompt in PROMPTS:
            assert "name" in prompt
            assert "file" in prompt
            assert "patterns" in prompt
            assert "weight" in prompt
            assert isinstance(prompt["name"], str)
            assert isinstance(prompt["file"], str)
            assert isinstance(prompt["patterns"], list)
            assert isinstance(prompt["weight"], int)

    def test_prompts_patterns(self):
        """Test des patterns des prompts"""
        for prompt in PROMPTS:
            for pattern in prompt["patterns"]:
                assert isinstance(pattern, str)
                assert len(pattern) > 0

    def test_prompts_weights(self):
        """Test des poids des prompts"""
        for prompt in PROMPTS:
            assert prompt["weight"] > 0
            assert prompt["weight"] <= 10  # Poids raisonnable


class TestIntegration:
    """Tests d'intégration pour le système de prompts"""

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="import pytest\ndef test_function(): assert True",
    )
    @patch("subprocess.run")
    def test_full_prompt_detection_workflow(self, mock_run, mock_file):
        """Test du workflow complet de détection de prompts"""
        mock_run.return_value = MagicMock(
            returncode=0, stdout=b"test_strategy.md", stderr=b""
        )

        filepath = "test_file.py"

        # Test de détection avec scoring
        scored_prompts = detect_prompts_scoring(filepath)

        # Test de détection sémantique
        semantic_prompt = detect_prompt_semantic(filepath)

        # Test d'affichage
        result = show_prompts(scored_prompts, semantic_prompt)

        assert isinstance(scored_prompts, list)
        assert isinstance(semantic_prompt, str)
        assert isinstance(result, str)
        assert len(result) > 0

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="# Documentation\n## Features\n### Security",
    )
    def test_markdown_prompt_workflow(self, mock_file):
        """Test du workflow pour les fichiers markdown"""
        filepath = "README.md"

        scored_prompts = detect_prompts_scoring(filepath)

        # Vérifier qu'au moins un prompt de design est détecté
        assert len(scored_prompts) > 0
        assert any(score > 0 for _, score in scored_prompts)

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="def refactor_function(): pass",
    )
    def test_refactor_prompt_workflow(self, mock_file):
        """Test du workflow pour les fichiers de refactorisation"""
        filepath = "utils.py"

        scored_prompts = detect_prompts_scoring(filepath)

        # Vérifier qu'au moins un prompt de refactorisation est détecté
        assert len(scored_prompts) > 0
        assert any(score > 0 for _, score in scored_prompts)
