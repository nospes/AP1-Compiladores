from src.lexer import Lexer
from src.parser import Parser
import pytest

def test_program_header():
    code = """
    program exemplo;
    begin
    end.
    """
    lexer = Lexer(code)
    parser = Parser(lexer)
    parser.program()


def test_variable_declarations():
    code = """
    program exemplo;
    var 
        x, y: integer;
        flag: boolean;
    begin
    end.
    """
    lexer = Lexer(code)
    parser = Parser(lexer)
    parser.program()


def test_simple_command():
    code = """
    program exemplo;
    var 
        x: integer;
    begin
        x := 10;
    end.
    """
    lexer = Lexer(code)
    parser = Parser(lexer)
    parser.program()


def test_if_without_else():
    code = """
    program exemplo;
    var 
        x, y: integer;
    begin
        if x > y then
            x := y;
    end.
    """
    lexer = Lexer(code)
    parser = Parser(lexer)
    parser.program()


def test_if_with_else():
    code = """
    program exemplo;
    var 
        x, y: integer;
    begin
        if x > y then
            x := y;
        else
            y := x;
    end.
    """
    lexer = Lexer(code)
    parser = Parser(lexer)
    parser.program()
