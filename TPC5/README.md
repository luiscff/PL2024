# TPC5
**Título:** Máquina de Venda Automática

**Autor:** Luís Carlos Fragoso Figueiredo, a100549

1. **Descrição:** Este script em Python implementa uma máquina de venda automática através do uso de um lexer e de um parser. O programa lê um arquivo JSON para carregar o stock de produtos que ele assume que existe. Cada produto tem um código, nome, quantidade e preço. O usuário pode interagir com a máquina através de comandos de texto.

2. **Funcionalidades Implementadas:**
Todas as funcionalidades básicas foram implementadas. 
O programa:
- Carrega o stock de produtos a partir de um arquivo JSON. 
- Exibe uma mensagem de boas-vindas e a data atual ao iniciar.
- Aceita e executa como é suposto todos os comandos propostos.
- A cada interação, exibe o que é suposto num estilo igual ou semelhante ao proposto
- Ao sair do programa, guarda o estado no stock.json.


3. **Funcionalidades Extra:**
- Foi acrescentado o comando HELP que exibe uma mensagem de ajuda que lista todos os comandos disponíveis.
- Lida com comandos inválidos, exibindo uma mensagem de erro apropriada, sugerindo a utilização do comando HELP.
- Aquando a seleção de um produto, o programa lida com situações em que o produto não existe ou o stock do mesmo está vazio.
- Caso o stock inicial esteja vazio (ao dar load do json), o programa exibe uma mensagem de erro que informa que é preciso ter stock e sai. 


4. **Implementação:** O programa utiliza a biblioteca ply (Python Lex-Yacc) para analisar os comandos do utilizador. Cada comando é tokenizado e analisado para determinar a ação apropriada. O estado da máquina de venda automática, incluindo o saldo e o estoque de produtos, é mantido numa instância da classe Vending_Machine.

5. **Instruções de Uso:**

- Altere o ficheiro stock.json de modo a que este corresponda ao stock que deseja utilizar

- Execute o script Python
    ```bash
    python3 main.py
    ```

- Digite comandos para interagir com a máquina de venda automática. Para saber que comandos existem use o comando "HELP"

Este programa foi útil para aprender e aplicar os conceitos básicos de análise léxica e parsing.