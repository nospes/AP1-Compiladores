# Tabela de Símbolos usada para controle de variáveis e memoria durante a análise semântica 
tabela = {}

def adicionar(ident):
    """Adiciona um novo identificador à tabela de símbolos"""
    if ident in tabela:
        raise Exception(f"Erro semântico: variável '{ident}' já foi declarada.")
    endereco = len(tabela)  # o endereço é definido pela ordem de inserção
    tabela[ident] = endereco

def buscar(ident):
    """Busca o endereço de memória de um identificador"""
    if ident not in tabela:
        raise Exception(f"Erro semântico: variável '{ident}' não declarada.")
    return tabela[ident]

def total():
    """Retorna o total de variáveis declaradas."""
    return len(tabela)

def limpar():
    """Limpa toda a tabela de símbolos."""
    tabela.clear()
