# TPC3

**Título:** Somador On/Off

**Autor:** Luís Carlos Fragoso Figueiredo, a100549

1. **Descrição:**
Este programa em Python realiza a soma de todas as sequências de dígitos encontradas em um texto, com a capacidade de ligar e desligar esse comportamento conforme a presença das strings "On" e "Off". Sempre que encontrar o caractere "=", o resultado da soma é exibido na saída.


2. **Funcionamento do programa:**
O programa começa por ler a entrada do stdin e inicializa duas variáveis: `somador`, que indica se o somador está ativado ou desativado (inicialmente está desativado por default), e `soma`, que armazena o resultado acumulado das somas das sequências de dígitos.

Em seguida, o programa itera sobre cada parte da entrada usando expressões regulares para encontrar as strings "On", "Off", "=", e sequências de dígitos. Ao encontrar "On", ativa o somador; ao encontrar "Off", desativa o mesmo. Se encontrar uma sequência de dígitos e o somador estiver ativado, adiciona o valor da sequência à variável `soma`, senão ignora. Se encontrar "=", o programa imprime o valor da soma desde a última ocorrência de "=", e zera o valor da variável `soma`. O programa faz isto até o fim da entrada.


3. **Instruções de Uso:**
Execute o programa Python fornecendo uma string no STDIN. Por exemplo:
```
echo "On 123 Off = 456" | python3 somador_on_off.py
```
ou 
```
python3 main.py < teste1.txt
```