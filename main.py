from src.lexer import Lexer


if __name__ == "__main__":
    source_code = """
    program exemplo;
    var x: integer;
    begin
        x := 10;
        if x > 5 then write(x);
    end.
    """

    print("\n--- Tokens Reconhecidos ---\n")
    lexer = Lexer(source_code)
    while True:
        token = lexer.get_next_token()
        print(f"Linha {token[2]:<3} -> Tipo: {token[0]:<15} Lexema: {token[1]}")
        if token[0] == 'EOF':
            break
