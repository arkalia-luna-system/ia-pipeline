"""
Tests unitaires générés pour text_format
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import text_format
except ImportError:
    pytest.skip(f"Module text_format non importable")


def test_MessageToString():
    """Test de la fonction MessageToString"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'MessageToString')
    assert callable(getattr(text_format, 'MessageToString'))

def test_MessageToBytes():
    """Test de la fonction MessageToBytes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'MessageToBytes')
    assert callable(getattr(text_format, 'MessageToBytes'))

def test__IsMapEntry():
    """Test de la fonction _IsMapEntry"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_IsMapEntry')
    assert callable(getattr(text_format, '_IsMapEntry'))

def test__IsGroupLike():
    """Test de la fonction _IsGroupLike"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_IsGroupLike')
    assert callable(getattr(text_format, '_IsGroupLike'))

def test_PrintMessage():
    """Test de la fonction PrintMessage"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'PrintMessage')
    assert callable(getattr(text_format, 'PrintMessage'))

def test_PrintField():
    """Test de la fonction PrintField"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'PrintField')
    assert callable(getattr(text_format, 'PrintField'))

def test_PrintFieldValue():
    """Test de la fonction PrintFieldValue"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'PrintFieldValue')
    assert callable(getattr(text_format, 'PrintFieldValue'))

def test__BuildMessageFromTypeName():
    """Test de la fonction _BuildMessageFromTypeName"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_BuildMessageFromTypeName')
    assert callable(getattr(text_format, '_BuildMessageFromTypeName'))

def test_Parse():
    """Test de la fonction Parse"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'Parse')
    assert callable(getattr(text_format, 'Parse'))

def test_Merge():
    """Test de la fonction Merge"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'Merge')
    assert callable(getattr(text_format, 'Merge'))

def test_ParseLines():
    """Test de la fonction ParseLines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'ParseLines')
    assert callable(getattr(text_format, 'ParseLines'))

def test_MergeLines():
    """Test de la fonction MergeLines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'MergeLines')
    assert callable(getattr(text_format, 'MergeLines'))

def test__ConsumeInt32():
    """Test de la fonction _ConsumeInt32"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_ConsumeInt32')
    assert callable(getattr(text_format, '_ConsumeInt32'))

def test__ConsumeUint32():
    """Test de la fonction _ConsumeUint32"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_ConsumeUint32')
    assert callable(getattr(text_format, '_ConsumeUint32'))

def test__TryConsumeInt64():
    """Test de la fonction _TryConsumeInt64"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_TryConsumeInt64')
    assert callable(getattr(text_format, '_TryConsumeInt64'))

def test__ConsumeInt64():
    """Test de la fonction _ConsumeInt64"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_ConsumeInt64')
    assert callable(getattr(text_format, '_ConsumeInt64'))

def test__TryConsumeUint64():
    """Test de la fonction _TryConsumeUint64"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_TryConsumeUint64')
    assert callable(getattr(text_format, '_TryConsumeUint64'))

def test__ConsumeUint64():
    """Test de la fonction _ConsumeUint64"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_ConsumeUint64')
    assert callable(getattr(text_format, '_ConsumeUint64'))

def test__ConsumeInteger():
    """Test de la fonction _ConsumeInteger"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_ConsumeInteger')
    assert callable(getattr(text_format, '_ConsumeInteger'))

def test_ParseInteger():
    """Test de la fonction ParseInteger"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'ParseInteger')
    assert callable(getattr(text_format, 'ParseInteger'))

def test__ParseAbstractInteger():
    """Test de la fonction _ParseAbstractInteger"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_ParseAbstractInteger')
    assert callable(getattr(text_format, '_ParseAbstractInteger'))

def test_ParseFloat():
    """Test de la fonction ParseFloat"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'ParseFloat')
    assert callable(getattr(text_format, 'ParseFloat'))

def test_ParseBool():
    """Test de la fonction ParseBool"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'ParseBool')
    assert callable(getattr(text_format, 'ParseBool'))

def test_ParseEnum():
    """Test de la fonction ParseEnum"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'ParseEnum')
    assert callable(getattr(text_format, 'ParseEnum'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '__init__')
    assert callable(getattr(text_format, '__init__'))

def test_GetLine():
    """Test de la fonction GetLine"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'GetLine')
    assert callable(getattr(text_format, 'GetLine'))

def test_GetColumn():
    """Test de la fonction GetColumn"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'GetColumn')
    assert callable(getattr(text_format, 'GetColumn'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '__init__')
    assert callable(getattr(text_format, '__init__'))

def test_write():
    """Test de la fonction write"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'write')
    assert callable(getattr(text_format, 'write'))

def test_close():
    """Test de la fonction close"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'close')
    assert callable(getattr(text_format, 'close'))

def test_getvalue():
    """Test de la fonction getvalue"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'getvalue')
    assert callable(getattr(text_format, 'getvalue'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '__init__')
    assert callable(getattr(text_format, '__init__'))

def test__TryPrintAsAnyMessage():
    """Test de la fonction _TryPrintAsAnyMessage"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_TryPrintAsAnyMessage')
    assert callable(getattr(text_format, '_TryPrintAsAnyMessage'))

def test__TryCustomFormatMessage():
    """Test de la fonction _TryCustomFormatMessage"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_TryCustomFormatMessage')
    assert callable(getattr(text_format, '_TryCustomFormatMessage'))

def test_PrintMessage():
    """Test de la fonction PrintMessage"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'PrintMessage')
    assert callable(getattr(text_format, 'PrintMessage'))

def test__PrintUnknownFields():
    """Test de la fonction _PrintUnknownFields"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_PrintUnknownFields')
    assert callable(getattr(text_format, '_PrintUnknownFields'))

def test__PrintFieldName():
    """Test de la fonction _PrintFieldName"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_PrintFieldName')
    assert callable(getattr(text_format, '_PrintFieldName'))

def test_PrintField():
    """Test de la fonction PrintField"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'PrintField')
    assert callable(getattr(text_format, 'PrintField'))

def test__PrintShortRepeatedPrimitivesValue():
    """Test de la fonction _PrintShortRepeatedPrimitivesValue"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_PrintShortRepeatedPrimitivesValue')
    assert callable(getattr(text_format, '_PrintShortRepeatedPrimitivesValue'))

def test__PrintMessageFieldValue():
    """Test de la fonction _PrintMessageFieldValue"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_PrintMessageFieldValue')
    assert callable(getattr(text_format, '_PrintMessageFieldValue'))

def test_PrintFieldValue():
    """Test de la fonction PrintFieldValue"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'PrintFieldValue')
    assert callable(getattr(text_format, 'PrintFieldValue'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '__init__')
    assert callable(getattr(text_format, '__init__'))

def test_ParseLines():
    """Test de la fonction ParseLines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'ParseLines')
    assert callable(getattr(text_format, 'ParseLines'))

def test_MergeLines():
    """Test de la fonction MergeLines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'MergeLines')
    assert callable(getattr(text_format, 'MergeLines'))

def test__ParseOrMerge():
    """Test de la fonction _ParseOrMerge"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_ParseOrMerge')
    assert callable(getattr(text_format, '_ParseOrMerge'))

def test__MergeField():
    """Test de la fonction _MergeField"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_MergeField')
    assert callable(getattr(text_format, '_MergeField'))

def test__LogSilentMarker():
    """Test de la fonction _LogSilentMarker"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_LogSilentMarker')
    assert callable(getattr(text_format, '_LogSilentMarker'))

def test__DetectSilentMarker():
    """Test de la fonction _DetectSilentMarker"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_DetectSilentMarker')
    assert callable(getattr(text_format, '_DetectSilentMarker'))

def test__ConsumeAnyTypeUrl():
    """Test de la fonction _ConsumeAnyTypeUrl"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_ConsumeAnyTypeUrl')
    assert callable(getattr(text_format, '_ConsumeAnyTypeUrl'))

def test__MergeMessageField():
    """Test de la fonction _MergeMessageField"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_MergeMessageField')
    assert callable(getattr(text_format, '_MergeMessageField'))

def test__MergeScalarField():
    """Test de la fonction _MergeScalarField"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_MergeScalarField')
    assert callable(getattr(text_format, '_MergeScalarField'))

def test__SkipFieldContents():
    """Test de la fonction _SkipFieldContents"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_SkipFieldContents')
    assert callable(getattr(text_format, '_SkipFieldContents'))

def test__SkipField():
    """Test de la fonction _SkipField"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_SkipField')
    assert callable(getattr(text_format, '_SkipField'))

def test__SkipFieldMessage():
    """Test de la fonction _SkipFieldMessage"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_SkipFieldMessage')
    assert callable(getattr(text_format, '_SkipFieldMessage'))

def test__SkipFieldValue():
    """Test de la fonction _SkipFieldValue"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_SkipFieldValue')
    assert callable(getattr(text_format, '_SkipFieldValue'))

def test__SkipRepeatedFieldValue():
    """Test de la fonction _SkipRepeatedFieldValue"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_SkipRepeatedFieldValue')
    assert callable(getattr(text_format, '_SkipRepeatedFieldValue'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '__init__')
    assert callable(getattr(text_format, '__init__'))

def test_LookingAt():
    """Test de la fonction LookingAt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'LookingAt')
    assert callable(getattr(text_format, 'LookingAt'))

def test_AtEnd():
    """Test de la fonction AtEnd"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'AtEnd')
    assert callable(getattr(text_format, 'AtEnd'))

def test__PopLine():
    """Test de la fonction _PopLine"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_PopLine')
    assert callable(getattr(text_format, '_PopLine'))

def test__SkipWhitespace():
    """Test de la fonction _SkipWhitespace"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_SkipWhitespace')
    assert callable(getattr(text_format, '_SkipWhitespace'))

def test_TryConsume():
    """Test de la fonction TryConsume"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'TryConsume')
    assert callable(getattr(text_format, 'TryConsume'))

def test_Consume():
    """Test de la fonction Consume"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'Consume')
    assert callable(getattr(text_format, 'Consume'))

def test_ConsumeComment():
    """Test de la fonction ConsumeComment"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'ConsumeComment')
    assert callable(getattr(text_format, 'ConsumeComment'))

def test_ConsumeCommentOrTrailingComment():
    """Test de la fonction ConsumeCommentOrTrailingComment"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'ConsumeCommentOrTrailingComment')
    assert callable(getattr(text_format, 'ConsumeCommentOrTrailingComment'))

def test_TryConsumeIdentifier():
    """Test de la fonction TryConsumeIdentifier"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'TryConsumeIdentifier')
    assert callable(getattr(text_format, 'TryConsumeIdentifier'))

def test_ConsumeIdentifier():
    """Test de la fonction ConsumeIdentifier"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'ConsumeIdentifier')
    assert callable(getattr(text_format, 'ConsumeIdentifier'))

def test_TryConsumeIdentifierOrNumber():
    """Test de la fonction TryConsumeIdentifierOrNumber"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'TryConsumeIdentifierOrNumber')
    assert callable(getattr(text_format, 'TryConsumeIdentifierOrNumber'))

def test_ConsumeIdentifierOrNumber():
    """Test de la fonction ConsumeIdentifierOrNumber"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'ConsumeIdentifierOrNumber')
    assert callable(getattr(text_format, 'ConsumeIdentifierOrNumber'))

def test_TryConsumeInteger():
    """Test de la fonction TryConsumeInteger"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'TryConsumeInteger')
    assert callable(getattr(text_format, 'TryConsumeInteger'))

def test_ConsumeInteger():
    """Test de la fonction ConsumeInteger"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'ConsumeInteger')
    assert callable(getattr(text_format, 'ConsumeInteger'))

def test_TryConsumeFloat():
    """Test de la fonction TryConsumeFloat"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'TryConsumeFloat')
    assert callable(getattr(text_format, 'TryConsumeFloat'))

def test_ConsumeFloat():
    """Test de la fonction ConsumeFloat"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'ConsumeFloat')
    assert callable(getattr(text_format, 'ConsumeFloat'))

def test_ConsumeBool():
    """Test de la fonction ConsumeBool"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'ConsumeBool')
    assert callable(getattr(text_format, 'ConsumeBool'))

def test_TryConsumeByteString():
    """Test de la fonction TryConsumeByteString"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'TryConsumeByteString')
    assert callable(getattr(text_format, 'TryConsumeByteString'))

def test_ConsumeString():
    """Test de la fonction ConsumeString"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'ConsumeString')
    assert callable(getattr(text_format, 'ConsumeString'))

def test_ConsumeByteString():
    """Test de la fonction ConsumeByteString"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'ConsumeByteString')
    assert callable(getattr(text_format, 'ConsumeByteString'))

def test__ConsumeSingleByteString():
    """Test de la fonction _ConsumeSingleByteString"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_ConsumeSingleByteString')
    assert callable(getattr(text_format, '_ConsumeSingleByteString'))

def test_ConsumeEnum():
    """Test de la fonction ConsumeEnum"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'ConsumeEnum')
    assert callable(getattr(text_format, 'ConsumeEnum'))

def test_ParseErrorPreviousToken():
    """Test de la fonction ParseErrorPreviousToken"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'ParseErrorPreviousToken')
    assert callable(getattr(text_format, 'ParseErrorPreviousToken'))

def test_ParseError():
    """Test de la fonction ParseError"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'ParseError')
    assert callable(getattr(text_format, 'ParseError'))

def test__StringParseError():
    """Test de la fonction _StringParseError"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, '_StringParseError')
    assert callable(getattr(text_format, '_StringParseError'))

def test_NextToken():
    """Test de la fonction NextToken"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_format, 'NextToken')
    assert callable(getattr(text_format, 'NextToken'))

class TestError:
    """Tests pour la classe Error"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(text_format, 'Error')
        assert isinstance(getattr(text_format, 'Error'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(text_format, 'Error')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestParseError:
    """Tests pour la classe ParseError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(text_format, 'ParseError')
        assert isinstance(getattr(text_format, 'ParseError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(text_format, 'ParseError')
        for method_name in ['__init__', 'GetLine', 'GetColumn']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTextWriter:
    """Tests pour la classe TextWriter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(text_format, 'TextWriter')
        assert isinstance(getattr(text_format, 'TextWriter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(text_format, 'TextWriter')
        for method_name in ['__init__', 'write', 'close', 'getvalue']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_Printer:
    """Tests pour la classe _Printer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(text_format, '_Printer')
        assert isinstance(getattr(text_format, '_Printer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(text_format, '_Printer')
        for method_name in ['__init__', '_TryPrintAsAnyMessage', '_TryCustomFormatMessage', 'PrintMessage', '_PrintUnknownFields', '_PrintFieldName', 'PrintField', '_PrintShortRepeatedPrimitivesValue', '_PrintMessageFieldValue', 'PrintFieldValue']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_Parser:
    """Tests pour la classe _Parser"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(text_format, '_Parser')
        assert isinstance(getattr(text_format, '_Parser'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(text_format, '_Parser')
        for method_name in ['__init__', 'ParseLines', 'MergeLines', '_ParseOrMerge', '_MergeField', '_LogSilentMarker', '_DetectSilentMarker', '_ConsumeAnyTypeUrl', '_MergeMessageField', '_MergeScalarField', '_SkipFieldContents', '_SkipField', '_SkipFieldMessage', '_SkipFieldValue', '_SkipRepeatedFieldValue']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTokenizer:
    """Tests pour la classe Tokenizer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(text_format, 'Tokenizer')
        assert isinstance(getattr(text_format, 'Tokenizer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(text_format, 'Tokenizer')
        for method_name in ['__init__', 'LookingAt', 'AtEnd', '_PopLine', '_SkipWhitespace', 'TryConsume', 'Consume', 'ConsumeComment', 'ConsumeCommentOrTrailingComment', 'TryConsumeIdentifier', 'ConsumeIdentifier', 'TryConsumeIdentifierOrNumber', 'ConsumeIdentifierOrNumber', 'TryConsumeInteger', 'ConsumeInteger', 'TryConsumeFloat', 'ConsumeFloat', 'ConsumeBool', 'TryConsumeByteString', 'ConsumeString', 'ConsumeByteString', '_ConsumeSingleByteString', 'ConsumeEnum', 'ParseErrorPreviousToken', 'ParseError', '_StringParseError', 'NextToken']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
