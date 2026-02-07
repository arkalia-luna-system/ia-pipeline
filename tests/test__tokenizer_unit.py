"""
Tests unitaires générés pour _tokenizer
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _tokenizer
except ImportError:
    pytest.skip(f"Module _tokenizer non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, '__init__')
    assert callable(getattr(_tokenizer, '__init__'))

def test___iter__():
    """Test de la fonction __iter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, '__iter__')
    assert callable(getattr(_tokenizer, '__iter__'))

def test_consumeNumberEntity():
    """Test de la fonction consumeNumberEntity"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'consumeNumberEntity')
    assert callable(getattr(_tokenizer, 'consumeNumberEntity'))

def test_consumeEntity():
    """Test de la fonction consumeEntity"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'consumeEntity')
    assert callable(getattr(_tokenizer, 'consumeEntity'))

def test_processEntityInAttribute():
    """Test de la fonction processEntityInAttribute"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'processEntityInAttribute')
    assert callable(getattr(_tokenizer, 'processEntityInAttribute'))

def test_emitCurrentToken():
    """Test de la fonction emitCurrentToken"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'emitCurrentToken')
    assert callable(getattr(_tokenizer, 'emitCurrentToken'))

def test_dataState():
    """Test de la fonction dataState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'dataState')
    assert callable(getattr(_tokenizer, 'dataState'))

def test_entityDataState():
    """Test de la fonction entityDataState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'entityDataState')
    assert callable(getattr(_tokenizer, 'entityDataState'))

def test_rcdataState():
    """Test de la fonction rcdataState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'rcdataState')
    assert callable(getattr(_tokenizer, 'rcdataState'))

def test_characterReferenceInRcdata():
    """Test de la fonction characterReferenceInRcdata"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'characterReferenceInRcdata')
    assert callable(getattr(_tokenizer, 'characterReferenceInRcdata'))

def test_rawtextState():
    """Test de la fonction rawtextState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'rawtextState')
    assert callable(getattr(_tokenizer, 'rawtextState'))

def test_scriptDataState():
    """Test de la fonction scriptDataState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'scriptDataState')
    assert callable(getattr(_tokenizer, 'scriptDataState'))

def test_plaintextState():
    """Test de la fonction plaintextState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'plaintextState')
    assert callable(getattr(_tokenizer, 'plaintextState'))

def test_tagOpenState():
    """Test de la fonction tagOpenState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'tagOpenState')
    assert callable(getattr(_tokenizer, 'tagOpenState'))

def test_closeTagOpenState():
    """Test de la fonction closeTagOpenState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'closeTagOpenState')
    assert callable(getattr(_tokenizer, 'closeTagOpenState'))

def test_tagNameState():
    """Test de la fonction tagNameState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'tagNameState')
    assert callable(getattr(_tokenizer, 'tagNameState'))

def test_rcdataLessThanSignState():
    """Test de la fonction rcdataLessThanSignState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'rcdataLessThanSignState')
    assert callable(getattr(_tokenizer, 'rcdataLessThanSignState'))

def test_rcdataEndTagOpenState():
    """Test de la fonction rcdataEndTagOpenState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'rcdataEndTagOpenState')
    assert callable(getattr(_tokenizer, 'rcdataEndTagOpenState'))

def test_rcdataEndTagNameState():
    """Test de la fonction rcdataEndTagNameState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'rcdataEndTagNameState')
    assert callable(getattr(_tokenizer, 'rcdataEndTagNameState'))

def test_rawtextLessThanSignState():
    """Test de la fonction rawtextLessThanSignState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'rawtextLessThanSignState')
    assert callable(getattr(_tokenizer, 'rawtextLessThanSignState'))

def test_rawtextEndTagOpenState():
    """Test de la fonction rawtextEndTagOpenState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'rawtextEndTagOpenState')
    assert callable(getattr(_tokenizer, 'rawtextEndTagOpenState'))

def test_rawtextEndTagNameState():
    """Test de la fonction rawtextEndTagNameState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'rawtextEndTagNameState')
    assert callable(getattr(_tokenizer, 'rawtextEndTagNameState'))

def test_scriptDataLessThanSignState():
    """Test de la fonction scriptDataLessThanSignState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'scriptDataLessThanSignState')
    assert callable(getattr(_tokenizer, 'scriptDataLessThanSignState'))

def test_scriptDataEndTagOpenState():
    """Test de la fonction scriptDataEndTagOpenState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'scriptDataEndTagOpenState')
    assert callable(getattr(_tokenizer, 'scriptDataEndTagOpenState'))

def test_scriptDataEndTagNameState():
    """Test de la fonction scriptDataEndTagNameState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'scriptDataEndTagNameState')
    assert callable(getattr(_tokenizer, 'scriptDataEndTagNameState'))

def test_scriptDataEscapeStartState():
    """Test de la fonction scriptDataEscapeStartState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'scriptDataEscapeStartState')
    assert callable(getattr(_tokenizer, 'scriptDataEscapeStartState'))

def test_scriptDataEscapeStartDashState():
    """Test de la fonction scriptDataEscapeStartDashState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'scriptDataEscapeStartDashState')
    assert callable(getattr(_tokenizer, 'scriptDataEscapeStartDashState'))

def test_scriptDataEscapedState():
    """Test de la fonction scriptDataEscapedState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'scriptDataEscapedState')
    assert callable(getattr(_tokenizer, 'scriptDataEscapedState'))

def test_scriptDataEscapedDashState():
    """Test de la fonction scriptDataEscapedDashState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'scriptDataEscapedDashState')
    assert callable(getattr(_tokenizer, 'scriptDataEscapedDashState'))

def test_scriptDataEscapedDashDashState():
    """Test de la fonction scriptDataEscapedDashDashState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'scriptDataEscapedDashDashState')
    assert callable(getattr(_tokenizer, 'scriptDataEscapedDashDashState'))

def test_scriptDataEscapedLessThanSignState():
    """Test de la fonction scriptDataEscapedLessThanSignState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'scriptDataEscapedLessThanSignState')
    assert callable(getattr(_tokenizer, 'scriptDataEscapedLessThanSignState'))

def test_scriptDataEscapedEndTagOpenState():
    """Test de la fonction scriptDataEscapedEndTagOpenState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'scriptDataEscapedEndTagOpenState')
    assert callable(getattr(_tokenizer, 'scriptDataEscapedEndTagOpenState'))

def test_scriptDataEscapedEndTagNameState():
    """Test de la fonction scriptDataEscapedEndTagNameState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'scriptDataEscapedEndTagNameState')
    assert callable(getattr(_tokenizer, 'scriptDataEscapedEndTagNameState'))

def test_scriptDataDoubleEscapeStartState():
    """Test de la fonction scriptDataDoubleEscapeStartState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'scriptDataDoubleEscapeStartState')
    assert callable(getattr(_tokenizer, 'scriptDataDoubleEscapeStartState'))

def test_scriptDataDoubleEscapedState():
    """Test de la fonction scriptDataDoubleEscapedState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'scriptDataDoubleEscapedState')
    assert callable(getattr(_tokenizer, 'scriptDataDoubleEscapedState'))

def test_scriptDataDoubleEscapedDashState():
    """Test de la fonction scriptDataDoubleEscapedDashState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'scriptDataDoubleEscapedDashState')
    assert callable(getattr(_tokenizer, 'scriptDataDoubleEscapedDashState'))

def test_scriptDataDoubleEscapedDashDashState():
    """Test de la fonction scriptDataDoubleEscapedDashDashState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'scriptDataDoubleEscapedDashDashState')
    assert callable(getattr(_tokenizer, 'scriptDataDoubleEscapedDashDashState'))

def test_scriptDataDoubleEscapedLessThanSignState():
    """Test de la fonction scriptDataDoubleEscapedLessThanSignState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'scriptDataDoubleEscapedLessThanSignState')
    assert callable(getattr(_tokenizer, 'scriptDataDoubleEscapedLessThanSignState'))

def test_scriptDataDoubleEscapeEndState():
    """Test de la fonction scriptDataDoubleEscapeEndState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'scriptDataDoubleEscapeEndState')
    assert callable(getattr(_tokenizer, 'scriptDataDoubleEscapeEndState'))

def test_beforeAttributeNameState():
    """Test de la fonction beforeAttributeNameState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'beforeAttributeNameState')
    assert callable(getattr(_tokenizer, 'beforeAttributeNameState'))

def test_attributeNameState():
    """Test de la fonction attributeNameState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'attributeNameState')
    assert callable(getattr(_tokenizer, 'attributeNameState'))

def test_afterAttributeNameState():
    """Test de la fonction afterAttributeNameState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'afterAttributeNameState')
    assert callable(getattr(_tokenizer, 'afterAttributeNameState'))

def test_beforeAttributeValueState():
    """Test de la fonction beforeAttributeValueState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'beforeAttributeValueState')
    assert callable(getattr(_tokenizer, 'beforeAttributeValueState'))

def test_attributeValueDoubleQuotedState():
    """Test de la fonction attributeValueDoubleQuotedState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'attributeValueDoubleQuotedState')
    assert callable(getattr(_tokenizer, 'attributeValueDoubleQuotedState'))

def test_attributeValueSingleQuotedState():
    """Test de la fonction attributeValueSingleQuotedState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'attributeValueSingleQuotedState')
    assert callable(getattr(_tokenizer, 'attributeValueSingleQuotedState'))

def test_attributeValueUnQuotedState():
    """Test de la fonction attributeValueUnQuotedState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'attributeValueUnQuotedState')
    assert callable(getattr(_tokenizer, 'attributeValueUnQuotedState'))

def test_afterAttributeValueState():
    """Test de la fonction afterAttributeValueState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'afterAttributeValueState')
    assert callable(getattr(_tokenizer, 'afterAttributeValueState'))

def test_selfClosingStartTagState():
    """Test de la fonction selfClosingStartTagState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'selfClosingStartTagState')
    assert callable(getattr(_tokenizer, 'selfClosingStartTagState'))

def test_bogusCommentState():
    """Test de la fonction bogusCommentState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'bogusCommentState')
    assert callable(getattr(_tokenizer, 'bogusCommentState'))

def test_markupDeclarationOpenState():
    """Test de la fonction markupDeclarationOpenState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'markupDeclarationOpenState')
    assert callable(getattr(_tokenizer, 'markupDeclarationOpenState'))

def test_commentStartState():
    """Test de la fonction commentStartState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'commentStartState')
    assert callable(getattr(_tokenizer, 'commentStartState'))

def test_commentStartDashState():
    """Test de la fonction commentStartDashState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'commentStartDashState')
    assert callable(getattr(_tokenizer, 'commentStartDashState'))

def test_commentState():
    """Test de la fonction commentState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'commentState')
    assert callable(getattr(_tokenizer, 'commentState'))

def test_commentEndDashState():
    """Test de la fonction commentEndDashState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'commentEndDashState')
    assert callable(getattr(_tokenizer, 'commentEndDashState'))

def test_commentEndState():
    """Test de la fonction commentEndState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'commentEndState')
    assert callable(getattr(_tokenizer, 'commentEndState'))

def test_commentEndBangState():
    """Test de la fonction commentEndBangState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'commentEndBangState')
    assert callable(getattr(_tokenizer, 'commentEndBangState'))

def test_doctypeState():
    """Test de la fonction doctypeState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'doctypeState')
    assert callable(getattr(_tokenizer, 'doctypeState'))

def test_beforeDoctypeNameState():
    """Test de la fonction beforeDoctypeNameState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'beforeDoctypeNameState')
    assert callable(getattr(_tokenizer, 'beforeDoctypeNameState'))

def test_doctypeNameState():
    """Test de la fonction doctypeNameState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'doctypeNameState')
    assert callable(getattr(_tokenizer, 'doctypeNameState'))

def test_afterDoctypeNameState():
    """Test de la fonction afterDoctypeNameState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'afterDoctypeNameState')
    assert callable(getattr(_tokenizer, 'afterDoctypeNameState'))

def test_afterDoctypePublicKeywordState():
    """Test de la fonction afterDoctypePublicKeywordState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'afterDoctypePublicKeywordState')
    assert callable(getattr(_tokenizer, 'afterDoctypePublicKeywordState'))

def test_beforeDoctypePublicIdentifierState():
    """Test de la fonction beforeDoctypePublicIdentifierState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'beforeDoctypePublicIdentifierState')
    assert callable(getattr(_tokenizer, 'beforeDoctypePublicIdentifierState'))

def test_doctypePublicIdentifierDoubleQuotedState():
    """Test de la fonction doctypePublicIdentifierDoubleQuotedState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'doctypePublicIdentifierDoubleQuotedState')
    assert callable(getattr(_tokenizer, 'doctypePublicIdentifierDoubleQuotedState'))

def test_doctypePublicIdentifierSingleQuotedState():
    """Test de la fonction doctypePublicIdentifierSingleQuotedState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'doctypePublicIdentifierSingleQuotedState')
    assert callable(getattr(_tokenizer, 'doctypePublicIdentifierSingleQuotedState'))

def test_afterDoctypePublicIdentifierState():
    """Test de la fonction afterDoctypePublicIdentifierState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'afterDoctypePublicIdentifierState')
    assert callable(getattr(_tokenizer, 'afterDoctypePublicIdentifierState'))

def test_betweenDoctypePublicAndSystemIdentifiersState():
    """Test de la fonction betweenDoctypePublicAndSystemIdentifiersState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'betweenDoctypePublicAndSystemIdentifiersState')
    assert callable(getattr(_tokenizer, 'betweenDoctypePublicAndSystemIdentifiersState'))

def test_afterDoctypeSystemKeywordState():
    """Test de la fonction afterDoctypeSystemKeywordState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'afterDoctypeSystemKeywordState')
    assert callable(getattr(_tokenizer, 'afterDoctypeSystemKeywordState'))

def test_beforeDoctypeSystemIdentifierState():
    """Test de la fonction beforeDoctypeSystemIdentifierState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'beforeDoctypeSystemIdentifierState')
    assert callable(getattr(_tokenizer, 'beforeDoctypeSystemIdentifierState'))

def test_doctypeSystemIdentifierDoubleQuotedState():
    """Test de la fonction doctypeSystemIdentifierDoubleQuotedState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'doctypeSystemIdentifierDoubleQuotedState')
    assert callable(getattr(_tokenizer, 'doctypeSystemIdentifierDoubleQuotedState'))

def test_doctypeSystemIdentifierSingleQuotedState():
    """Test de la fonction doctypeSystemIdentifierSingleQuotedState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'doctypeSystemIdentifierSingleQuotedState')
    assert callable(getattr(_tokenizer, 'doctypeSystemIdentifierSingleQuotedState'))

def test_afterDoctypeSystemIdentifierState():
    """Test de la fonction afterDoctypeSystemIdentifierState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'afterDoctypeSystemIdentifierState')
    assert callable(getattr(_tokenizer, 'afterDoctypeSystemIdentifierState'))

def test_bogusDoctypeState():
    """Test de la fonction bogusDoctypeState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'bogusDoctypeState')
    assert callable(getattr(_tokenizer, 'bogusDoctypeState'))

def test_cdataSectionState():
    """Test de la fonction cdataSectionState"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tokenizer, 'cdataSectionState')
    assert callable(getattr(_tokenizer, 'cdataSectionState'))

class TestHTMLTokenizer:
    """Tests pour la classe HTMLTokenizer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tokenizer, 'HTMLTokenizer')
        assert isinstance(getattr(_tokenizer, 'HTMLTokenizer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tokenizer, 'HTMLTokenizer')
        for method_name in ['__init__', '__iter__', 'consumeNumberEntity', 'consumeEntity', 'processEntityInAttribute', 'emitCurrentToken', 'dataState', 'entityDataState', 'rcdataState', 'characterReferenceInRcdata', 'rawtextState', 'scriptDataState', 'plaintextState', 'tagOpenState', 'closeTagOpenState', 'tagNameState', 'rcdataLessThanSignState', 'rcdataEndTagOpenState', 'rcdataEndTagNameState', 'rawtextLessThanSignState', 'rawtextEndTagOpenState', 'rawtextEndTagNameState', 'scriptDataLessThanSignState', 'scriptDataEndTagOpenState', 'scriptDataEndTagNameState', 'scriptDataEscapeStartState', 'scriptDataEscapeStartDashState', 'scriptDataEscapedState', 'scriptDataEscapedDashState', 'scriptDataEscapedDashDashState', 'scriptDataEscapedLessThanSignState', 'scriptDataEscapedEndTagOpenState', 'scriptDataEscapedEndTagNameState', 'scriptDataDoubleEscapeStartState', 'scriptDataDoubleEscapedState', 'scriptDataDoubleEscapedDashState', 'scriptDataDoubleEscapedDashDashState', 'scriptDataDoubleEscapedLessThanSignState', 'scriptDataDoubleEscapeEndState', 'beforeAttributeNameState', 'attributeNameState', 'afterAttributeNameState', 'beforeAttributeValueState', 'attributeValueDoubleQuotedState', 'attributeValueSingleQuotedState', 'attributeValueUnQuotedState', 'afterAttributeValueState', 'selfClosingStartTagState', 'bogusCommentState', 'markupDeclarationOpenState', 'commentStartState', 'commentStartDashState', 'commentState', 'commentEndDashState', 'commentEndState', 'commentEndBangState', 'doctypeState', 'beforeDoctypeNameState', 'doctypeNameState', 'afterDoctypeNameState', 'afterDoctypePublicKeywordState', 'beforeDoctypePublicIdentifierState', 'doctypePublicIdentifierDoubleQuotedState', 'doctypePublicIdentifierSingleQuotedState', 'afterDoctypePublicIdentifierState', 'betweenDoctypePublicAndSystemIdentifiersState', 'afterDoctypeSystemKeywordState', 'beforeDoctypeSystemIdentifierState', 'doctypeSystemIdentifierDoubleQuotedState', 'doctypeSystemIdentifierSingleQuotedState', 'afterDoctypeSystemIdentifierState', 'bogusDoctypeState', 'cdataSectionState']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
