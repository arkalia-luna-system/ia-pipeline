"""
Tests unitaires générés pour cpuinfo
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import cpuinfo
except ImportError:
    pytest.skip(f"Module cpuinfo non importable")


def test_getoutput():
    """Test de la fonction getoutput"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, 'getoutput')
    assert callable(getattr(cpuinfo, 'getoutput'))

def test_command_info():
    """Test de la fonction command_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, 'command_info')
    assert callable(getattr(cpuinfo, 'command_info'))

def test_command_by_line():
    """Test de la fonction command_by_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, 'command_by_line')
    assert callable(getattr(cpuinfo, 'command_by_line'))

def test_key_value_from_command():
    """Test de la fonction key_value_from_command"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, 'key_value_from_command')
    assert callable(getattr(cpuinfo, 'key_value_from_command'))

def test__try_call():
    """Test de la fonction _try_call"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_try_call')
    assert callable(getattr(cpuinfo, '_try_call'))

def test___getattr__():
    """Test de la fonction __getattr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '__getattr__')
    assert callable(getattr(cpuinfo, '__getattr__'))

def test__getNCPUs():
    """Test de la fonction _getNCPUs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_getNCPUs')
    assert callable(getattr(cpuinfo, '_getNCPUs'))

def test___get_nbits():
    """Test de la fonction __get_nbits"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '__get_nbits')
    assert callable(getattr(cpuinfo, '__get_nbits'))

def test__is_32bit():
    """Test de la fonction _is_32bit"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_32bit')
    assert callable(getattr(cpuinfo, '_is_32bit'))

def test__is_64bit():
    """Test de la fonction _is_64bit"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_64bit')
    assert callable(getattr(cpuinfo, '_is_64bit'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '__init__')
    assert callable(getattr(cpuinfo, '__init__'))

def test__not_impl():
    """Test de la fonction _not_impl"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_not_impl')
    assert callable(getattr(cpuinfo, '_not_impl'))

def test__is_AMD():
    """Test de la fonction _is_AMD"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_AMD')
    assert callable(getattr(cpuinfo, '_is_AMD'))

def test__is_AthlonK6_2():
    """Test de la fonction _is_AthlonK6_2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_AthlonK6_2')
    assert callable(getattr(cpuinfo, '_is_AthlonK6_2'))

def test__is_AthlonK6_3():
    """Test de la fonction _is_AthlonK6_3"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_AthlonK6_3')
    assert callable(getattr(cpuinfo, '_is_AthlonK6_3'))

def test__is_AthlonK6():
    """Test de la fonction _is_AthlonK6"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_AthlonK6')
    assert callable(getattr(cpuinfo, '_is_AthlonK6'))

def test__is_AthlonK7():
    """Test de la fonction _is_AthlonK7"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_AthlonK7')
    assert callable(getattr(cpuinfo, '_is_AthlonK7'))

def test__is_AthlonMP():
    """Test de la fonction _is_AthlonMP"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_AthlonMP')
    assert callable(getattr(cpuinfo, '_is_AthlonMP'))

def test__is_AMD64():
    """Test de la fonction _is_AMD64"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_AMD64')
    assert callable(getattr(cpuinfo, '_is_AMD64'))

def test__is_Athlon64():
    """Test de la fonction _is_Athlon64"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_Athlon64')
    assert callable(getattr(cpuinfo, '_is_Athlon64'))

def test__is_AthlonHX():
    """Test de la fonction _is_AthlonHX"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_AthlonHX')
    assert callable(getattr(cpuinfo, '_is_AthlonHX'))

def test__is_Opteron():
    """Test de la fonction _is_Opteron"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_Opteron')
    assert callable(getattr(cpuinfo, '_is_Opteron'))

def test__is_Hammer():
    """Test de la fonction _is_Hammer"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_Hammer')
    assert callable(getattr(cpuinfo, '_is_Hammer'))

def test__is_Alpha():
    """Test de la fonction _is_Alpha"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_Alpha')
    assert callable(getattr(cpuinfo, '_is_Alpha'))

def test__is_EV4():
    """Test de la fonction _is_EV4"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_EV4')
    assert callable(getattr(cpuinfo, '_is_EV4'))

def test__is_EV5():
    """Test de la fonction _is_EV5"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_EV5')
    assert callable(getattr(cpuinfo, '_is_EV5'))

def test__is_EV56():
    """Test de la fonction _is_EV56"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_EV56')
    assert callable(getattr(cpuinfo, '_is_EV56'))

def test__is_PCA56():
    """Test de la fonction _is_PCA56"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_PCA56')
    assert callable(getattr(cpuinfo, '_is_PCA56'))

def test__is_Intel():
    """Test de la fonction _is_Intel"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_Intel')
    assert callable(getattr(cpuinfo, '_is_Intel'))

def test__is_i486():
    """Test de la fonction _is_i486"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_i486')
    assert callable(getattr(cpuinfo, '_is_i486'))

def test__is_i586():
    """Test de la fonction _is_i586"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_i586')
    assert callable(getattr(cpuinfo, '_is_i586'))

def test__is_i686():
    """Test de la fonction _is_i686"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_i686')
    assert callable(getattr(cpuinfo, '_is_i686'))

def test__is_Celeron():
    """Test de la fonction _is_Celeron"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_Celeron')
    assert callable(getattr(cpuinfo, '_is_Celeron'))

def test__is_Pentium():
    """Test de la fonction _is_Pentium"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_Pentium')
    assert callable(getattr(cpuinfo, '_is_Pentium'))

def test__is_PentiumII():
    """Test de la fonction _is_PentiumII"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_PentiumII')
    assert callable(getattr(cpuinfo, '_is_PentiumII'))

def test__is_PentiumPro():
    """Test de la fonction _is_PentiumPro"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_PentiumPro')
    assert callable(getattr(cpuinfo, '_is_PentiumPro'))

def test__is_PentiumMMX():
    """Test de la fonction _is_PentiumMMX"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_PentiumMMX')
    assert callable(getattr(cpuinfo, '_is_PentiumMMX'))

def test__is_PentiumIII():
    """Test de la fonction _is_PentiumIII"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_PentiumIII')
    assert callable(getattr(cpuinfo, '_is_PentiumIII'))

def test__is_PentiumIV():
    """Test de la fonction _is_PentiumIV"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_PentiumIV')
    assert callable(getattr(cpuinfo, '_is_PentiumIV'))

def test__is_PentiumM():
    """Test de la fonction _is_PentiumM"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_PentiumM')
    assert callable(getattr(cpuinfo, '_is_PentiumM'))

def test__is_Prescott():
    """Test de la fonction _is_Prescott"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_Prescott')
    assert callable(getattr(cpuinfo, '_is_Prescott'))

def test__is_Nocona():
    """Test de la fonction _is_Nocona"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_Nocona')
    assert callable(getattr(cpuinfo, '_is_Nocona'))

def test__is_Core2():
    """Test de la fonction _is_Core2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_Core2')
    assert callable(getattr(cpuinfo, '_is_Core2'))

def test__is_Itanium():
    """Test de la fonction _is_Itanium"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_Itanium')
    assert callable(getattr(cpuinfo, '_is_Itanium'))

def test__is_XEON():
    """Test de la fonction _is_XEON"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_XEON')
    assert callable(getattr(cpuinfo, '_is_XEON'))

def test__is_singleCPU():
    """Test de la fonction _is_singleCPU"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_singleCPU')
    assert callable(getattr(cpuinfo, '_is_singleCPU'))

def test__getNCPUs():
    """Test de la fonction _getNCPUs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_getNCPUs')
    assert callable(getattr(cpuinfo, '_getNCPUs'))

def test__has_fdiv_bug():
    """Test de la fonction _has_fdiv_bug"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_has_fdiv_bug')
    assert callable(getattr(cpuinfo, '_has_fdiv_bug'))

def test__has_f00f_bug():
    """Test de la fonction _has_f00f_bug"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_has_f00f_bug')
    assert callable(getattr(cpuinfo, '_has_f00f_bug'))

def test__has_mmx():
    """Test de la fonction _has_mmx"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_has_mmx')
    assert callable(getattr(cpuinfo, '_has_mmx'))

def test__has_sse():
    """Test de la fonction _has_sse"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_has_sse')
    assert callable(getattr(cpuinfo, '_has_sse'))

def test__has_sse2():
    """Test de la fonction _has_sse2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_has_sse2')
    assert callable(getattr(cpuinfo, '_has_sse2'))

def test__has_sse3():
    """Test de la fonction _has_sse3"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_has_sse3')
    assert callable(getattr(cpuinfo, '_has_sse3'))

def test__has_ssse3():
    """Test de la fonction _has_ssse3"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_has_ssse3')
    assert callable(getattr(cpuinfo, '_has_ssse3'))

def test__has_3dnow():
    """Test de la fonction _has_3dnow"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_has_3dnow')
    assert callable(getattr(cpuinfo, '_has_3dnow'))

def test__has_3dnowext():
    """Test de la fonction _has_3dnowext"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_has_3dnowext')
    assert callable(getattr(cpuinfo, '_has_3dnowext'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '__init__')
    assert callable(getattr(cpuinfo, '__init__'))

def test__not_impl():
    """Test de la fonction _not_impl"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_not_impl')
    assert callable(getattr(cpuinfo, '_not_impl'))

def test__is_singleCPU():
    """Test de la fonction _is_singleCPU"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_singleCPU')
    assert callable(getattr(cpuinfo, '_is_singleCPU'))

def test__getNCPUs():
    """Test de la fonction _getNCPUs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_getNCPUs')
    assert callable(getattr(cpuinfo, '_getNCPUs'))

def test___cputype():
    """Test de la fonction __cputype"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '__cputype')
    assert callable(getattr(cpuinfo, '__cputype'))

def test__is_r2000():
    """Test de la fonction _is_r2000"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_r2000')
    assert callable(getattr(cpuinfo, '_is_r2000'))

def test__is_r3000():
    """Test de la fonction _is_r3000"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_r3000')
    assert callable(getattr(cpuinfo, '_is_r3000'))

def test__is_r3900():
    """Test de la fonction _is_r3900"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_r3900')
    assert callable(getattr(cpuinfo, '_is_r3900'))

def test__is_r4000():
    """Test de la fonction _is_r4000"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_r4000')
    assert callable(getattr(cpuinfo, '_is_r4000'))

def test__is_r4100():
    """Test de la fonction _is_r4100"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_r4100')
    assert callable(getattr(cpuinfo, '_is_r4100'))

def test__is_r4300():
    """Test de la fonction _is_r4300"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_r4300')
    assert callable(getattr(cpuinfo, '_is_r4300'))

def test__is_r4400():
    """Test de la fonction _is_r4400"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_r4400')
    assert callable(getattr(cpuinfo, '_is_r4400'))

def test__is_r4600():
    """Test de la fonction _is_r4600"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_r4600')
    assert callable(getattr(cpuinfo, '_is_r4600'))

def test__is_r4650():
    """Test de la fonction _is_r4650"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_r4650')
    assert callable(getattr(cpuinfo, '_is_r4650'))

def test__is_r5000():
    """Test de la fonction _is_r5000"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_r5000')
    assert callable(getattr(cpuinfo, '_is_r5000'))

def test__is_r6000():
    """Test de la fonction _is_r6000"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_r6000')
    assert callable(getattr(cpuinfo, '_is_r6000'))

def test__is_r8000():
    """Test de la fonction _is_r8000"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_r8000')
    assert callable(getattr(cpuinfo, '_is_r8000'))

def test__is_r10000():
    """Test de la fonction _is_r10000"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_r10000')
    assert callable(getattr(cpuinfo, '_is_r10000'))

def test__is_r12000():
    """Test de la fonction _is_r12000"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_r12000')
    assert callable(getattr(cpuinfo, '_is_r12000'))

def test__is_rorion():
    """Test de la fonction _is_rorion"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_rorion')
    assert callable(getattr(cpuinfo, '_is_rorion'))

def test_get_ip():
    """Test de la fonction get_ip"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, 'get_ip')
    assert callable(getattr(cpuinfo, 'get_ip'))

def test___machine():
    """Test de la fonction __machine"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '__machine')
    assert callable(getattr(cpuinfo, '__machine'))

def test__is_IP19():
    """Test de la fonction _is_IP19"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_IP19')
    assert callable(getattr(cpuinfo, '_is_IP19'))

def test__is_IP20():
    """Test de la fonction _is_IP20"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_IP20')
    assert callable(getattr(cpuinfo, '_is_IP20'))

def test__is_IP21():
    """Test de la fonction _is_IP21"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_IP21')
    assert callable(getattr(cpuinfo, '_is_IP21'))

def test__is_IP22():
    """Test de la fonction _is_IP22"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_IP22')
    assert callable(getattr(cpuinfo, '_is_IP22'))

def test__is_IP22_4k():
    """Test de la fonction _is_IP22_4k"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_IP22_4k')
    assert callable(getattr(cpuinfo, '_is_IP22_4k'))

def test__is_IP22_5k():
    """Test de la fonction _is_IP22_5k"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_IP22_5k')
    assert callable(getattr(cpuinfo, '_is_IP22_5k'))

def test__is_IP24():
    """Test de la fonction _is_IP24"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_IP24')
    assert callable(getattr(cpuinfo, '_is_IP24'))

def test__is_IP25():
    """Test de la fonction _is_IP25"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_IP25')
    assert callable(getattr(cpuinfo, '_is_IP25'))

def test__is_IP26():
    """Test de la fonction _is_IP26"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_IP26')
    assert callable(getattr(cpuinfo, '_is_IP26'))

def test__is_IP27():
    """Test de la fonction _is_IP27"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_IP27')
    assert callable(getattr(cpuinfo, '_is_IP27'))

def test__is_IP28():
    """Test de la fonction _is_IP28"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_IP28')
    assert callable(getattr(cpuinfo, '_is_IP28'))

def test__is_IP30():
    """Test de la fonction _is_IP30"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_IP30')
    assert callable(getattr(cpuinfo, '_is_IP30'))

def test__is_IP32():
    """Test de la fonction _is_IP32"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_IP32')
    assert callable(getattr(cpuinfo, '_is_IP32'))

def test__is_IP32_5k():
    """Test de la fonction _is_IP32_5k"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_IP32_5k')
    assert callable(getattr(cpuinfo, '_is_IP32_5k'))

def test__is_IP32_10k():
    """Test de la fonction _is_IP32_10k"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_IP32_10k')
    assert callable(getattr(cpuinfo, '_is_IP32_10k'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '__init__')
    assert callable(getattr(cpuinfo, '__init__'))

def test__not_impl():
    """Test de la fonction _not_impl"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_not_impl')
    assert callable(getattr(cpuinfo, '_not_impl'))

def test__getNCPUs():
    """Test de la fonction _getNCPUs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_getNCPUs')
    assert callable(getattr(cpuinfo, '_getNCPUs'))

def test__is_Power_Macintosh():
    """Test de la fonction _is_Power_Macintosh"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_Power_Macintosh')
    assert callable(getattr(cpuinfo, '_is_Power_Macintosh'))

def test__is_i386():
    """Test de la fonction _is_i386"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_i386')
    assert callable(getattr(cpuinfo, '_is_i386'))

def test__is_ppc():
    """Test de la fonction _is_ppc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_ppc')
    assert callable(getattr(cpuinfo, '_is_ppc'))

def test___machine():
    """Test de la fonction __machine"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '__machine')
    assert callable(getattr(cpuinfo, '__machine'))

def test__is_ppc601():
    """Test de la fonction _is_ppc601"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_ppc601')
    assert callable(getattr(cpuinfo, '_is_ppc601'))

def test__is_ppc602():
    """Test de la fonction _is_ppc602"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_ppc602')
    assert callable(getattr(cpuinfo, '_is_ppc602'))

def test__is_ppc603():
    """Test de la fonction _is_ppc603"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_ppc603')
    assert callable(getattr(cpuinfo, '_is_ppc603'))

def test__is_ppc603e():
    """Test de la fonction _is_ppc603e"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_ppc603e')
    assert callable(getattr(cpuinfo, '_is_ppc603e'))

def test__is_ppc604():
    """Test de la fonction _is_ppc604"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_ppc604')
    assert callable(getattr(cpuinfo, '_is_ppc604'))

def test__is_ppc604e():
    """Test de la fonction _is_ppc604e"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_ppc604e')
    assert callable(getattr(cpuinfo, '_is_ppc604e'))

def test__is_ppc620():
    """Test de la fonction _is_ppc620"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_ppc620')
    assert callable(getattr(cpuinfo, '_is_ppc620'))

def test__is_ppc630():
    """Test de la fonction _is_ppc630"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_ppc630')
    assert callable(getattr(cpuinfo, '_is_ppc630'))

def test__is_ppc740():
    """Test de la fonction _is_ppc740"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_ppc740')
    assert callable(getattr(cpuinfo, '_is_ppc740'))

def test__is_ppc7400():
    """Test de la fonction _is_ppc7400"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_ppc7400')
    assert callable(getattr(cpuinfo, '_is_ppc7400'))

def test__is_ppc7450():
    """Test de la fonction _is_ppc7450"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_ppc7450')
    assert callable(getattr(cpuinfo, '_is_ppc7450'))

def test__is_ppc750():
    """Test de la fonction _is_ppc750"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_ppc750')
    assert callable(getattr(cpuinfo, '_is_ppc750'))

def test__is_ppc403():
    """Test de la fonction _is_ppc403"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_ppc403')
    assert callable(getattr(cpuinfo, '_is_ppc403'))

def test__is_ppc505():
    """Test de la fonction _is_ppc505"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_ppc505')
    assert callable(getattr(cpuinfo, '_is_ppc505'))

def test__is_ppc801():
    """Test de la fonction _is_ppc801"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_ppc801')
    assert callable(getattr(cpuinfo, '_is_ppc801'))

def test__is_ppc821():
    """Test de la fonction _is_ppc821"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_ppc821')
    assert callable(getattr(cpuinfo, '_is_ppc821'))

def test__is_ppc823():
    """Test de la fonction _is_ppc823"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_ppc823')
    assert callable(getattr(cpuinfo, '_is_ppc823'))

def test__is_ppc860():
    """Test de la fonction _is_ppc860"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_ppc860')
    assert callable(getattr(cpuinfo, '_is_ppc860'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '__init__')
    assert callable(getattr(cpuinfo, '__init__'))

def test__not_impl():
    """Test de la fonction _not_impl"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_not_impl')
    assert callable(getattr(cpuinfo, '_not_impl'))

def test__is_i386():
    """Test de la fonction _is_i386"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_i386')
    assert callable(getattr(cpuinfo, '_is_i386'))

def test__is_sparc():
    """Test de la fonction _is_sparc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_sparc')
    assert callable(getattr(cpuinfo, '_is_sparc'))

def test__is_sparcv9():
    """Test de la fonction _is_sparcv9"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_sparcv9')
    assert callable(getattr(cpuinfo, '_is_sparcv9'))

def test__getNCPUs():
    """Test de la fonction _getNCPUs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_getNCPUs')
    assert callable(getattr(cpuinfo, '_getNCPUs'))

def test__is_sun4():
    """Test de la fonction _is_sun4"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_sun4')
    assert callable(getattr(cpuinfo, '_is_sun4'))

def test__is_SUNW():
    """Test de la fonction _is_SUNW"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_SUNW')
    assert callable(getattr(cpuinfo, '_is_SUNW'))

def test__is_sparcstation5():
    """Test de la fonction _is_sparcstation5"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_sparcstation5')
    assert callable(getattr(cpuinfo, '_is_sparcstation5'))

def test__is_ultra1():
    """Test de la fonction _is_ultra1"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_ultra1')
    assert callable(getattr(cpuinfo, '_is_ultra1'))

def test__is_ultra250():
    """Test de la fonction _is_ultra250"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_ultra250')
    assert callable(getattr(cpuinfo, '_is_ultra250'))

def test__is_ultra2():
    """Test de la fonction _is_ultra2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_ultra2')
    assert callable(getattr(cpuinfo, '_is_ultra2'))

def test__is_ultra30():
    """Test de la fonction _is_ultra30"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_ultra30')
    assert callable(getattr(cpuinfo, '_is_ultra30'))

def test__is_ultra4():
    """Test de la fonction _is_ultra4"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_ultra4')
    assert callable(getattr(cpuinfo, '_is_ultra4'))

def test__is_ultra5_10():
    """Test de la fonction _is_ultra5_10"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_ultra5_10')
    assert callable(getattr(cpuinfo, '_is_ultra5_10'))

def test__is_ultra5():
    """Test de la fonction _is_ultra5"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_ultra5')
    assert callable(getattr(cpuinfo, '_is_ultra5'))

def test__is_ultra60():
    """Test de la fonction _is_ultra60"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_ultra60')
    assert callable(getattr(cpuinfo, '_is_ultra60'))

def test__is_ultra80():
    """Test de la fonction _is_ultra80"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_ultra80')
    assert callable(getattr(cpuinfo, '_is_ultra80'))

def test__is_ultraenterprice():
    """Test de la fonction _is_ultraenterprice"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_ultraenterprice')
    assert callable(getattr(cpuinfo, '_is_ultraenterprice'))

def test__is_ultraenterprice10k():
    """Test de la fonction _is_ultraenterprice10k"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_ultraenterprice10k')
    assert callable(getattr(cpuinfo, '_is_ultraenterprice10k'))

def test__is_sunfire():
    """Test de la fonction _is_sunfire"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_sunfire')
    assert callable(getattr(cpuinfo, '_is_sunfire'))

def test__is_ultra():
    """Test de la fonction _is_ultra"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_ultra')
    assert callable(getattr(cpuinfo, '_is_ultra'))

def test__is_cpusparcv7():
    """Test de la fonction _is_cpusparcv7"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_cpusparcv7')
    assert callable(getattr(cpuinfo, '_is_cpusparcv7'))

def test__is_cpusparcv8():
    """Test de la fonction _is_cpusparcv8"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_cpusparcv8')
    assert callable(getattr(cpuinfo, '_is_cpusparcv8'))

def test__is_cpusparcv9():
    """Test de la fonction _is_cpusparcv9"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_cpusparcv9')
    assert callable(getattr(cpuinfo, '_is_cpusparcv9'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '__init__')
    assert callable(getattr(cpuinfo, '__init__'))

def test__not_impl():
    """Test de la fonction _not_impl"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_not_impl')
    assert callable(getattr(cpuinfo, '_not_impl'))

def test__is_AMD():
    """Test de la fonction _is_AMD"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_AMD')
    assert callable(getattr(cpuinfo, '_is_AMD'))

def test__is_Am486():
    """Test de la fonction _is_Am486"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_Am486')
    assert callable(getattr(cpuinfo, '_is_Am486'))

def test__is_Am5x86():
    """Test de la fonction _is_Am5x86"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_Am5x86')
    assert callable(getattr(cpuinfo, '_is_Am5x86'))

def test__is_AMDK5():
    """Test de la fonction _is_AMDK5"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_AMDK5')
    assert callable(getattr(cpuinfo, '_is_AMDK5'))

def test__is_AMDK6():
    """Test de la fonction _is_AMDK6"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_AMDK6')
    assert callable(getattr(cpuinfo, '_is_AMDK6'))

def test__is_AMDK6_2():
    """Test de la fonction _is_AMDK6_2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_AMDK6_2')
    assert callable(getattr(cpuinfo, '_is_AMDK6_2'))

def test__is_AMDK6_3():
    """Test de la fonction _is_AMDK6_3"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_AMDK6_3')
    assert callable(getattr(cpuinfo, '_is_AMDK6_3'))

def test__is_AMDK7():
    """Test de la fonction _is_AMDK7"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_AMDK7')
    assert callable(getattr(cpuinfo, '_is_AMDK7'))

def test__is_AMD64():
    """Test de la fonction _is_AMD64"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_AMD64')
    assert callable(getattr(cpuinfo, '_is_AMD64'))

def test__is_Intel():
    """Test de la fonction _is_Intel"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_Intel')
    assert callable(getattr(cpuinfo, '_is_Intel'))

def test__is_i386():
    """Test de la fonction _is_i386"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_i386')
    assert callable(getattr(cpuinfo, '_is_i386'))

def test__is_i486():
    """Test de la fonction _is_i486"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_i486')
    assert callable(getattr(cpuinfo, '_is_i486'))

def test__is_i586():
    """Test de la fonction _is_i586"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_i586')
    assert callable(getattr(cpuinfo, '_is_i586'))

def test__is_i686():
    """Test de la fonction _is_i686"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_i686')
    assert callable(getattr(cpuinfo, '_is_i686'))

def test__is_Pentium():
    """Test de la fonction _is_Pentium"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_Pentium')
    assert callable(getattr(cpuinfo, '_is_Pentium'))

def test__is_PentiumMMX():
    """Test de la fonction _is_PentiumMMX"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_PentiumMMX')
    assert callable(getattr(cpuinfo, '_is_PentiumMMX'))

def test__is_PentiumPro():
    """Test de la fonction _is_PentiumPro"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_PentiumPro')
    assert callable(getattr(cpuinfo, '_is_PentiumPro'))

def test__is_PentiumII():
    """Test de la fonction _is_PentiumII"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_PentiumII')
    assert callable(getattr(cpuinfo, '_is_PentiumII'))

def test__is_PentiumIII():
    """Test de la fonction _is_PentiumIII"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_PentiumIII')
    assert callable(getattr(cpuinfo, '_is_PentiumIII'))

def test__is_PentiumIV():
    """Test de la fonction _is_PentiumIV"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_PentiumIV')
    assert callable(getattr(cpuinfo, '_is_PentiumIV'))

def test__is_PentiumM():
    """Test de la fonction _is_PentiumM"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_PentiumM')
    assert callable(getattr(cpuinfo, '_is_PentiumM'))

def test__is_Core2():
    """Test de la fonction _is_Core2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_Core2')
    assert callable(getattr(cpuinfo, '_is_Core2'))

def test__is_singleCPU():
    """Test de la fonction _is_singleCPU"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_is_singleCPU')
    assert callable(getattr(cpuinfo, '_is_singleCPU'))

def test__getNCPUs():
    """Test de la fonction _getNCPUs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_getNCPUs')
    assert callable(getattr(cpuinfo, '_getNCPUs'))

def test__has_mmx():
    """Test de la fonction _has_mmx"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_has_mmx')
    assert callable(getattr(cpuinfo, '_has_mmx'))

def test__has_sse():
    """Test de la fonction _has_sse"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_has_sse')
    assert callable(getattr(cpuinfo, '_has_sse'))

def test__has_sse2():
    """Test de la fonction _has_sse2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_has_sse2')
    assert callable(getattr(cpuinfo, '_has_sse2'))

def test__has_3dnow():
    """Test de la fonction _has_3dnow"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_has_3dnow')
    assert callable(getattr(cpuinfo, '_has_3dnow'))

def test__has_3dnowext():
    """Test de la fonction _has_3dnowext"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cpuinfo, '_has_3dnowext')
    assert callable(getattr(cpuinfo, '_has_3dnowext'))

class TestCPUInfoBase:
    """Tests pour la classe CPUInfoBase"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(cpuinfo, 'CPUInfoBase')
        assert isinstance(getattr(cpuinfo, 'CPUInfoBase'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(cpuinfo, 'CPUInfoBase')
        for method_name in ['_try_call', '__getattr__', '_getNCPUs', '__get_nbits', '_is_32bit', '_is_64bit']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestLinuxCPUInfo:
    """Tests pour la classe LinuxCPUInfo"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(cpuinfo, 'LinuxCPUInfo')
        assert isinstance(getattr(cpuinfo, 'LinuxCPUInfo'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(cpuinfo, 'LinuxCPUInfo')
        for method_name in ['__init__', '_not_impl', '_is_AMD', '_is_AthlonK6_2', '_is_AthlonK6_3', '_is_AthlonK6', '_is_AthlonK7', '_is_AthlonMP', '_is_AMD64', '_is_Athlon64', '_is_AthlonHX', '_is_Opteron', '_is_Hammer', '_is_Alpha', '_is_EV4', '_is_EV5', '_is_EV56', '_is_PCA56', '_is_Intel', '_is_i486', '_is_i586', '_is_i686', '_is_Celeron', '_is_Pentium', '_is_PentiumII', '_is_PentiumPro', '_is_PentiumMMX', '_is_PentiumIII', '_is_PentiumIV', '_is_PentiumM', '_is_Prescott', '_is_Nocona', '_is_Core2', '_is_Itanium', '_is_XEON', '_is_singleCPU', '_getNCPUs', '_has_fdiv_bug', '_has_f00f_bug', '_has_mmx', '_has_sse', '_has_sse2', '_has_sse3', '_has_ssse3', '_has_3dnow', '_has_3dnowext']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestIRIXCPUInfo:
    """Tests pour la classe IRIXCPUInfo"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(cpuinfo, 'IRIXCPUInfo')
        assert isinstance(getattr(cpuinfo, 'IRIXCPUInfo'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(cpuinfo, 'IRIXCPUInfo')
        for method_name in ['__init__', '_not_impl', '_is_singleCPU', '_getNCPUs', '__cputype', '_is_r2000', '_is_r3000', '_is_r3900', '_is_r4000', '_is_r4100', '_is_r4300', '_is_r4400', '_is_r4600', '_is_r4650', '_is_r5000', '_is_r6000', '_is_r8000', '_is_r10000', '_is_r12000', '_is_rorion', 'get_ip', '__machine', '_is_IP19', '_is_IP20', '_is_IP21', '_is_IP22', '_is_IP22_4k', '_is_IP22_5k', '_is_IP24', '_is_IP25', '_is_IP26', '_is_IP27', '_is_IP28', '_is_IP30', '_is_IP32', '_is_IP32_5k', '_is_IP32_10k']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDarwinCPUInfo:
    """Tests pour la classe DarwinCPUInfo"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(cpuinfo, 'DarwinCPUInfo')
        assert isinstance(getattr(cpuinfo, 'DarwinCPUInfo'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(cpuinfo, 'DarwinCPUInfo')
        for method_name in ['__init__', '_not_impl', '_getNCPUs', '_is_Power_Macintosh', '_is_i386', '_is_ppc', '__machine', '_is_ppc601', '_is_ppc602', '_is_ppc603', '_is_ppc603e', '_is_ppc604', '_is_ppc604e', '_is_ppc620', '_is_ppc630', '_is_ppc740', '_is_ppc7400', '_is_ppc7450', '_is_ppc750', '_is_ppc403', '_is_ppc505', '_is_ppc801', '_is_ppc821', '_is_ppc823', '_is_ppc860']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSunOSCPUInfo:
    """Tests pour la classe SunOSCPUInfo"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(cpuinfo, 'SunOSCPUInfo')
        assert isinstance(getattr(cpuinfo, 'SunOSCPUInfo'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(cpuinfo, 'SunOSCPUInfo')
        for method_name in ['__init__', '_not_impl', '_is_i386', '_is_sparc', '_is_sparcv9', '_getNCPUs', '_is_sun4', '_is_SUNW', '_is_sparcstation5', '_is_ultra1', '_is_ultra250', '_is_ultra2', '_is_ultra30', '_is_ultra4', '_is_ultra5_10', '_is_ultra5', '_is_ultra60', '_is_ultra80', '_is_ultraenterprice', '_is_ultraenterprice10k', '_is_sunfire', '_is_ultra', '_is_cpusparcv7', '_is_cpusparcv8', '_is_cpusparcv9']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestWin32CPUInfo:
    """Tests pour la classe Win32CPUInfo"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(cpuinfo, 'Win32CPUInfo')
        assert isinstance(getattr(cpuinfo, 'Win32CPUInfo'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(cpuinfo, 'Win32CPUInfo')
        for method_name in ['__init__', '_not_impl', '_is_AMD', '_is_Am486', '_is_Am5x86', '_is_AMDK5', '_is_AMDK6', '_is_AMDK6_2', '_is_AMDK6_3', '_is_AMDK7', '_is_AMD64', '_is_Intel', '_is_i386', '_is_i486', '_is_i586', '_is_i686', '_is_Pentium', '_is_PentiumMMX', '_is_PentiumPro', '_is_PentiumII', '_is_PentiumIII', '_is_PentiumIV', '_is_PentiumM', '_is_Core2', '_is_singleCPU', '_getNCPUs', '_has_mmx', '_has_sse', '_has_sse2', '_has_3dnow', '_has_3dnowext']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
