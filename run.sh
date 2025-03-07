#!/bin/bash

echo "🚀 Iniciando o Compilador PascalLite..."

# Ativar ambiente virtual
if [ -d "venv" ]; then
    source venv/bin/activate
    echo "✅ Ambiente virtual ativado!"
else
    echo "❌ Erro: Ambiente virtual não encontrado! Execute ./setup.sh primeiro."
    exit 1
fi

# Rodar o projeto
if [ -f "main.py" ]; then
    python main.py
else
    echo "❌ Erro: Arquivo main.py não encontrado!"
    exit 1
fi
