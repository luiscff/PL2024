import datetime
import json
import re
import ply.lex as lex
import ply.yacc as yacc


class Produto:
    def __init__(self, codigo: str, nome: str, quantidade: int, preco: float):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        return f"{self.codigo.center(3)} | {self.nome.center(14)} | {str(self.quantidade).center(10)} | {str(self.preco).center(5)}"


class Vending_Machine:

    # LEXER

    tokens = ["LISTAR", "SELECIONAR", "MOEDA", "SAIR", "HELP"]

    def t_LISTAR(self, t):
        r"LISTAR"
        return t

    def t_SELECIONAR(self, t):
        r"SELECIONAR\s([A-Z]\d\d)"
        match = re.match(r"SELECIONAR ([A-Z]\d{2})", t.value)
        t.value = match.group(1)  # Guarda o código do produto na variável value
        return t

    def t_MOEDA(self, t):
        r"MOEDA\s((?:2e|1e|50c|20c|10c|5c|2c|1c),\s)*(?:2e|1e|50c|20c|10c|5c|2c|1c)\s\."
        # Aceita:
        # MOEDA 2e, 1e, 50c, 20c, 10c, 5c, 2c, 1c .
        # MOEDA 1e .
        lista = t.value[6:].split(", ")  # Guarda as moedas numa lista
        lista[-1] = lista[-1][:-2]  # Remove o ponto final
        t.value = lista  # Guarda a lista de moedas na variável value
        return t

    def t_SAIR(self, t):
        r"SAIR"
        return t

    def t_HELP(self, t):
        r"HELP"
        return t

    def t_error(self, t):
        print(f"Comando inválido, use o comando HELP para obter ajuda.")
        t.lexer.skip(len(t.value))

    t_ignore = " \t\n"

    # PARSER
    def p_listar(self, t):
        "command : LISTAR"
        print("Produtos disponíveis:")
        print("Cód |      Nome      | Quantidade | Preço")
        for produto in self.produtos:
            print(produto)

    def p_selecionar(self, p):
        "command : SELECIONAR"
        id = p[1]  # Código do produto está em p[1], que é o value do token SELECIONAR
        produto = self.buscar_produto(id)
        if produto == None: # produto inexistente
            print("Produto inexistente!")
            return
        if produto.quantidade == 0: # produto esgotado
            print("Produto esgotado!")
            return
        if self.saldo < produto.preco: # saldo insuficiente
            print("Saldo insufuciente para satisfazer o seu pedido")
            print("Saldo = " + self.pretty_print_string(self.saldo) + "; Pedido = " + self.pretty_print_string(produto.preco))
            return
        
        #compra efetuada
        self.saldo -= produto.preco 
        produto.quantidade -= 1
        print(f'Pode retirar o produto dispensado \"{produto.nome}\"')
        print("Saldo = " + self.pretty_print_string(self.saldo))

    def p_moeda(self, p):
        "command : MOEDA"
        # A lista de moedas está em p[2]
        lista = p[1]
        valor = 0.0
        for moeda in lista:
            if moeda[-1] == "e":
                valor += float(moeda[:-1])
            elif moeda[-1] == "c":
                valor += float(moeda[:-1]) / 100
            else:
                print("Erro GRAVE!")
                print(f"Moeda {moeda} não reconhecida!")
        self.saldo += valor
        print("Saldo = " + self.pretty_print_string(self.saldo))

    def p_sair(self, p):
        "command : SAIR"
        print(f"Pode retirar o troco: ")
        self.calcula_troco(self.saldo)
        self.save()
        self.exit = True

    def p_help(self, p):
        "command : HELP"
        print("Comandos disponíveis:")
        print("LISTAR - Lista os produtos disponíveis")
        print("SELECIONAR <ID> - Seleciona um produto pelo ID (ex: SELECIONAR A01)")
        print("MOEDA <moedas> - Insere moedas na máquina (ex: MOEDA 50c, 20c, 1c .)")
        print("SAIR - Termina a sessão e devolve o troco")

    def p_error(self, p):
        print("Erro de sintaxe!")

    def __init__(self):
        self.lexer = lex.lex(module=self)
        self.parser = yacc.yacc(module=self)
        self.produtos = []
        self.saldo = 0.0
        self.exit = False
        self.data = datetime.datetime.now().date()
        self.moedas = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

    def setup(self):
        self.load()
        if len(self.produtos) == 0:
            print(
                "Stock vazio! Insira produtos no ficheiro stock.json e reinicie a máquina."
            )
            self.exit = True
        else:
            print("Stock Carregado!")

    def run(self):
        print("Bem-vindo à Vending Machine!")
        print(self.data.strftime("%d/%m/%Y"))
        print("Digite HELP para obter ajuda.")
        while self.exit == False:
            comando = input(">>> ")
            self.lexer.input(comando)
            while True:
                token = self.lexer.token()
                if not token:
                    break
                else:
                    self.parser.parse(comando, lexer=self.lexer)
        print("Até à próxima!")

    def load(self):
        json_file = open("stock.json")
        json_data = json.load(json_file)
        for produto in json_data:
            self.produtos.append(
                Produto(
                    produto["cod"], produto["nome"], produto["quant"], produto["preco"]
                )
            )

    def save(self):
        with open("stock.json", "w") as json_file:
            json_object = []
            for produto in self.produtos:
                json_object.append(
                    {
                        "cod": produto.codigo,
                        "nome": produto.nome,
                        "quant": produto.quantidade,
                        "preco": produto.preco,
                    }
                )
            json.dump(json_object, json_file, indent=4, ensure_ascii=False)
        print("Stock atualizado")


    def buscar_produto(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto
        return None

    def print_troco(self, troco):
        troco_string = ""
        for i in range(len(self.moedas)):
            if troco[i] > 0:
                if self.moedas[i] >= 1:
                    troco_string += f"{troco[i]}x {self.moedas[i]}e, "
                else:
                    troco_string += f"{troco[i]}x {int(self.moedas[i] * 100)}c, "

        # Remove a última vírgula e espaço e adiciona um ponto final
        if len(troco_string) > 0:
            troco_string = troco_string[:-2] + "."
        else:
            troco_string = "Sem troco."
        # Substitui a última vírgula por um "e" se houver mais do que uma moeda
        if troco_string.count(",") > 1:
            troco_string = troco_string[::-1].replace(",", "e ", 1)[::-1]
        print(troco_string)

    def calcula_troco(self, valor: float):  # guarda o troco na lista troco
        troco = [0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(len(self.moedas)):
            while valor >= self.moedas[i]:
                troco[i] += 1
                valor -= self.moedas[i]
        self.print_troco(troco)

    def pretty_print_string(self, valor: float) -> str:
        valor_string = ""
        valor_formatado = "{:.2f}".format(valor)
        if valor >= 1:
            centimos = str(valor_formatado).split(".")[1]
            euros = str(valor_formatado).split(".")[0]
            valor_string += euros + "e" + centimos + "c"
        else:
            centimos = str(valor_formatado).split(".")[1]
            valor_string += centimos + "c"
        return valor_string


def main():
    maquina = Vending_Machine()
    maquina.setup()

    print("Bem-vindo à Vending Machine!")
    print("Digite HELP para obter ajuda.")
    while maquina.exit == False:
        comando = input(">>> ")
        maquina.lexer.input(comando)
        while True:
            token = maquina.lexer.token()
            if not token:
                break
            else:
                maquina.parser.parse(token)


if __name__ == "__main__":
    maquina = Vending_Machine()
    maquina.setup()
    maquina.run()
