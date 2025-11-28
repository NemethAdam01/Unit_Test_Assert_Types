import pytest
from text_processor import TextProcessor


def test_capitalize_text_equal():
    """1. Assert equal - egyenlőség ellenőrzés"""
    processor = TextProcessor()
    result = processor.capitalize_text("hello world")
    assert result == "HELLO WORLD"


def test_capitalize_text_not_equal():
    """2. Assert not equal - nem egyenlő"""
    processor = TextProcessor()
    result = processor.capitalize_text("hello world")
    assert result != "hello world"
    assert result != "Hello World"


def test_reverse_text_in():
    """3. Assert in - benne van"""
    processor = TextProcessor()
    result = processor.reverse_text("hello")
    assert 'o' in result
    assert 'l' in result
    assert 'olleh' in result


def test_reverse_text_not_in():
    """4. Assert not in - nincs benne"""
    processor = TextProcessor()
    result = processor.reverse_text("hello")
    assert 'hello' not in result


def test_count_words_isinstance():
    """5. Assert isinstance - típus ellenőrzés"""
    processor = TextProcessor()
    result = processor.count_words("Hello World")
    assert isinstance(result, int)
    assert not isinstance(result, str)


def test_count_words_greater_less():
    """6. Assert >, <, >=, <= - összehasonlítás"""
    processor = TextProcessor()
    result = processor.count_words("Hello World")
    assert isinstance(result, int) and result > 1


def test_count_words_empty_string():
    """7. Üres sztring bemenet ellenőrzése"""
    processor = TextProcessor()
    result = processor.count_words("")
    assert isinstance(result, int) and result == 0


def test_is_palindrome_true_false():
    """8. Assert True/False - boolean ellenőrzés"""
    processor = TextProcessor()
    result = processor.is_palindrome("anna")
    assert  result is True


def test_remove_spaces_multiple_asserts():
    """9. Több assert egy tesztben"""
    processor = TextProcessor()
    result = processor.remove_spaces("anna anna")
    result2 = processor.is_palindrome("anna anna")
    assert result == "annaanna" and result2 is True and isinstance(result, str)