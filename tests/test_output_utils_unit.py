"""
Tests unitaires générés pour output_utils
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import output_utils
except ImportError:
    pytest.skip(f"Module output_utils non importable")


def test_build_announcements_section_content():
    """Test de la fonction build_announcements_section_content"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'build_announcements_section_content')
    assert callable(getattr(output_utils, 'build_announcements_section_content'))

def test_add_empty_line():
    """Test de la fonction add_empty_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'add_empty_line')
    assert callable(getattr(output_utils, 'add_empty_line'))

def test_style_lines():
    """Test de la fonction style_lines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'style_lines')
    assert callable(getattr(output_utils, 'style_lines'))

def test_format_vulnerability():
    """Test de la fonction format_vulnerability"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'format_vulnerability')
    assert callable(getattr(output_utils, 'format_vulnerability'))

def test_format_license():
    """Test de la fonction format_license"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'format_license')
    assert callable(getattr(output_utils, 'format_license'))

def test_get_fix_hint_for_unpinned():
    """Test de la fonction get_fix_hint_for_unpinned"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'get_fix_hint_for_unpinned')
    assert callable(getattr(output_utils, 'get_fix_hint_for_unpinned'))

def test_get_unpinned_hint():
    """Test de la fonction get_unpinned_hint"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'get_unpinned_hint')
    assert callable(getattr(output_utils, 'get_unpinned_hint'))

def test_get_specifier_range_info():
    """Test de la fonction get_specifier_range_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'get_specifier_range_info')
    assert callable(getattr(output_utils, 'get_specifier_range_info'))

def test_build_other_options_msg():
    """Test de la fonction build_other_options_msg"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'build_other_options_msg')
    assert callable(getattr(output_utils, 'build_other_options_msg'))

def test_build_remediation_section():
    """Test de la fonction build_remediation_section"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'build_remediation_section')
    assert callable(getattr(output_utils, 'build_remediation_section'))

def test_get_final_brief():
    """Test de la fonction get_final_brief"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'get_final_brief')
    assert callable(getattr(output_utils, 'get_final_brief'))

def test_get_final_brief_license():
    """Test de la fonction get_final_brief_license"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'get_final_brief_license')
    assert callable(getattr(output_utils, 'get_final_brief_license'))

def test_format_long_text():
    """Test de la fonction format_long_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'format_long_text')
    assert callable(getattr(output_utils, 'format_long_text'))

def test_get_printable_list_of_scanned_items():
    """Test de la fonction get_printable_list_of_scanned_items"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'get_printable_list_of_scanned_items')
    assert callable(getattr(output_utils, 'get_printable_list_of_scanned_items'))

def test_build_report_brief_section():
    """Test de la fonction build_report_brief_section"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'build_report_brief_section')
    assert callable(getattr(output_utils, 'build_report_brief_section'))

def test_build_report_for_review_vuln_report():
    """Test de la fonction build_report_for_review_vuln_report"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'build_report_for_review_vuln_report')
    assert callable(getattr(output_utils, 'build_report_for_review_vuln_report'))

def test_build_using_sentence():
    """Test de la fonction build_using_sentence"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'build_using_sentence')
    assert callable(getattr(output_utils, 'build_using_sentence'))

def test_build_scanned_count_sentence():
    """Test de la fonction build_scanned_count_sentence"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'build_scanned_count_sentence')
    assert callable(getattr(output_utils, 'build_scanned_count_sentence'))

def test_add_warnings_if_needed():
    """Test de la fonction add_warnings_if_needed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'add_warnings_if_needed')
    assert callable(getattr(output_utils, 'add_warnings_if_needed'))

def test_get_report_brief_info():
    """Test de la fonction get_report_brief_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'get_report_brief_info')
    assert callable(getattr(output_utils, 'get_report_brief_info'))

def test_build_primary_announcement():
    """Test de la fonction build_primary_announcement"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'build_primary_announcement')
    assert callable(getattr(output_utils, 'build_primary_announcement'))

def test_is_using_api_key():
    """Test de la fonction is_using_api_key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'is_using_api_key')
    assert callable(getattr(output_utils, 'is_using_api_key'))

def test_is_using_a_safety_policy_file():
    """Test de la fonction is_using_a_safety_policy_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'is_using_a_safety_policy_file')
    assert callable(getattr(output_utils, 'is_using_a_safety_policy_file'))

def test_should_add_nl():
    """Test de la fonction should_add_nl"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'should_add_nl')
    assert callable(getattr(output_utils, 'should_add_nl'))

def test_get_skip_reason():
    """Test de la fonction get_skip_reason"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'get_skip_reason')
    assert callable(getattr(output_utils, 'get_skip_reason'))

def test_get_applied_msg():
    """Test de la fonction get_applied_msg"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'get_applied_msg')
    assert callable(getattr(output_utils, 'get_applied_msg'))

def test_get_skipped_msg():
    """Test de la fonction get_skipped_msg"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'get_skipped_msg')
    assert callable(getattr(output_utils, 'get_skipped_msg'))

def test_get_fix_opt_used_msg():
    """Test de la fonction get_fix_opt_used_msg"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'get_fix_opt_used_msg')
    assert callable(getattr(output_utils, 'get_fix_opt_used_msg'))

def test_print_service():
    """Test de la fonction print_service"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'print_service')
    assert callable(getattr(output_utils, 'print_service'))

def test_prompt_service():
    """Test de la fonction prompt_service"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'prompt_service')
    assert callable(getattr(output_utils, 'prompt_service'))

def test_parse_html():
    """Test de la fonction parse_html"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'parse_html')
    assert callable(getattr(output_utils, 'parse_html'))

def test_format_unpinned_vulnerabilities():
    """Test de la fonction format_unpinned_vulnerabilities"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(output_utils, 'format_unpinned_vulnerabilities')
    assert callable(getattr(output_utils, 'format_unpinned_vulnerabilities'))

if __name__ == "__main__":
    pytest.main([__file__])
