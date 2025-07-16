import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import import_github_issues

def test_parse_issues():
    issues = import_github_issues.parse_issues(os.path.join(os.path.dirname(__file__), '../github_issues.md'))
    assert len(issues) > 0
    for iss in issues:
        assert 'title' in iss and 'body' in iss
