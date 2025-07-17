#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import shutil
import pytest
import tempfile
from athalia_core.analytics import (
    generate_heatmap_data,
    generate_technical_debt_analysis,
    generate_analytics_html,
    save_analytics,
    analyze_project
)

"""
Tests pour le module d'analytics IA.
"""

def test_generate_heatmap_data():
    """Test la génération des données de heatmap."""
    projects_info = [
        {'name': 'test_project_1'},
        {'name': 'test_project_2'}
    ]

    heatmap_data = generate_heatmap_data(projects_info)

    assert 'labels' in heatmap_data
    assert 'datasets' in heatmap_data
    assert len(heatmap_data['labels']) == 2
    assert len(heatmap_data['datasets']) == 2

def test_generate_technical_debt_analysis():
    """Test l'analyse de la dette technique."""
    projects_info = [
        {'name': 'test_project_1'},
        {'name': 'test_project_2'}
    ]

    debt_analysis = generate_technical_debt_analysis(projects_info)

    assert 'total_projects' in debt_analysis
    assert 'average_score' in debt_analysis
    assert 'score_distribution' in debt_analysis
    assert 'common_issues' in debt_analysis
    assert 'top_suggestions' in debt_analysis

    assert debt_analysis['total_projects'] == 2
    assert isinstance(debt_analysis['average_score'], (int, float))

def test_generate_analytics_html():
    """Test la génération du HTML d'analytics."""
    projects_info = [
        {'name': 'test_project_1'},
        {'name': 'test_project_2'}
    ]

    html = generate_analytics_html(projects_info)

    assert 'Analytics IA' in html
    assert 'chart.js' in html
    assert 'heatmapChart' in html
    assert 'issuesChart' in html

def test_save_analytics():
    """Test la sauvegarde des analytics."""
    projects_info = [
        {'name': 'test_project_1'},
        {'name': 'test_project_2'}
    ]

    temp_dir = tempfile.mkdtemp()
    output_file = os.path.join(temp_dir, 'test_analytics.html')

    try:
        result = save_analytics(projects_info, output_file)

        assert result == output_file
        assert os.path.exists(output_file)

        # Vérifier le contenu
        with open(output_file, 'r') as file_handle:
            content = file_handle.read()
            assert 'Analytics IA' in content
            assert 'chart.js' in content

    finally:
        shutil.rmtree(temp_dir)

def test_analytics_with_real_projects():
    """Test les analytics avec de vrais projets existants."""
    # Utiliser des projets existants pour le test
    real_projects = []
    for data in os.listdir('.'):
        if os.path.isdir(data) and (data.startswith('ia_project') or data.startswith('projet_')):
            real_projects.append({'name': data})

    if len(real_projects) >= 2:
        # Test avec de vrais projets
        heatmap_data = generate_heatmap_data(real_projects[:2])
        debt_analysis = generate_technical_debt_analysis(real_projects[:2])

        assert len(heatmap_data['labels']) >= 1
        assert debt_analysis['total_projects'] >= 1
        assert isinstance(debt_analysis['average_score'], (int, float))

        print(f"✅ Analytics testés sur {len(real_projects[:2])} projets")
    else:
        pytest.skip("Pas assez de projets réels pour tester")

def test_analyze_project():
    with tempfile.TemporaryDirectory() as temp_dir:
        os.mkdir(os.path.join(temp_dir, 'src'))
        with open(os.path.join(temp_dir, 'src', 'main.py'), 'w') as file_handle:
            file_handle.write('print("Hello")')
        with open(os.path.join(temp_dir, 'README.md'), 'w') as file_handle:
            file_handle.write('# Doc')
        with open(os.path.join(temp_dir, 'test_utils.py'), 'w') as file_handle:
            file_handle.write('def test_x(): pass')
        report = analyze_project(temp_dir)
        assert report['total_files'] == 3
        assert report['python_files'] == 2
        assert report['test_files'] == 1
        assert report['md_files'] == 1
        assert report['dirs'] == 1