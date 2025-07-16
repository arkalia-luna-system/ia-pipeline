import requests
import os
import re

GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
REPO = '<user>/<repo>'

def parse_issues(md_path):
    issues = []
    with open(md_path) as f:
        content = f.read()
    for match in re.finditer(r"## \[ \] Implémenter le module \*\*(.*?)\*\*([\s\S]*?)(?=##|$)", content):
        title = match.group(1)
        body = match.group(2).strip()
        issues.append({'title': title, 'body': body})
    return issues

def create_issue(title, body, dry_run=True):
    url = f'https://api.github.com/repos/{REPO}/issues'
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    data = {'title': title, 'body': body}
    if dry_run:
        print(f"[DRY RUN] Would create: {title}")
        return
    r = requests.post(url, headers=headers, json=data)
    print(r.status_code, r.json())

if __name__ == "__main__":
    issues = parse_issues("github_issues.md")
    for iss in issues:
        create_issue(iss['title'], iss['body'], dry_run=True)
