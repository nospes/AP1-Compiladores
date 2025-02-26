import re

#Inicio do Lexer (onde iremos definir todos os atributos para ignorar)
class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0
        self.line = 1
        self.reserved_words = {"begin", "boolean", "div", "do", "else", "end", "false", "if", "integer", "mod", "program", "read", "then", "true", "not", "var", "while", "write"}
        self.token_patterns = [
            (r'\s+', None),  # Espaços e quebras de linha
            (r'//.*', None),  # Comentário de linha
            (r'\(\*.*?\*\)', None),  # Comentário de bloco (* ... *)
            (r'\{.*?\}', None),  # Comentário de bloco { ... }
            (r'[a-zA-Z_][a-zA-Z0-9_]{0,19}', self.handle_identifier),  # Identificadores
            (r'\d+', 'NUMERO'),  # Números inteiros
            (r':=', 'ATRIBUICAO'),  # Atribuição
            (r':', 'DOIS_PONTOS'),  # Adicionando ":" corretamente
            (r'[<>]=?|=', 'RELACIONAL'),  # Operadores relacionais
            (r'[+\-*/]', 'ARITMETICO'),  # Operadores aritméticos
            (r'[();,\.]', 'DELIMITADOR')  # Delimitadores
        ]

    
    def handle_identifier(self, lexeme):
        return ('RESERVADA', lexeme) if lexeme in self.reserved_words else ('IDENTIFICADOR', lexeme)
    
    def get_next_token(self):
        if self.position >= len(self.source_code):
            return ('EOF', 'EOF')
        
        for pattern, token_type in self.token_patterns:
            match = re.match(pattern, self.source_code[self.position:])
            
            if match:
                lexeme = match.group(0)
                self.position += len(lexeme)
                
                if token_type is None:  # Para ignorar espaços e comentarios
                    return self.get_next_token()
                
                if callable(token_type):
                    return token_type(lexeme)
                
                return (token_type, lexeme)
        
        return ('ERRO', self.source_code[self.position])

# Teste (Use qualquer linguagem)
source_code = """
program exemplo;
begin
    var x: integer;
    x := 10;
    if x > 5 then write(x);
end.
"""
lexer = Lexer(source_code)
while True:
    token = lexer.get_next_token()
    print(token)
    if token[0] == 'EOF':
        break
