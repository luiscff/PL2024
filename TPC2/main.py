import re
import sys
import webbrowser

# string pa testes
markdown_example = """
# Título
Este é um **exemplo** de *Markdown*.

## listas
1. item 1
2. item 2
3. item 3
1. item 4
2. item 5
3. item 6

- First item
- Second item
- Third item

1. item 1
2. item 2

## Link
Veja mais em [Google](https://www.google.com).

## Imagem
![Fundo do meu Computador](test.jpg)


## Funcionalidades extra

### Paragrafo
Isto é um paragrafo.

### Código
`print("Hello World")`

### Código multi-line com linguagem
```python
print("Hello World")
print("Hello World again")
```

### Código multi-line sem linguagem
```
print("Hello World")
print("Hello World again")
```


### Horizontal Rules
---
------------------

### Citação
> Isto é uma citação.

### This aren't horizontal rules
- - -
--


"""


def convert_to_html(string: str):
    # Cabeçalhos
    string = re.sub(r"^# (.+)$", r"<h1>\1</h1>", string, flags=re.MULTILINE)
    string = re.sub(r"^## (.+)$", r"<h2>\1</h2>", string, flags=re.MULTILINE)
    string = re.sub(r"^### (.+)$", r"<h3>\1</h3>", string, flags=re.MULTILINE)
    string = re.sub(r"^#### (.+)$", r"<h4>\1</h4>", string, flags=re.MULTILINE)
    string = re.sub(r"^##### (.+)$", r"<h5>\1</h5>", string, flags=re.MULTILINE)
    string = re.sub(r"^###### (.+)$", r"<h6>\1</h6>", string, flags=re.MULTILINE)

    # Bold
    string = re.sub(r"\*\*(.+)\*\*", r"<b>\1</b>", string, flags=re.MULTILINE)

    # Itálico
    string = re.sub(r"\*(.+)\*", r"<i>\1</i>", string, flags=re.MULTILINE)

    # Ordered lists

    # mete um <ol> antes do 1º elemento de qualquer lista numerada
    string = re.sub(
        r"^(\d+\..+\n\d+\..+)+$",
        r"\n<ol>\n\1",
        string,
        count=1,
        flags=re.MULTILINE,
    )

    # mete um </ol> depois do ultimo elemento de qualquer lista numerada
    lista = re.findall(r"^\d+\..+$", string, flags=re.MULTILINE)
    if lista:
        string, substituiçoes = re.subn(
            re.escape(lista[-1]), lista[-1] + "\n</ol>", string
        )

    # tira os </ol> postos a mais (só acontece quando há o mesmo exato elemento com a mesma numeração em 2 listas diferentes)
    if lista:
        while substituiçoes > 1:
            string = re.sub(re.escape(lista[-1] + "\n</ol>"), lista[-1], string, 1)
            substituiçoes -= 1

    # divide em listas diferentes caso a numeração não seja sequencial (ou seja, caso haja mais do que uma lista numerada)
    num_experado = 1
    if lista:
        for item in lista:
            if num_experado == int(item[0]):
                num_experado += 1
                # adiciona um </ol>\n no fim do item caso seja o ultimo item da lista(ou seja, se o proximo item não for um numero sequencial)
                if lista.index(item) + 1 != len(lista) and num_experado != int(
                    lista[lista.index(item) + 1][0]
                ):
                    string = string.replace(item, item + "\n</ol>", 1)

            elif item[0] == "1":  # no caso de ser o inicio de uma nova lista
                inverted_string = string[::-1]
                inverted_item = item[::-1]
                addition = f"\n<ol>\n{item}"  # adiciona um <ol> antes de cada item inical de uma lista quando a numeração não é sequencial
                inverted_addition = addition[::-1]
                string = inverted_string.replace(inverted_item, inverted_addition, 1)[
                    ::-1
                ]

                num_experado = 2

    string = re.sub(r"^\d+\. (.+)$", r"  <li>\1</li>", string, flags=re.MULTILINE)

    # Unordered lists (nao precisa de existir <ul> e </ul> porque o browser trata disso automaticamente, bastam as <li> e </li>)
    string = re.sub(r"^- (.+)$", r"<li>\1</li>", string, flags=re.MULTILINE)

    # Imagens (é feito primeiro de modo a mudar logo a string para depois não haver match de imagens nos links)

    string = re.sub(r"!\[(.+)\]\((.+)\)", r'<img src="\2" alt="\1">', string)

    # Links

    string = re.sub(r"\[(.+)\]\((.+)\)", r'<a href="\2">\1</a>', string)

    # Funcionalidades extra

    # Código multi-line com linguagem
    string = re.sub(r"^```(.+)\n((?:.+\n?)+)\n```$", r'<pre>\n<code class="language-\1">\n\2\n</code>\n</pre>', string, flags=re.MULTILINE)
    # Código multi-line sem linguagem
    string = re.sub(r"^```\n((?:.+\n?)+)\n```$", r'<pre>\n<code>\n\1\n</code>\n</pre>', string, flags=re.MULTILINE)

    # Código
    string = re.sub(
        r"`(.+)`", r'<code>\1</code>', string, flags=re.MULTILINE
    )

    # Citação
    string = re.sub(r"^> (.+)$", r"<blockquote>\1</blockquote>", string, flags=re.MULTILINE)

    # Horizontal Rule
    string = re.sub(r"^-{3,}$", r"<hr>", string, flags=re.MULTILINE)

    # Paragrafos
    string = re.sub(r"^([a-zA-Z0-9].+)$", r"<p>\1</p>", string, flags=re.MULTILINE)

    return string


def main():
    html = ""
    # se tiver argumento de input, usa esse input
    if len(sys.argv) > 1:
        html = convert_to_html(sys.argv[1])

    else:
        html = convert_to_html(markdown_example)

    print(html)

    # mete a string convertida num ficheiro .html
    with open("output.html", "w") as file:
        file.write(html)

    # abre o ficheiro no browser
    webbrowser.open("output.html")


main()
