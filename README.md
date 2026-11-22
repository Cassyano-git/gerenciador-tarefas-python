# gerenciador-tarefas-python

Projeto de linha de comando (CLI) desenvolvido em Python para adicionar, listar e remover tarefas de forma simples no terminal, com salvamento em arquivo de texto.

## Funcionalidades
- Adicionar novas tarefas à lista.
- Listar tarefas numeradas (`enumerate`).
- Remover tarefas pelo número ou pelo nome.
- Limpeza de tela entre ações usando o módulo `os`.
- Tratamento de entradas inválidas com `try` / `except`.

## Tecnologias e conceitos utilizados
- Python 3
- Listas, laços (`while`, `for`) e condicionais
- Funções (`def`)
- Manipulação de arquivos (`open`, `with`)
- Módulos nativos (`os`)

## Como executar
1. Certifique-se de ter o Python 3 instalado (ou use um ambiente como o Pydroid 3 no Android).
2. Baixe ou clone este repositório.
3. Execute o arquivo principal no terminal:
   ```bash
   python tarefas.py
   ```

## Próximos passos / Melhorias futuras
- Evitar tarefas duplicadas ao adicionar.
- Marcar tarefas como concluídas.
- Melhorar a organização de mensagens e validações.
- salvamento em documento, utilizando '.txt'.
