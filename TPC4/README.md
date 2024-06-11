# TPC4
**Título:** Analisador Léxico

**Autor:** Luís Carlos Fragoso Figueiredo, a100549

1. **Descrição:**
    Este script em Python implementa um analisador léxico para a linguagem SQL. É utilizada a biblioteca Ply (Python Lex-Yacc) para realizar a análise léxica, identificando tokens como comandos (`SELECT`, `FROM`, `WHERE`, etc.), outras palavras-chave específicas da linguagem SQL (como `as`, `or`, etc.), operadores matemáticos (`+`, `-`, `*`, `/`), e valores numéricos. 

2. **Funcionalidades Implementadas:**
    - Reconhece comandos SQL como tokens individuais.
    - Identifica operadores matemáticos.
    - Reconhece valores numéricos.
    - Identifica delimitadores como vírgulas e parênteses.
    - Gestão de erros para tokens inválidos.
    - Ignora espaços em branco e quebras de linha (`\n`).
    - Distinção entre o operador de multiplicação (`*`) e o `*` que significa ALL no comando `SELECT *`.

3. **Implementação:**
    O programa utiliza expressões regulares para definir padrões de tokens. Cada padrão corresponde a um tipo de token, como comandos, operadores, números, etc. Ao encontrar um padrão correspondente, o lexer atribui o tipo de token apropriado e continua analisando o texto fornecido. A variável `is_prev_SELECT` é utilizada para manter o contexto de se o `*` é precedido de `SELECT` ou não, permitindo a distinção entre o comando `SELECT *` e o operador de multiplicação `*`.

4. **Instruções de Uso:**
    - Execute o script Python 
    ```bash
    python3 main.py
    ```
    - O programa realizará automaticamente a análise léxica dos exemplos fornecidos no final do código e os resultados da análise serão exibidos no terminal.

Este programa é útil para estudar os conceitos básicos de análise léxica e para implementar analisadores léxicos para outras linguagens de programação ou formatos de arquivo.