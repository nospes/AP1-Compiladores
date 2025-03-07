# Caminho para o ambiente virtual 
VENV=venv

# Definir o interpretador Python
PYTHON=$(VENV)/bin/python

# Instalar dependências
install:
	python -m venv $(VENV)
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

# Executar os testes
test:
	$(PYTHON) -m unittest discover tests/

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
