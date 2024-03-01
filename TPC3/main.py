import re
import sys

# Resultado esperado do teste1.txt: 0 257 132 188 0 58 9 12 0 0 0 0 14 43  
# Resultado esperado do teste2.txt: 30
# Resultado esperado do teste3.txt: 369 0 369 0


def somador_on_off():
    test_string = sys.stdin.read()
    somador = False
    soma = 0
    for i in re.findall(r"on|off|=|\d+", test_string, flags=re.IGNORECASE):
        if i.lower() == "on":
            somador = True
        elif i.lower() == "off":
            somador = False
        elif i.isdigit() and somador:
            soma += int(i)
        elif i == "=":
            print(soma)
            soma = 0


somador_on_off()