import src.lexer as Lexer
from .tabela_simbolos import adicionar, buscar, total

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
        self.rotulo = 0

    def gerar_rotulo(self):
        "Gera Rotulos para controles de fluxo do programa"
        self.rotulo += 1
        return self.rotulo

    def error(self, message):
        """Exibe uma mensagem de erro detalhada."""
        print(f"Erro sintático: {message} na linha {self.current_token[2]}")
        exit(1)

    def consume(self, token_type, expected=None):
        """Consome o token atual se ele corresponder ao esperado."""
        if self.current_token[0] == token_type and (expected is None or self.current_token[1] == expected):
            #print(f"Linha: {self.current_token[2]} - atomo: {self.current_token[0]} lexema: {self.current_token[1]}")
            self.current_token = self.lexer.get_next_token()
        else:
            expected_str = f"{token_type} {expected}" if expected else token_type
            self.error(f"esperado [{expected_str}], encontrado [{self.current_token[0]} {self.current_token[1]}]")

    def program(self):
        """Analisa a estrutura principal do programa."""
        #Agora inicia e termina o programa
        print("INPP") #
        self.consume('PROGRAM')
        self.consume('IDENTIFICADOR')
        self.consume('PONTO_VIRGULA')
        self.block()
        print("PARA")
        self.consume('PONTO_FINAL')

    def block(self):
        """Analisa o bloco principal, incluindo declarações e comandos."""
        #Block agora declara a alocação de memoria (AMEM)
        if self.current_token[0] == 'VAR':
            self.variable_declarations()
        print(f"AMEM {total()}") 
        self.compound_command()

    def variable_declarations(self):
        """Analisa as declarações de variáveis."""
        self.consume('VAR')
        while self.current_token[0] == 'IDENTIFICADOR':
            self.declaration()
            self.consume('PONTO_VIRGULA')

    def declaration(self):
        """Analisa uma única declaração de variável."""
        self.identifier_list()
        self.consume('DOIS_PONTOS')
        self.variable_type()

    def identifier_list(self):
        """Analisa uma lista de identificadores."""
        ident = self.current_token[1]
        self.consume('IDENTIFICADOR')
        adicionar(ident)
        while self.current_token[0] == 'VIRGULA':
            self.consume('VIRGULA')
            ident = self.current_token[1]
            self.consume('IDENTIFICADOR')
            adicionar(ident)

    def variable_type(self):
        """Verifica o tipo de variável."""
        if self.current_token[0] in ('INTEGER', 'BOOLEAN'):
            self.consume(self.current_token[0])
        else:
            self.error(f"tipo inválido [{self.current_token[1]}]")

    def compound_command(self):
        """Analisa comandos compostos."""
        self.consume('BEGIN')
        while self.current_token[0] not in ('END', 'ELSE'):
            self.command()
            if self.current_token[0] == 'PONTO_VIRGULA':
                self.consume('PONTO_VIRGULA')
            else:
                break
        if self.current_token[0] == 'END':
            self.consume('END')

    def command(self):
        """Identifica e analisa o tipo de comando."""
        if self.current_token[0] == 'IDENTIFICADOR':
            self.assignment()
        elif self.current_token[0] == 'IF':
            self.if_command()
        elif self.current_token[0] == 'WHILE':
            self.while_command()
        elif self.current_token[0] == 'READ':
            self.read_command()
        elif self.current_token[0] == 'WRITE':
            self.write_command()
        elif self.current_token[0] == 'BEGIN':
            self.compound_command()
        else:
            self.error(f"comando inválido [{self.current_token[1]}]")

    def assignment(self):
        """Analisa um comando de atribuição."""
        # Agora imprime que armazena o resultado da expressão no endereço X
        ident = self.current_token[1]
        self.consume('IDENTIFICADOR')
        endereco = buscar(ident)
        self.consume('ATRIBUICAO')
        self.expression()
        print(f"ARMZ {endereco}")

    def if_command(self):
        """Analisa um comando condicional IF."""
        #Agora IF e WHILE tambem imprimem seus devidos comandos e definem os rotulos do fluxo do programa
        rot1 = self.gerar_rotulo()
        rot2 = self.gerar_rotulo()

        self.consume('IF')
        self.expression()
        print(f"DSVF L{rot1}")

        self.consume('THEN')
        self.command()
        print(f"DSVS L{rot2}")

        print(f"L{rot1}: NADA")

        if self.current_token[0] == 'ELSE':
            self.consume('ELSE')
            self.command()

        print(f"L{rot2}: NADA")

    def while_command(self):
        """Analisa um comando de repetição WHILE."""
        rot1 = self.gerar_rotulo()
        rot2 = self.gerar_rotulo()

        print(f"L{rot1}: NADA")
        self.consume('WHILE')
        self.expression()
        print(f"DSVF L{rot2}")
        self.consume('DO')
        self.command()
        print(f"DSVS L{rot1}")
        print(f"L{rot2}: NADA")

    def read_command(self):
        """Analisa um comando de entrada (READ)."""
        self.consume('READ')
        self.consume('ABRE_PARENTESE')
        ident = self.current_token[1]
        self.consume('IDENTIFICADOR')
        print("LEIT")
        print(f"ARMZ {buscar(ident)}")
        while self.current_token[0] == 'VIRGULA':
            self.consume('VIRGULA')
            ident = self.current_token[1]
            self.consume('IDENTIFICADOR')
            print("LEIT")
            print(f"ARMZ {buscar(ident)}")
        self.consume('FECHA_PARENTESE')

    def write_command(self):
        """Analisa um comando de saída (WRITE)."""
        self.consume('WRITE')
        self.consume('ABRE_PARENTESE')
        self.expression()
        print("IMPR")
        while self.current_token[0] == 'VIRGULA':
            self.consume('VIRGULA')
            self.expression()
            print("IMPR")
        self.consume('FECHA_PARENTESE')

    def expression(self):
        """Analisa expressões."""
        #Agora junto com "term" e "simple_expression" imprimem os tipos de diversos tipos de operações
        self.simple_expression()
        if self.current_token[0] == 'RELACIONAL':
            op = self.current_token[1]
            self.consume('RELACIONAL')
            self.simple_expression()
            if op == '>':
                print("CMMA")
            elif op == '<':
                print("CMME")
            elif op == '>=':
                print("CMAG")
            elif op == '<=':
                print("CMEG")
            elif op == '=':
                print("CMIG")
            elif op == '<>':
                print("CMDG")

    def simple_expression(self):
        """Analisa expressões simples."""
        self.term()
        while self.current_token[0] in ('ADICAO', 'OR'):
            op = self.current_token[1]
            self.consume(self.current_token[0])
            self.term()
            if op == '+':
                print("SOMA")
            elif op == '-':
                print("SUBT")

    def term(self):
        """Analisa termos de uma expressão."""
        self.factor()
        while self.current_token[0] in ('MULTIPLICACAO', 'DIV', 'MOD', 'AND'):
            op = self.current_token[1]
            self.consume(self.current_token[0])
            self.factor()
            if op == '*':
                print("MULT")
            elif op == '/':
                print("DIVI")
            elif op == 'div':
                print("DIVI")
            elif op == 'mod':
                print("MOD")

    def factor(self):
        """Analisa fatores de uma expressão."""
        # Agora além de analisar, tambem gera feedback ao carregar valores
        if self.current_token[0] == 'IDENTIFICADOR':
            endereco = buscar(self.current_token[1])
            print(f"CRVL {endereco}")
            self.consume('IDENTIFICADOR')
        elif self.current_token[0] == 'NUMERO':
            print(f"CRCT {self.current_token[1]}")
            self.consume('NUMERO')
        elif self.current_token[0] == 'TRUE':
            self.consume('TRUE')
        elif self.current_token[0] == 'FALSE':
            self.consume('FALSE')
        elif self.current_token[0] == 'NOT':
            self.consume('NOT')
            self.factor()
        elif self.current_token[0] == 'ABRE_PARENTESE':
            self.consume('ABRE_PARENTESE')
            self.expression()
            self.consume('FECHA_PARENTESE')
        else:
            self.error(f"fator inválido [{self.current_token[1]}]")