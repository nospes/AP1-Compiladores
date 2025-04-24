from src.lexer import Lexer
from src.parser import Parser


if __name__ == "__main__":
    code = """
    program exemplo;
    var
        fat, num, cont: integer;
    begin
        read(num);
        fat := 1;
        cont := 2;
        while cont <= num do
        begin
            fat := fat * num;
            cont := cont + 1;
        end;
        write(fat);
    end.

    """

    lexer = Lexer(code)
    parser = Parser(lexer)
    
    try:
        parser.program()
        print("Programa analisado com sucesso!")
    except SystemExit:
        print("Erro durante a análise do programa.")
        