import ply.lex as lex

keywords = {
    "select": "SELECT",
    "from": "FROM",
    "where": "WHERE",
    "and": "AND",
    "or": "OR",
    "not": "NOT",
    "in": "IN",
    "as": "AS",
    "inner": "INNER",
    "outer": "OUTER",
    "left": "LEFT",
    "right": "RIGHT",
    "join": "JOIN",
    "on": "ON",
    "group": "GROUP",
    "by": "BY"
    # (...)
}

tokens = [
    "NUMBER",
    "OPERATOR",
    "FIELD",
    "COMMAND",
    "DELIMITER",
    "FINAL_DELIMITER",
    "ALL" # é o * do "SELECT *  "
    ] + list(keywords.values())


is_prev_SELECT = False # Variável para verificar se o * é precedido de SELECT ou não


def t_DELIMITER (t):
    r","
    global is_prev_SELECT
    is_prev_SELECT = False
    return t

def t_FINAL_DELIMITER (t): 
    r";"
    global is_prev_SELECT
    is_prev_SELECT = False
    return t    

def t_ALL(t):
    r"\*"
    global is_prev_SELECT
    if is_prev_SELECT: # Se o * for precedido de SELECT, é um comando SELECT ALL
        t.type = "ALL"
    else :
        t.type = "OPERATOR" # Se não, é um operador de multiplicação normal
    is_prev_SELECT = False
    return t

def t_NUMBER(t):
    r"\d+\.?\d*" # Matches any number (int or float)
    global is_prev_SELECT
    is_prev_SELECT = False
    if "." in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

def t_OPERATOR(t):
    r"[><=+\-]+" # Matches any math operator (o \- é para nao confundir com o intervalo de caracteres do regex tipo [a-z])
    global is_prev_SELECT
    is_prev_SELECT = False
    return t

def t_COMMAND(t):
    r"\w+(\.\w+)?" # Matches any word. a parte do (\.\w+)? é para dar match em palavras com pontos, como "u.nome" (usado em JOINs em SQL)
    global is_prev_SELECT
    is_prev_SELECT = False
    if t.value.lower() in keywords:
        t.type = keywords[t.value.lower()]
        if t.value.lower() == "select":
            is_prev_SELECT = True
    else:
        t.type = "FIELD"
    return t

def t_error(t):
    global is_prev_SELECT
    is_prev_SELECT = False
    print(f"Caractere ilegal: {t.value[0]}")
    t.lexer.skip(1)
    

t_ignore = " \t\n"

lexer = lex.lex()

def test_lexer(input):
    lexer.input(input)
    while True:
        token = lexer.token()
        if not token:
            break
        print(token)


print ("Teste 1:")
print("SELECT nome, idade FROM usuarios WHERE idade > 18;\n")
test_lexer("SELECT nome, idade FROM usuarios WHERE idade > 18;")


print ("\nTeste 2:")
print("SELECT * FROM table WHERE field = 10;\n")
test_lexer("SELECT * FROM table WHERE field = 10;")


print ("\nTeste 3:")
print("SELECT field1, field2 FROM table WHERE field1 = 10 AND field2 = 20;\n")
test_lexer("SELECT field1, field2 FROM table WHERE field1 = 10 AND field2 = 20;")


print ("\nTeste 4:")
print("SELECT u.nome, p.descricao \n FROM usuarios u \n INNER JOIN pedidos p ON u.id = p.usuario_id \n WHERE p.valor >= 100;\n")
test_lexer("SELECT u.nome, p.descricao \n FROM usuarios u \n INNER JOIN pedidos p ON u.id = p.usuario_id \n WHERE p.valor >= 100;")


print ("\nTeste 5:")
print("SELECT id, preco AS total \n FROM vendas \n WHERE preco >= 10 OR categoria = 5;\n")
test_lexer("SELECT id, preco AS total \n FROM vendas \n WHERE preco >= 10 OR categoria = 5;")
