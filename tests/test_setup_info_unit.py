"""
Tests unitaires générés pour setup_info
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import setup_info
except ImportError:
    pytest.skip(f"Module setup_info non importable")


def test_pep517_subprocess_runner():
    """Test de la fonction pep517_subprocess_runner"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'pep517_subprocess_runner')
    assert callable(getattr(setup_info, 'pep517_subprocess_runner'))

def test_get_value_from_tuple():
    """Test de la fonction get_value_from_tuple"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'get_value_from_tuple')
    assert callable(getattr(setup_info, 'get_value_from_tuple'))

def test_is_readonly_path():
    """Test de la fonction is_readonly_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'is_readonly_path')
    assert callable(getattr(setup_info, 'is_readonly_path'))

def test_query_registry_value():
    """Test de la fonction query_registry_value"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'query_registry_value')
    assert callable(getattr(setup_info, 'query_registry_value'))

def test__find_icacls_exe():
    """Test de la fonction _find_icacls_exe"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, '_find_icacls_exe')
    assert callable(getattr(setup_info, '_find_icacls_exe'))

def test__walk_for_powershell():
    """Test de la fonction _walk_for_powershell"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, '_walk_for_powershell')
    assert callable(getattr(setup_info, '_walk_for_powershell'))

def test__get_powershell_path():
    """Test de la fonction _get_powershell_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, '_get_powershell_path')
    assert callable(getattr(setup_info, '_get_powershell_path'))

def test__get_sid_with_powershell():
    """Test de la fonction _get_sid_with_powershell"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, '_get_sid_with_powershell')
    assert callable(getattr(setup_info, '_get_sid_with_powershell'))

def test__get_sid_from_registry():
    """Test de la fonction _get_sid_from_registry"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, '_get_sid_from_registry')
    assert callable(getattr(setup_info, '_get_sid_from_registry'))

def test__get_current_user():
    """Test de la fonction _get_current_user"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, '_get_current_user')
    assert callable(getattr(setup_info, '_get_current_user'))

def test__wait_for_files():
    """Test de la fonction _wait_for_files"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, '_wait_for_files')
    assert callable(getattr(setup_info, '_wait_for_files'))

def test_set_write_bit():
    """Test de la fonction set_write_bit"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'set_write_bit')
    assert callable(getattr(setup_info, 'set_write_bit'))

def test_make_base_requirements():
    """Test de la fonction make_base_requirements"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'make_base_requirements')
    assert callable(getattr(setup_info, 'make_base_requirements'))

def test_handle_remove_readonly():
    """Test de la fonction handle_remove_readonly"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'handle_remove_readonly')
    assert callable(getattr(setup_info, 'handle_remove_readonly'))

def test_rmtree():
    """Test de la fonction rmtree"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'rmtree')
    assert callable(getattr(setup_info, 'rmtree'))

def test_suppress_unparsable():
    """Test de la fonction suppress_unparsable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'suppress_unparsable')
    assert callable(getattr(setup_info, 'suppress_unparsable'))

def test_setuptools_parse_setup_cfg():
    """Test de la fonction setuptools_parse_setup_cfg"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'setuptools_parse_setup_cfg')
    assert callable(getattr(setup_info, 'setuptools_parse_setup_cfg'))

def test_parse_setup_cfg():
    """Test de la fonction parse_setup_cfg"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'parse_setup_cfg')
    assert callable(getattr(setup_info, 'parse_setup_cfg'))

def test_build_pep517():
    """Test de la fonction build_pep517"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'build_pep517')
    assert callable(getattr(setup_info, 'build_pep517'))

def test__get_src_dir():
    """Test de la fonction _get_src_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, '_get_src_dir')
    assert callable(getattr(setup_info, '_get_src_dir'))

def test_ensure_reqs():
    """Test de la fonction ensure_reqs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'ensure_reqs')
    assert callable(getattr(setup_info, 'ensure_reqs'))

def test_any_valid_values():
    """Test de la fonction any_valid_values"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'any_valid_values')
    assert callable(getattr(setup_info, 'any_valid_values'))

def test__prepare_wheel_building_kwargs():
    """Test de la fonction _prepare_wheel_building_kwargs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, '_prepare_wheel_building_kwargs')
    assert callable(getattr(setup_info, '_prepare_wheel_building_kwargs'))

def test__is_venv_dir():
    """Test de la fonction _is_venv_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, '_is_venv_dir')
    assert callable(getattr(setup_info, '_is_venv_dir'))

def test_iter_metadata():
    """Test de la fonction iter_metadata"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'iter_metadata')
    assert callable(getattr(setup_info, 'iter_metadata'))

def test_find_egginfo():
    """Test de la fonction find_egginfo"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'find_egginfo')
    assert callable(getattr(setup_info, 'find_egginfo'))

def test_find_distinfo():
    """Test de la fonction find_distinfo"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'find_distinfo')
    assert callable(getattr(setup_info, 'find_distinfo'))

def test_get_distinfo_dist():
    """Test de la fonction get_distinfo_dist"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'get_distinfo_dist')
    assert callable(getattr(setup_info, 'get_distinfo_dist'))

def test_get_egginfo_dist():
    """Test de la fonction get_egginfo_dist"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'get_egginfo_dist')
    assert callable(getattr(setup_info, 'get_egginfo_dist'))

def test_get_metadata():
    """Test de la fonction get_metadata"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'get_metadata')
    assert callable(getattr(setup_info, 'get_metadata'))

def test_get_extra_name_from_marker():
    """Test de la fonction get_extra_name_from_marker"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'get_extra_name_from_marker')
    assert callable(getattr(setup_info, 'get_extra_name_from_marker'))

def test_get_metadata_from_wheel():
    """Test de la fonction get_metadata_from_wheel"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'get_metadata_from_wheel')
    assert callable(getattr(setup_info, 'get_metadata_from_wheel'))

def test_get_metadata_from_dist():
    """Test de la fonction get_metadata_from_dist"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'get_metadata_from_dist')
    assert callable(getattr(setup_info, 'get_metadata_from_dist'))

def test_ast_parse_setup_py():
    """Test de la fonction ast_parse_setup_py"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'ast_parse_setup_py')
    assert callable(getattr(setup_info, 'ast_parse_setup_py'))

def test_run_setup():
    """Test de la fonction run_setup"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'run_setup')
    assert callable(getattr(setup_info, 'run_setup'))

def test_pip_install():
    """Test de la fonction pip_install"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'pip_install')
    assert callable(getattr(setup_info, 'pip_install'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, '__init__')
    assert callable(getattr(setup_info, '__init__'))

def test_read_setup_py():
    """Test de la fonction read_setup_py"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'read_setup_py')
    assert callable(getattr(setup_info, 'read_setup_py'))

def test_read_setup_cfg():
    """Test de la fonction read_setup_cfg"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'read_setup_cfg')
    assert callable(getattr(setup_info, 'read_setup_cfg'))

def test__find_setup_call():
    """Test de la fonction _find_setup_call"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, '_find_setup_call')
    assert callable(getattr(setup_info, '_find_setup_call'))

def test__find_sub_setup_call():
    """Test de la fonction _find_sub_setup_call"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, '_find_sub_setup_call')
    assert callable(getattr(setup_info, '_find_sub_setup_call'))

def test__find_install_requires():
    """Test de la fonction _find_install_requires"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, '_find_install_requires')
    assert callable(getattr(setup_info, '_find_install_requires'))

def test__find_extras_require():
    """Test de la fonction _find_extras_require"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, '_find_extras_require')
    assert callable(getattr(setup_info, '_find_extras_require'))

def test__find_single_string():
    """Test de la fonction _find_single_string"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, '_find_single_string')
    assert callable(getattr(setup_info, '_find_single_string'))

def test__find_in_call():
    """Test de la fonction _find_in_call"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, '_find_in_call')
    assert callable(getattr(setup_info, '_find_in_call'))

def test__find_call_kwargs():
    """Test de la fonction _find_call_kwargs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, '_find_call_kwargs')
    assert callable(getattr(setup_info, '_find_call_kwargs'))

def test__find_variable_in_body():
    """Test de la fonction _find_variable_in_body"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, '_find_variable_in_body')
    assert callable(getattr(setup_info, '_find_variable_in_body'))

def test__find_in_dict():
    """Test de la fonction _find_in_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, '_find_in_dict')
    assert callable(getattr(setup_info, '_find_in_dict'))

def test_is_valid():
    """Test de la fonction is_valid"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'is_valid')
    assert callable(getattr(setup_info, 'is_valid'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, '__init__')
    assert callable(getattr(setup_info, '__init__'))

def test___next__():
    """Test de la fonction __next__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, '__next__')
    assert callable(getattr(setup_info, '__next__'))

def test___iter__():
    """Test de la fonction __iter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, '__iter__')
    assert callable(getattr(setup_info, '__iter__'))

def test_next():
    """Test de la fonction next"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'next')
    assert callable(getattr(setup_info, 'next'))

def test_close():
    """Test de la fonction close"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'close')
    assert callable(getattr(setup_info, 'close'))

def test___setattr__():
    """Test de la fonction __setattr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, '__setattr__')
    assert callable(getattr(setup_info, '__setattr__'))

def test___str__():
    """Test de la fonction __str__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, '__str__')
    assert callable(getattr(setup_info, '__str__'))

def test___hash__():
    """Test de la fonction __hash__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, '__hash__')
    assert callable(getattr(setup_info, '__hash__'))

def test_as_dict():
    """Test de la fonction as_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'as_dict')
    assert callable(getattr(setup_info, 'as_dict'))

def test_as_tuple():
    """Test de la fonction as_tuple"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'as_tuple')
    assert callable(getattr(setup_info, 'as_tuple'))

def test_from_string():
    """Test de la fonction from_string"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'from_string')
    assert callable(getattr(setup_info, 'from_string'))

def test_from_req():
    """Test de la fonction from_req"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'from_req')
    assert callable(getattr(setup_info, 'from_req'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, '__init__')
    assert callable(getattr(setup_info, '__init__'))

def test___hash__():
    """Test de la fonction __hash__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, '__hash__')
    assert callable(getattr(setup_info, '__hash__'))

def test___eq__():
    """Test de la fonction __eq__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, '__eq__')
    assert callable(getattr(setup_info, '__eq__'))

def test_requires():
    """Test de la fonction requires"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'requires')
    assert callable(getattr(setup_info, 'requires'))

def test_extras():
    """Test de la fonction extras"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'extras')
    assert callable(getattr(setup_info, 'extras'))

def test_version():
    """Test de la fonction version"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'version')
    assert callable(getattr(setup_info, 'version'))

def test_egg_base():
    """Test de la fonction egg_base"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'egg_base')
    assert callable(getattr(setup_info, 'egg_base'))

def test_update_from_dict():
    """Test de la fonction update_from_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'update_from_dict')
    assert callable(getattr(setup_info, 'update_from_dict'))

def test_get_extras_from_ireq():
    """Test de la fonction get_extras_from_ireq"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'get_extras_from_ireq')
    assert callable(getattr(setup_info, 'get_extras_from_ireq'))

def test_parse_setup_cfg():
    """Test de la fonction parse_setup_cfg"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'parse_setup_cfg')
    assert callable(getattr(setup_info, 'parse_setup_cfg'))

def test_parse_setup_py():
    """Test de la fonction parse_setup_py"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'parse_setup_py')
    assert callable(getattr(setup_info, 'parse_setup_py'))

def test_run_setup():
    """Test de la fonction run_setup"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'run_setup')
    assert callable(getattr(setup_info, 'run_setup'))

def test_pep517_config():
    """Test de la fonction pep517_config"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'pep517_config')
    assert callable(getattr(setup_info, 'pep517_config'))

def test_build_wheel():
    """Test de la fonction build_wheel"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'build_wheel')
    assert callable(getattr(setup_info, 'build_wheel'))

def test_build_sdist():
    """Test de la fonction build_sdist"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'build_sdist')
    assert callable(getattr(setup_info, 'build_sdist'))

def test_build():
    """Test de la fonction build"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'build')
    assert callable(getattr(setup_info, 'build'))

def test_get_metadata_from_wheel():
    """Test de la fonction get_metadata_from_wheel"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'get_metadata_from_wheel')
    assert callable(getattr(setup_info, 'get_metadata_from_wheel'))

def test_get_egg_metadata():
    """Test de la fonction get_egg_metadata"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'get_egg_metadata')
    assert callable(getattr(setup_info, 'get_egg_metadata'))

def test_populate_metadata():
    """Test de la fonction populate_metadata"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'populate_metadata')
    assert callable(getattr(setup_info, 'populate_metadata'))

def test_run_pyproject():
    """Test de la fonction run_pyproject"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'run_pyproject')
    assert callable(getattr(setup_info, 'run_pyproject'))

def test_get_initial_info():
    """Test de la fonction get_initial_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'get_initial_info')
    assert callable(getattr(setup_info, 'get_initial_info'))

def test_get_info():
    """Test de la fonction get_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'get_info')
    assert callable(getattr(setup_info, 'get_info'))

def test_as_dict():
    """Test de la fonction as_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'as_dict')
    assert callable(getattr(setup_info, 'as_dict'))

def test_from_requirement():
    """Test de la fonction from_requirement"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'from_requirement')
    assert callable(getattr(setup_info, 'from_requirement'))

def test_from_ireq():
    """Test de la fonction from_ireq"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'from_ireq')
    assert callable(getattr(setup_info, 'from_ireq'))

def test_create():
    """Test de la fonction create"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'create')
    assert callable(getattr(setup_info, 'create'))

def test_caller():
    """Test de la fonction caller"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setup_info, 'caller')
    assert callable(getattr(setup_info, 'caller'))

class TestBuildEnv:
    """Tests pour la classe BuildEnv"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(setup_info, 'BuildEnv')
        assert isinstance(getattr(setup_info, 'BuildEnv'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(setup_info, 'BuildEnv')
        for method_name in ['pip_install']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestHookCaller:
    """Tests pour la classe HookCaller"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(setup_info, 'HookCaller')
        assert isinstance(getattr(setup_info, 'HookCaller'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(setup_info, 'HookCaller')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestUnparsable:
    """Tests pour la classe Unparsable"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(setup_info, 'Unparsable')
        assert isinstance(getattr(setup_info, 'Unparsable'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(setup_info, 'Unparsable')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSetupReader:
    """Tests pour la classe SetupReader"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(setup_info, 'SetupReader')
        assert isinstance(getattr(setup_info, 'SetupReader'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(setup_info, 'SetupReader')
        for method_name in ['read_setup_py', 'read_setup_cfg', '_find_setup_call', '_find_sub_setup_call', '_find_install_requires', '_find_extras_require', '_find_single_string', '_find_in_call', '_find_call_kwargs', '_find_variable_in_body', '_find_in_dict']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestScandirCloser:
    """Tests pour la classe ScandirCloser"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(setup_info, 'ScandirCloser')
        assert isinstance(getattr(setup_info, 'ScandirCloser'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(setup_info, 'ScandirCloser')
        for method_name in ['__init__', '__next__', '__iter__', 'next', 'close']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestBaseRequirement:
    """Tests pour la classe BaseRequirement"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(setup_info, 'BaseRequirement')
        assert isinstance(getattr(setup_info, 'BaseRequirement'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(setup_info, 'BaseRequirement')
        for method_name in ['__setattr__', '__str__', '__hash__', 'as_dict', 'as_tuple', 'from_string', 'from_req']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSetupInfo:
    """Tests pour la classe SetupInfo"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(setup_info, 'SetupInfo')
        assert isinstance(getattr(setup_info, 'SetupInfo'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(setup_info, 'SetupInfo')
        for method_name in ['__init__', '__hash__', '__eq__', 'requires', 'extras', 'version', 'egg_base', 'update_from_dict', 'get_extras_from_ireq', 'parse_setup_cfg', 'parse_setup_py', 'run_setup', 'pep517_config', 'build_wheel', 'build_sdist', 'build', 'get_metadata_from_wheel', 'get_egg_metadata', 'populate_metadata', 'run_pyproject', 'get_initial_info', 'get_info', 'as_dict', 'from_requirement', 'from_ireq', 'create']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestConfig:
    """Tests pour la classe Config"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(setup_info, 'Config')
        assert isinstance(getattr(setup_info, 'Config'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(setup_info, 'Config')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestConfig:
    """Tests pour la classe Config"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(setup_info, 'Config')
        assert isinstance(getattr(setup_info, 'Config'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(setup_info, 'Config')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
