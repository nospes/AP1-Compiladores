from src.lexer import Lexer

class Parser:
    def __init__(self, lexer):
        
        # Inicializa o analisador sintático, recebendo um objeto Lexer para análise léxica.
        
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()  # Obtém o primeiro token

    def consume(self, token_type, expected=None):
        """
        Verifica se o token atual corresponde ao esperado. 
        Se for diferente, exibe um erro sintático e encerra a execução.

        :param token_type: Tipo esperado do token (ex: 'RESERVED', 'DELIMITER').
        :param expected: Lexema específico esperado (ex: 'program', ';').
        """
        if self.current_token[0] == token_type and (expected is None or self.current_token[1] == expected):
            self.current_token = self.lexer.get_next_token()  # Avança para o próximo token
        else:
            print(f"Erro sintático: esperado [{token_type} {expected or ''}], encontrado [{self.current_token[0]} {self.current_token[1]}] na linha {self.current_token[2]}")
            exit(1)

    def program(self):
        """
        Implementa a regra:
        <programa> ::= program identificador [( <lista de identificadores> )] ; <bloco>.
        """
        self.consume('RESERVED', 'program')  # Espera a palavra reservada "program"
        self.consume('IDENTIFIER')  # Espera um identificador (nome do programa)
        self.consume('DELIMITER', ';')  # Espera ponto e vírgula ';'
        self.block()  # Processa o bloco principal do programa
        self.consume('DELIMITER', '.')  # Espera ponto final '.'

    def block(self):
        """
        Implementa a regra:
        <bloco> ::= [<declarações de variáveis>] <comando composto>
        """
        if self.current_token[1] == 'var':
            self.variable_declarations()
        self.compound_command()  # Processa os comandos do bloco

    def variable_declarations(self):
        """
        Implementa a regra:
        <declarações de variáveis> ::= var <declaração> {; <declaração> };
        """
        self.consume('RESERVED', 'var')  # Espera a palavra reservada "var"
        while self.current_token[0] == 'IDENTIFIER':  # Enquanto houver identificadores
            self.declaration()
            self.consume('DELIMITER', ';')  # Espera ';' após cada declaração

    def declaration(self):
        """
        Implementa a regra:
        <declaração> ::= <lista de identificadores> : <tipo>
        """
        self.identifier_list()
        self.consume('COLON')  # Espera o caractere ':'
        self.variable_type()  # Processa o tipo da variável

    def identifier_list(self):
        """
        Implementa a regra:
        <lista de identificadores> ::= identificador { , identificador }
        """
        self.consume('IDENTIFIER')  # Espera um identificador
        while self.current_token[1] == ',':  # Se houver mais identificadores, processa-os
            self.consume('DELIMITER', ',')
            self.consume('IDENTIFIER')

    def variable_type(self):
        """
        Implementa a regra:
        <tipo> ::= integer | boolean
        """
        if self.current_token[1] in ('integer', 'boolean'):
            self.consume('RESERVED')  # Espera "integer" ou "boolean"
        else:
            print(f"Erro sintático: tipo inválido [{self.current_token[1]}] na linha {self.current_token[2]}")
            exit(1)

    def compound_command(self):
        """
        Implementa a regra:
        <comando composto> ::= begin <comando> { ; <comando> } end
        """
        self.consume('RESERVED', 'begin')  # Espera "begin"
        self.command()  # Processa o primeiro comando
        while self.current_token[1] == ';':  # Permite múltiplos comandos separados por ';'
            self.consume('DELIMITER', ';')
            self.command()
        self.consume('RESERVED', 'end')  # Espera "end" para fechar o bloco de comandos

    def command(self):
        """
        Implementa a regra:
        <comando> ::= <atribuição> | <comando if> | <comando while> | <comando composto>
        """
        if self.current_token[0] == 'IDENTIFIER':  # Se começa com identificador, é uma atribuição
            self.assignment()
        elif self.current_token[1] == 'if':  # Comando condicional "if"
            self.if_command()
        elif self.current_token[1] == 'while':  # Comando de repetição "while"
            self.while_command()
        elif self.current_token[1] == 'begin':  # Bloco de comandos
            self.compound_command()
        else:
            print(f"Erro sintático: comando inválido [{self.current_token[1]}] na linha {self.current_token[2]}")
            exit(1)

    def assignment(self):
        """
        Implementa a regra:
        <atribuição> ::= identificador := <expressao>
        """
        self.consume('IDENTIFIER')  # Espera um identificador
        self.consume('ASSIGNMENT')  # Espera ':='
        self.consume('NUMBER')  # Neste ponto, apenas aceita números (expressões serão adicionadas depois)
