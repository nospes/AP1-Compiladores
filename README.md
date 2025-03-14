# 🚀 Compilador PascalLite

Bem-vindo ao repositório do **Compilador PascalLite**, desenvolvido para a disciplina de **Compiladores**. Este projeto implementa as fases de **Análise Léxica e Sintática** para a linguagem **PascalLite**.

---

## 🧭 Navegação Rápida

- [📌 Sobre o Projeto](#-sobre-o-projeto)
- [🛠️ Tecnologias Utilizadas](#️-tecnologias-utilizadas)
- [🏗️ Estrutura do Projeto](#️-estrutura-do-projeto)
- [⚙️ Como Configurar o Ambiente](#️-como-configurar-o-ambiente)
- [🛠️ Comandos Disponíveis no Makefile](#-comandos-disponíveis-no-makefile)
- [📝 Funcionamento do Programa](#-Funcionamento-do-programa)
- [📖 Saiba mais na nossa wiki ](#-saiba-mais-na-wiki)

---

## 📌 Sobre o Projeto

O **PascalLite** é uma versão simplificada da linguagem Pascal, contendo apenas:

- **Tipos de dados:** `integer`, `boolean`
- **Comandos:** `if`, `while`, `begin...end`, `:=`, `read()`, `write()`
- **Operadores:** `=, <, >, <=, >=, <>, +, -, or, *, /, div, mod, and, not`
- **Comentários:** `//`, `{...}`, `(* ... *)`

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 🐍
- **Ferramentas:** GitHub, GitHub Actions, `pytest` para testes
- **Gerenciamento:** Makefile para automatização de comandos
- **Estrutura do Código:** Implementação baseada em análise descendente recursiva

---

## 🏗️ Estrutura do Projeto

```plaintext
📁 AP1-Compiladores/
├── 📂 src/           → Código-fonte do compilador
├── 📂 tests/         → Testes automatizados
├── 📄 README.md      → Este arquivo
├── 📄 requirements.txt → Dependências do projeto
├── 📄 Makefile       → Comandos de automação
```

---

## ⚙️ Como Configurar o Ambiente

- Siga os passos abaixo para configurar e executar o projeto localmente.

## 1️⃣ Clone o Repositório

```
git clone https://github.com/seu-usuario/AP1-Compiladores.git
cd AP1-Compiladores
```

## 2️⃣ Criar o Ambiente Virtual e Instalar Dependências

```
make install
```

## 3️⃣ Atualizar as Dependências (se necessário)

```
make update
```

## 4️⃣ Rodar o Programa Manualmente

```
make run
```

## 5️⃣ Rodar Todos os Testes

```
make test
```

## 6️⃣ Rodar Testes Específicos

- Apenas o Lexer

```
make test_lexer
```

- Apenas o Parser

```
make test_parser
```

## 7️⃣ Limpar Arquivos Temporários

```
make clean
```

## 🚀 Comandos Disponíveis no Makefile

- make install → Cria o ambiente virtual e instala as dependências.
- make update → Atualiza as dependências do projeto.
- make run → Executa o programa principal (main.py).
- make test → Executa todos os testes com pytest.
- make test_lexer → Executa apenas os testes do Lexer.
- make test_parser → Executa apenas os testes do Parser.
- make clean → Remove arquivos temporários e caches de testes.
- make setup → Comando que instala o ambiente e as dependências.
- make all → Comando padrão para rodar todos os testes.

---
## 📝 Funcionamento do Programa

escreva aqui! 📝
--- 
## 📖 Saiba Mais na Wiki

- 📌 Todas as informações detalhadas sobre o projeto estão na nossa [Wiki](https://github.com/millagmgomes/AP1-Compiladores/wiki)

- 📢 Dúvidas? Verifique a Wiki ou entre no grupo do WhatsApp para suporte! 🚀
