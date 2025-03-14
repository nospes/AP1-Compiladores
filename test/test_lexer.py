from src.lexer import Lexer

def test_reserved_words():
    lexer = Lexer("program\nbegin\nend\nif\nthen\nelse\nwhile\ndo\nvar\ninteger\nboolean\nread\nwrite")
    expected_tokens = [
        ('PROGRAM', 'program', 1),
        ('BEGIN', 'begin', 2),
        ('END', 'end', 3),
        ('IF', 'if', 4),
        ('THEN', 'then', 5),
        ('ELSE', 'else', 6),
        ('WHILE', 'while', 7),
        ('DO', 'do', 8),
        ('VAR', 'var', 9),
        ('INTEGER', 'integer', 10),
        ('BOOLEAN', 'boolean', 11),
        ('READ', 'read', 12),
        ('WRITE', 'write', 13),
        ('EOF', 'EOF', 13)
    ]
    for expected in expected_tokens:
        assert lexer.get_next_token() == expected

def test_identifier():
    lexer = Lexer("_id1\ntest_2\nabc123")
    expected_tokens = [
        ('IDENTIFICADOR', '_id1', 1),
        ('IDENTIFICADOR', 'test_2', 2),
        ('IDENTIFICADOR', 'abc123', 3),
        ('EOF', 'EOF', 3)
    ]
    for expected in expected_tokens:
        assert lexer.get_next_token() == expected

def test_numbers():
    lexer = Lexer("123\n456\n789")
    expected_tokens = [
        ('NUMERO', '123', 1),
        ('NUMERO', '456', 2),
        ('NUMERO', '789', 3),
        ('EOF', 'EOF', 3)
    ]
    for expected in expected_tokens:
        assert lexer.get_next_token() == expected

def test_invalid_character():
    lexer = Lexer("#")
    token = lexer.get_next_token()
    assert token[0] == 'ERRO_LEXICO'

def test_comments():
    lexer = Lexer("// Comment\nprogram\n(* block comment *)\nvar")
    expected_tokens = [
        ('PROGRAM', 'program', 2),
        ('VAR', 'var', 4),
        ('EOF', 'EOF', 4)
    ]
    for expected in expected_tokens:
        assert lexer.get_next_token() == expected
