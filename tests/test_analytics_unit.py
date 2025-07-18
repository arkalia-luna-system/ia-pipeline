import unittest
from unittest.mock import patch
from athalia_core import analytics

class TestAnalytics(unittest.TestCase):
    def setUp(self):
        # Exemple de données de projet
        self.projects_info = [
            {'name': 'ProjetA'},
            {'name': 'ProjetB'}
        ]

    @patch('athalia_core.analytics.audit_project_intelligent')
    def test_generate_heatmap_data(self, mock_audit):
        mock_audit.side_effect = lambda name: {
            'global_score': 75 if name == 'ProjetA' else 90,
            'metrics': {
                'structure_score': 80,
                'code_score': 70,
                'test_score': 60,
                'doc_score': 50,
                'security_score': 90,
                'perf_score': 85
            }
        }
        data = analytics.generate_heatmap_data(self.projects_info)
        self.assertIn('labels', data)
        self.assertIn('datasets', data)
        self.assertEqual(len(data['labels']), 2)
        self.assertEqual(len(data['datasets']), 2)
        self.assertEqual(data['datasets'][0]['global_score'], 75)
        self.assertEqual(data['datasets'][1]['global_score'], 90)

    @patch('athalia_core.analytics.audit_project_intelligent')
    def test_generate_technical_debt_analysis(self, mock_audit):
        mock_audit.side_effect = lambda name: {
            'global_score': 85 if name == 'ProjetA' else 35,
            'issues': ['Sécurité: mot de passe faible', 'Tests: couverture faible'],
            'suggestions': ['Ajouter des tests', 'Renforcer la sécurité']
        }
        data = analytics.generate_technical_debt_analysis(self.projects_info)
        self.assertIn('total_projects', data)
        self.assertEqual(data['total_projects'], 2)
        self.assertIn('average_score', data)
        self.assertIn('score_distribution', data)
        self.assertEqual(data['score_distribution']['excellent'], 1)
        self.assertEqual(data['score_distribution']['critical'], 1)
        self.assertIn('common_issues', data)
        self.assertIn('Sécurité', data['common_issues'])
        self.assertIn('Tests', data['common_issues'])
        self.assertIn('top_suggestions', data)
        self.assertTrue(any('Ajouter des tests' in s for s, _ in data['top_suggestions']))

    @patch('athalia_core.analytics.generate_heatmap_data')
    @patch('athalia_core.analytics.generate_technical_debt_analysis')
    def test_generate_analytics_html(self, mock_debt, mock_heatmap):
        mock_heatmap.return_value = {'labels': ['ProjetA'], 'datasets': [{'project': 'ProjetA', 'global_score': 80, 'metrics': {}}]}
        mock_debt.return_value = {
            'total_projects': 1,
            'average_score': 80,
            'score_distribution': {'excellent': 1, 'good': 0, 'medium': 0, 'critical': 0},
            'common_issues': {'Sécurité': 2},
            'top_suggestions': [('Ajouter des tests', 2)]
        }
        html = analytics.generate_analytics_html(self.projects_info)
        self.assertIn('<html>', html)
        self.assertIn('Analytics IA', html)
        self.assertIn('ProjetA', html)
        self.assertIn('Ajouter des tests', html)

    def test_analyze_project(self):
        import tempfile
        import os
        with tempfile.TemporaryDirectory() as tmpdir:
            # Créer des fichiers de test
            open(os.path.join(tmpdir, 'main.py'), 'w').close()
            open(os.path.join(tmpdir, 'test_module.py'), 'w').close()
            open(os.path.join(tmpdir, 'README.md'), 'w').close()
            os.mkdir(os.path.join(tmpdir, 'subdir'))
            report = analytics.analyze_project(tmpdir)
            self.assertEqual(report['total_files'], 3)
            self.assertEqual(report['python_files'], 2)
            self.assertEqual(report['test_files'], 1)
            self.assertEqual(report['md_files'], 1)
            self.assertEqual(report['dirs'], 1)

if __name__ == "__main__":
    unittest.main() 