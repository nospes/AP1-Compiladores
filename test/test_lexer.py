import pytest
from lexer import Lexer

def test_reserved_words():
    """
    Testa se palavras reservadas são reconhecidas corretamente.
    """
    lexer = Lexer("program begin end if then while var integer boolean")
    tokens = [lexer.get_next_token() for _ in range(9)]
    expected_tokens = [
        ('RESERVED', 'program', 1),
        ('RESERVED', 'begin', 1),
        ('RESERVED', 'end', 1),
        ('RESERVED', 'if', 1),
        ('RESERVED', 'then', 1),
        ('RESERVED', 'while', 1),
        ('RESERVED', 'var', 1),
        ('RESERVED', 'integer', 1),
        ('RESERVED', 'boolean', 1)
    ]
    assert tokens == expected_tokens

def test_identifiers():
    """
    Testa se identificadores são reconhecidos corretamente.
    """
    lexer = Lexer("x y variable1 _teste")
    tokens = [lexer.get_next_token() for _ in range(4)]
    expected_tokens = [
        ('IDENTIFIER', 'x', 1),
        ('IDENTIFIER', 'y', 1),
        ('IDENTIFIER', 'variable1', 1),
        ('IDENTIFIER', '_teste', 1),
    ]
    assert tokens == expected_tokens

def test_numbers():
    """
    Testa se números inteiros são reconhecidos corretamente.
    """
    lexer = Lexer("42 123 999")
    tokens = [lexer.get_next_token() for _ in range(3)]
    expected_tokens = [
        ('NUMBER', '42', 1),
        ('NUMBER', '123', 1),
        ('NUMBER', '999', 1)
    ]
    assert tokens == expected_tokens

def test_symbols():
    """
    Testa se símbolos e operadores são reconhecidos corretamente.
    """
    lexer = Lexer(": ; := < > = + - * / and or div mod")
    tokens = [lexer.get_next_token() for _ in range(15)]
    expected_tokens = [
        ('COLON', ':', 1),
        ('DELIMITER', ';', 1),
        ('ASSIGNMENT', ':=', 1),
        ('RELATIONAL', '<', 1),
        ('RELATIONAL', '>', 1),
        ('RELATIONAL', '=', 1),
        ('ADDITION', '+', 1),
        ('ADDITION', '-', 1),
        ('MULTIPLICATION', '*', 1),
        ('MULTIPLICATION', '/', 1),
        ('MULTIPLICATION', 'and', 1),
        ('ADDITION', 'or', 1),
        ('MULTIPLICATION', 'div', 1),
        ('MULTIPLICATION', 'mod', 1),
    ]
    assert tokens == expected_tokens

if __name__ == '__main__':
    pytest.main()
