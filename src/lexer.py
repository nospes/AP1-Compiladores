import re

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0
        self.line = 1

        self.reserved_words = {
            "begin", "boolean", "div", "do", "else", "end", "false", "if", "integer",
            "mod", "program", "read", "then", "true", "not", "var", "while", "write"
        }

        self.token_patterns = [
            (r'\s+', None),  # Espaços em branco e quebras de linha
            (r'//.*', None),  # Comentário de linha
            (r'\(\*[\s\S]*?\*\)', None),  # Comentário de bloco (* ... *)
            (r'\{[\s\S]*?\}', None),  # Comentário de bloco { ... }
            (r':=', 'ATRIBUICAO'),  # Atribuição :=
            (r':', 'DOIS_PONTOS'),  # Dois pontos :
            (r'<>|>=|<=|>|<|=', 'RELACIONAL'),  # Operadores relacionais
            (r'\+|-|or', 'ADICAO'),  # Operadores de adição
            (r'\*|/|div|mod|and', 'MULTIPLICACAO'),  # Operadores de multiplicação
            (r'[();,\.]', 'DELIMITADOR'),  # Delimitadores
            (r'\b(?:' + '|'.join(self.reserved_words) + r')\b', self.handle_reserved_word),  # Palavras reservadas
            (r'[_a-zA-Z][_a-zA-Z0-9]{0,19}', self.handle_identifier),  # Identificadores
            (r'\d+', self.handle_number)  # Números inteiros
        ]

    def handle_reserved_word(self, lexeme):
        """ Trata palavras reservadas diretamente """
        return ('RESERVADA', lexeme, self.line)

    def handle_identifier(self, lexeme):
        """ Verifica se o identificador é válido """
        if len(lexeme) > 20:
            return ('ERRO', f"Identificador muito longo na linha {self.line}: {lexeme}", self.line)
        return ('IDENTIFICADOR', lexeme, self.line)

    def handle_number(self, lexeme):
        """ Verifica se o número é válido """
        if len(lexeme) > 20:
            return ('ERRO', f"Número muito longo na linha {self.line}: {lexeme}", self.line)
        return ('NUMERO', lexeme, self.line)

    def get_next_token(self):
        """ Retorna o próximo token """
        if self.position >= len(self.source_code):
            return ('EOF', 'EOF', self.line)

        for pattern, token_type in self.token_patterns:
            match = re.match(pattern, self.source_code[self.position:], re.DOTALL)
            if match:
                lexeme = match.group(0)
                self.position += len(lexeme)

                if '\n' in lexeme:
                    self.line += lexeme.count('\n')

                if token_type is None:  # Ignorar espaços e comentários
                    return self.get_next_token()

                if callable(token_type):
                    return token_type(lexeme)

                return (token_type, lexeme, self.line)

        # Se nenhum padrão for encontrado, erro léxico
        erro_lexema = self.source_code[self.position] if self.position < len(self.source_code) else "EOF"
        erro_mensagem = f"Erro léxico na linha {self.line}: caractere inválido '{erro_lexema}'"
        self.position += 1  # Avança para evitar loop infinito
        return ('ERRO', erro_mensagem, self.line)