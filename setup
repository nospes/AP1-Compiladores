#!/bin/bash

echo "🚀 Configurando o ambiente Python..."

# Criar ambiente virtual se não existir
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Ambiente virtual criado!"
fi

# Ativar o ambiente virtual
source venv/bin/activate
echo "✅ Ambiente virtual ativado!"

# Instalar dependências se `requirements.txt` existir
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    echo "✅ Dependências instaladas!"
else
    echo "⚠️ Arquivo requirements.txt não encontrado!"
fi

echo "🎯 O ambiente está pronto! Agora você pode rodar o projeto com './run.sh'"
