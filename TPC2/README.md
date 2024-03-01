# TPC2
**Título:** Conversor de Markdown para HTML

**Autor:** Luís Carlos Fragoso Figueiredo, a100549

1. **Descrição:**
    Este script em Python converte texto formatado em Markdown para HTML. Ele fornece uma maneira fácil de transformar strings escritas em Markdown para HTML para visualização na web.

2. **Funcionalidades pedidas:**
    - Converte cabeçalhos de diferentes níveis (de h1 a h6).
    - Suporta negrito e itálico.
    - Converte listas numeradas.
    - Transforma links em tags HTML correspondentes.
    - Transforma imagens em tags HTML correspondentes.
    - Lida com blocos de código (na mesma linha).
    
3. **Funcionalidades extra:**
    - Suporta blocos de código multi-linha, tanto com especificação de linguagem quanto sem ela.
    - Suporta listas não numeradas
    - Envolve citações em blocos `<blockquote>`.
    - Adiciona regras horizontais `<hr>`.
    - Envolve parágrafos em tags `<p>`.

4. **Funcionamento do programa:**
    O script começa por verificar se foi fornecida uma string como argumento da linha de comando. Se tal ocorrer, essa string é usada como entrada para a conversão de Markdown para HTML. Caso contrário, o script utiliza uma string de testes incorporada no código.
    Em seguida, é invocada a função `convert_to_html()` para efetuar a conversão da string Markdown em HTML, aplicando todas as transformações necessárias de acordo com as regras definidas de modo a cumprir todas as funcionalidades listadas anteriormente (em 2. e em 3.).
    O HTML resultante é então exibido no terminal e também é guardado num ficheiro chamado `output.html`.
    Por fim, o ficheiro HTML gerado é aberto no browser (caso não queira esta funcionalidade, basta comentar a linha `webbrowser.open("output.html")`).



5. **Instruções de Uso:**
    - Execute o script sem argumentos, ele vai usar uma string de testes *hard-coded*: 
    ```
    python3 main.py
    ```
    **ou**
    Execute o script com uma string qualquer como argumento: 
    ```
    python3 main.py "esta é a string"
    ```
    - O HTML convertido será exibido no terminal e também será salvo em um arquivo chamado `output.html`.