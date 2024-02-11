"""
    Faz o parsing de uma linha em que os campos estão separados por vírgulas

    Parâmetros:
    linha (str): string que corresponde a uma linha do dataset  

    Retorna:
    tuplo: um tuplo que contem 3 strings que são os parâmetros "modalidade", "resultado" e "idade", 
"""


def parseLine(linha: str):
    tokens = linha.strip().split(",")
    return tokens[8], tokens[-1], tokens[5]


# _id,index,dataEMD,nome/primeiro,nome/último,idade,género,morada,modalidade,clube,email,federado,resultado


def main():
    modalidades = set()
    num_aptos = 0
    num_inaptos = 0
    idades = {"[20-24]": 0, "[25-29]": 0, "[30-34]": 0, "[35-39]": 0, "outros": 0}
    with open("emd.csv", "r") as f:
        next(f)
        linhas = f.readlines()
        for linha in linhas:
            modalidade, apto, idade_str = parseLine(linha)
            modalidades.add(modalidade)
            if apto == "true":
                num_aptos += 1
            else:
                num_inaptos += 1
            idade = int(idade_str)
            if 20 <= idade <= 24:
                idades["[20-24]"] += 1
            elif 25 <= idade <= 29:
                idades["[25-29]"] += 1
            elif 30 <= idade <= 34:
                idades["[30-34]"] += 1
            elif 35 <= idade <= 39:
                idades["[35-39]"] += 1
            else:
                idades["outros"] += 1
    mod_ordenadas = sorted(modalidades)
    num_total = num_aptos + num_inaptos
    percentagem_aptos = num_aptos / num_total * 100
    percentagem_inaptos = num_inaptos / num_total * 100
    print("modalidades: ", mod_ordenadas)
    print("percentagem de atletas aptos para desporto: ", percentagem_aptos, "%")
    print("percentagem de atletas inaptos para desporto: ", percentagem_inaptos, "%")
    print("Distribuição de atletas por faixa etária: ", idades)


if __name__ == "__main__":
    main()
