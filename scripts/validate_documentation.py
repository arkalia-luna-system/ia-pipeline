#!/usr/bin/env python3
"""
🔍 ATHALIA DOCUMENTATION VALIDATOR
Professional documentation quality assurance tool
"""

import os
import re
import sys
import json
import requests
from pathlib import Path
from typing import Dict, List, Tuple, Any
from datetime import datetime
import argparse

class DocumentationValidator:
    """Professional documentation validation tool."""
    
    def __init__(self, docs_path: str = "docs"):
        self.docs_path = Path(docs_path)
        self.issues = []
        self.stats = {
            'total_files': 0,
            'files_with_diagrams': 0,
            'files_with_code': 0,
            'files_with_badges': 0,
            'broken_links': 0,
            'missing_headers': 0,
            'quality_score': 0
        }
        
    def validate_all(self) -> Dict[str, Any]:
        """Run complete validation suite."""
        print("🔍 ATHALIA DOCUMENTATION VALIDATION")
        print("=" * 50)
        
        # Collect all markdown files
        md_files = list(self.docs_path.rglob("*.md"))
        md_files.extend(Path(".").glob("*.md"))
        
        self.stats['total_files'] = len(md_files)
        print(f"📁 Found {len(md_files)} markdown files")
        
        # Validate each file
        for md_file in md_files:
            self._validate_file(md_file)
        
        # Calculate quality score
        self._calculate_quality_score()
        
        # Generate report
        report = self._generate_report()
        
        print("\n" + "=" * 50)
        print(f"🎯 QUALITY SCORE: {self.stats['quality_score']:.1f}/100")
        
        return report
    
    def _validate_file(self, file_path: Path):
        """Validate individual markdown file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for required elements
            self._check_header_structure(file_path, content)
            self._check_mermaid_diagrams(file_path, content)
            self._check_code_blocks(file_path, content)
            self._check_badges(file_path, content)
            self._check_links(file_path, content)
            self._check_professional_elements(file_path, content)
            
        except Exception as e:
            self.issues.append({
                'file': str(file_path),
                'type': 'file_error',
                'message': f"Error reading file: {e}",
                'severity': 'high'
            })
    
    def _check_header_structure(self, file_path: Path, content: str):
        """Check markdown header structure."""
        lines = content.split('\n')
        
        # Check for H1 header
        h1_found = False
        for line in lines[:10]:  # Check first 10 lines
            if line.startswith('# '):
                h1_found = True
                break
        
        if not h1_found:
            self.issues.append({
                'file': str(file_path),
                'type': 'missing_h1',
                'message': "Missing H1 header in first 10 lines",
                'severity': 'medium'
            })
            self.stats['missing_headers'] += 1
        
        # Check header hierarchy
        prev_level = 0
        for i, line in enumerate(lines):
            if line.startswith('#'):
                level = len(line) - len(line.lstrip('#'))
                if level > prev_level + 1:
                    self.issues.append({
                        'file': str(file_path),
                        'type': 'header_hierarchy',
                        'message': f"Header hierarchy skip at line {i+1}: {line[:50]}",
                        'severity': 'low'
                    })
                prev_level = level
    
    def _check_mermaid_diagrams(self, file_path: Path, content: str):
        """Check for Mermaid diagrams."""
        mermaid_count = content.count('```mermaid')
        
        if mermaid_count > 0:
            self.stats['files_with_diagrams'] += 1
            
            # Check if diagrams are properly closed
            code_block_closes = content.count('```')
            if mermaid_count * 2 > code_block_closes:
                self.issues.append({
                    'file': str(file_path),
                    'type': 'unclosed_mermaid',
                    'message': f"Mermaid diagrams not properly closed ({mermaid_count} opened)",
                    'severity': 'high'
                })
            
            # Check for theme configuration
            if '%%{init:' not in content and mermaid_count > 0:
                self.issues.append({
                    'file': str(file_path),
                    'type': 'missing_mermaid_theme',
                    'message': "Mermaid diagrams missing theme configuration",
                    'severity': 'low'
                })
    
    def _check_code_blocks(self, file_path: Path, content: str):
        """Check for code blocks."""
        code_patterns = [
            r'```python',
            r'```bash',
            r'```yaml',
            r'```json'
        ]
        
        code_found = any(re.search(pattern, content) for pattern in code_patterns)
        if code_found:
            self.stats['files_with_code'] += 1
            
            # Check for proper code block closure
            total_blocks = content.count('```')
            if total_blocks % 2 != 0:
                self.issues.append({
                    'file': str(file_path),
                    'type': 'unclosed_code_block',
                    'message': "Code blocks not properly closed",
                    'severity': 'high'
                })
    
    def _check_badges(self, file_path: Path, content: str):
        """Check for professional badges."""
        badge_patterns = [
            r'!\[.*\]\(https://img\.shields\.io',
            r'<div align="center">',
            r'style=for-the-badge',
            r'style=flat-square'
        ]
        
        badge_found = any(re.search(pattern, content) for pattern in badge_patterns)
        if badge_found:
            self.stats['files_with_badges'] += 1
    
    def _check_links(self, file_path: Path, content: str):
        """Check for broken internal links."""
        # Find markdown links
        link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        links = re.findall(link_pattern, content)
        
        for link_text, link_url in links:
            # Skip external links
            if link_url.startswith(('http://', 'https://', 'mailto:')):
                continue
            
            # Check internal file links
            if link_url.endswith('.md'):
                target_file = file_path.parent / link_url
                if not target_file.exists():
                    self.issues.append({
                        'file': str(file_path),
                        'type': 'broken_link',
                        'message': f"Broken link: {link_url}",
                        'severity': 'medium'
                    })
                    self.stats['broken_links'] += 1
    
    def _check_professional_elements(self, file_path: Path, content: str):
        """Check for professional documentation elements."""
        professional_elements = [
            ('centered_div', r'<div align="center">', 'Missing centered layouts'),
            ('structured_tables', r'\|.*\|.*\|', 'No structured tables found'),
            ('emoji_headers', r'^#{1,6}\s+[🎯🔍📊🚀⚡🔧]', 'Missing emoji in headers'),
            ('emphasis_text', r'\*\*[^*]+\*\*', 'Missing bold emphasis'),
            ('navigation_links', r'^\s*-\s+\[', 'Missing navigation links')
        ]
        
        for element_name, pattern, message in professional_elements:
            if not re.search(pattern, content, re.MULTILINE):
                if file_path.name not in ['README.md', 'INDEX.md']:  # Skip for main files
                    continue
                    
                self.issues.append({
                    'file': str(file_path),
                    'type': f'missing_{element_name}',
                    'message': message,
                    'severity': 'low'
                })
    
    def _calculate_quality_score(self):
        """Calculate overall quality score."""
        total_files = self.stats['total_files']
        if total_files == 0:
            self.stats['quality_score'] = 0
            return
        
        # Base scores
        diagram_score = (self.stats['files_with_diagrams'] / total_files) * 30
        code_score = (self.stats['files_with_code'] / total_files) * 25
        badge_score = (self.stats['files_with_badges'] / total_files) * 20
        
        # Penalty for issues
        high_severity_penalty = len([i for i in self.issues if i['severity'] == 'high']) * 5
        medium_severity_penalty = len([i for i in self.issues if i['severity'] == 'medium']) * 2
        low_severity_penalty = len([i for i in self.issues if i['severity'] == 'low']) * 0.5
        
        total_penalty = high_severity_penalty + medium_severity_penalty + low_severity_penalty
        
        # Calculate final score
        base_score = diagram_score + code_score + badge_score + 25  # 25 for baseline
        final_score = max(0, base_score - total_penalty)
        
        self.stats['quality_score'] = min(100, final_score)
    
    def _generate_report(self) -> Dict[str, Any]:
        """Generate comprehensive validation report."""
        return {
            'timestamp': datetime.now().isoformat(),
            'stats': self.stats,
            'issues': self.issues,
            'recommendations': self._generate_recommendations()
        }
    
    def _generate_recommendations(self) -> List[str]:
        """Generate improvement recommendations."""
        recommendations = []
        
        total_files = self.stats['total_files']
        diagram_ratio = self.stats['files_with_diagrams'] / total_files if total_files > 0 else 0
        code_ratio = self.stats['files_with_code'] / total_files if total_files > 0 else 0
        badge_ratio = self.stats['files_with_badges'] / total_files if total_files > 0 else 0
        
        if diagram_ratio < 0.3:
            recommendations.append("🔴 Add more Mermaid diagrams (target: 30%+ of files)")
        
        if code_ratio < 0.4:
            recommendations.append("🟡 Include more code examples (target: 40%+ of files)")
        
        if badge_ratio < 0.2:
            recommendations.append("🟡 Add professional badges to key documents")
        
        if self.stats['broken_links'] > 0:
            recommendations.append(f"🔴 Fix {self.stats['broken_links']} broken internal links")
        
        high_issues = len([i for i in self.issues if i['severity'] == 'high'])
        if high_issues > 0:
            recommendations.append(f"🔴 Resolve {high_issues} high-severity issues")
        
        if self.stats['quality_score'] < 80:
            recommendations.append("🟡 Overall quality below 80% - review all recommendations")
        
        return recommendations

def create_quality_report(validator: DocumentationValidator, output_file: str = "doc_quality_report.json"):
    """Create detailed quality report."""
    report = validator.validate_all()
    
    # Save JSON report
    with open(output_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    # Create markdown summary
    md_report = f"""# 📊 Documentation Quality Report

**Generated:** {report['timestamp']}  
**Quality Score:** {report['stats']['quality_score']:.1f}/100

## 📈 Statistics

| Metric | Value | Percentage |
|--------|-------|------------|
| Total Files | {report['stats']['total_files']} | 100% |
| Files with Diagrams | {report['stats']['files_with_diagrams']} | {(report['stats']['files_with_diagrams']/report['stats']['total_files']*100):.1f}% |
| Files with Code | {report['stats']['files_with_code']} | {(report['stats']['files_with_code']/report['stats']['total_files']*100):.1f}% |
| Files with Badges | {report['stats']['files_with_badges']} | {(report['stats']['files_with_badges']/report['stats']['total_files']*100):.1f}% |

## ⚠️ Issues Found

**Total Issues:** {len(report['issues'])}
- High Severity: {len([i for i in report['issues'] if i['severity'] == 'high'])}
- Medium Severity: {len([i for i in report['issues'] if i['severity'] == 'medium'])}
- Low Severity: {len([i for i in report['issues'] if i['severity'] == 'low'])}

## 🎯 Recommendations

"""
    
    for rec in report['recommendations']:
        md_report += f"- {rec}\n"
    
    md_report += f"""
## 🔧 Next Steps

1. Review high-severity issues first
2. Add missing Mermaid diagrams
3. Include more code examples
4. Fix broken links
5. Re-run validation

---

*Report generated by Athalia Documentation Validator*
"""
    
    with open("doc_quality_report.md", 'w') as f:
        f.write(md_report)
    
    print(f"\n📊 Reports saved:")
    print(f"   - JSON: {output_file}")
    print(f"   - Markdown: doc_quality_report.md")

def main():
    """Main validation entry point."""
    parser = argparse.ArgumentParser(description='Validate Athalia documentation quality')
    parser.add_argument('--docs-path', default='docs', help='Path to documentation directory')
    parser.add_argument('--output', default='doc_quality_report.json', help='Output report file')
    parser.add_argument('--fix', action='store_true', help='Attempt to fix common issues')
    parser.add_argument('--threshold', type=float, default=80.0, help='Quality threshold for pass/fail')
    
    args = parser.parse_args()
    
    # Run validation
    validator = DocumentationValidator(args.docs_path)
    create_quality_report(validator, args.output)
    
    # Check threshold
    quality_score = validator.stats['quality_score']
    if quality_score >= args.threshold:
        print(f"\n✅ PASS: Quality score {quality_score:.1f} meets threshold {args.threshold}")
        sys.exit(0)
    else:
        print(f"\n❌ FAIL: Quality score {quality_score:.1f} below threshold {args.threshold}")
        sys.exit(1)

if __name__ == "__main__":
    main()