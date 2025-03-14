# Caminho para o ambiente virtual 
VENV=venv

# Definir o interpretador Python
PYTHON=$(VENV)/bin/python

# Instalar dependências
install:
	python -m venv $(VENV)
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

# Executar todos os testes
test:
	$(PYTHON) -m pytest -v test/

# Executar apenas o teste do Lexer
test_lexer:
	$(PYTHON) -m pytest -v test/test_lexer.py

# Executar apenas o teste do Parser
test_parser:
	$(PYTHON) -m pytest -v test/test_parser.py

# Executar o Lexer manualmente com `main.py`
run:
	$(PYTHON) main.py

# Limpar arquivos temporários
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
	find . -name "*.log" -delete
	rm -rf .pytest_cache
	rm -rf htmlcov

# Atualizar dependências
update:
	$(PYTHON) -m pip install --upgrade -r requirements.txt

# Criar um ambiente virtual e instalar dependências automaticamente
setup: install

# Comando padrão ao rodar `make`
all: test
