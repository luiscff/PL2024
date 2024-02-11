# TPC1
**Título:** Processamento de Dados CSV em Python

**Autor:** Luís Carlos Fragoso Figueiredo, a100549

1. **Descrição:**
    Este programa em Python lê um dataset de um ficheiro chamado `emd.CSV` que tem que estar na mesma pasta do script, processa-o e exibe os resultados que foram pedidos pelos professores. A única restrição é não poder usar o módulo CSV 

2. **Função `parseLine`:**
    - **Descrição:** Faz o parsing de uma linha em que os campos estão separados por vírgulas.
    - **Parâmetros:**
        - `linha (str)`: string que corresponde a uma linha do dataset.
    - **Retorna:**
        - Um tuplo que contém 3 strings correspondentes aos parâmetros "modalidade", "resultado" e "idade".

3. **Função `main`:**
    - **Descrição:** Função principal que executa o processamento dos dados CSV.
    - **Funcionamento:**
        - Abre o ficheiro CSV `emd.csv`;
        - Cria uma lista de linhas do CSV com a função `readlines()`;
        - Extrai certos campos de cada linha do CSV com ajuda da função `parseLine()`;
        - Processa os dados extraídos;
        - Exibe os resultados (lista de modalidades ordenadas alfabeticamente, as percentagens de atletas aptos e inaptos e a distribuição de atletas por faixa etária) no terminal.

4. **Exemplo de Uso:**
    - Certifique-se de que o ficheiro CSV `emd.csv` está no mesmo diretório que o script `main.py`;
    - Execute o programa com o comando:
    ``` 
    python3 main.py
    ```
    - Os resultados serão exibidos no terminal após a execução do programa.

