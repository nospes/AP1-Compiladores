import pytest
from parser import Parser
from lexer import Lexer

def test_valid_program():
    """
    Testa se o parser aceita um programa PascalLite válido.
    """
    source_code = """
    program exemplo;
    var x: integer;
    begin
        x := 10;
    end.
    """
    lexer = Lexer(source_code)
    parser = Parser(lexer)

    try:
        parser.program()
        success = True
    except SystemExit:
        success = False
    
    assert success, "O parser não aceitou um programa válido!"

def test_missing_semicolon():
    """
    Testa se o parser detecta um ponto e vírgula ausente.
    """
    source_code = """
    program exemplo
    var x: integer;
    begin
        x := 10;
    end.
    """
    lexer = Lexer(source_code)
    parser = Parser(lexer)

    with pytest.raises(SystemExit):
        parser.program()

def test_invalid_identifier():
    """
    Testa se o parser detecta um identificador inválido.
    """
    source_code = """
    program 123exemplo;
    var x: integer;
    begin
        x := 10;
    end.
    """
    lexer = Lexer(source_code)
    parser = Parser(lexer)

    with pytest.raises(SystemExit):
        parser.program()

if __name__ == '__main__':
    pytest.main()
