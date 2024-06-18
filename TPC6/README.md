# TPC6
**Título:** Gramática Independente de Contexto

**Autor:** Luís Carlos Fragoso Figueiredo, a100549

## Resumo

Este trabalho consiste em fazer uma GIC (gramática independente de contexto) para representar expressões aritméticas e lógicas simples. A gramática é composta por terminais, não-terminais e regras de produção, que descrevem como as expressões podem ser formadas. 

### Expressaoessões exemplo

```
$ ?a
$ b=a*123/(4321-123)
$ !a+b
$ c=(a*b)/(a+b)
```

## Resolução

```
T = {'?', '!', '(', ')', '=', '/', '*', '-', '+', var, num}

N = {S, Exp1, Exp2, Exp3, Op, Op2}

S = S

P = {
    S -> '?' var                  LA = {'?'}
       | '!' Exp1                 LA = {'!'}
       | var '=' Exp1             LA = {var}

    Exp1 -> Exp2 Op

    Op -> '+' Exp1          LA = {'+'}
        | '-' Exp1          LA = {'-'}
        | &                 LA = {$, ')'}
    
    Exp2 -> Exp3 Op2        LA = {'(', var, num}

    Op2 -> '*' Exp1         LA = {'*'}
         | '/' Exp1         LA = {'/'}
         | &                LA = {'+', '-', $, ')'}

    Exp3 -> '(' Exp1 ')'               LA = {'('}
           | var                       LA = {var}
           | num                       LA = {num}
}
```
