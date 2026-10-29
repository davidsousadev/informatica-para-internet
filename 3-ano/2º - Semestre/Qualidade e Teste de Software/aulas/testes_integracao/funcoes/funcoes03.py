"""Questão 3 - Maior entre dois números: Considere dois números inteiros diferentes, identifique o maior valor e apresente-o na tela."""



def maior_inteiro(a, b):
    maior = None
    if ((type(a) == int and type(b) == int)):
        if a == b: 
            maior = a
        elif a > b:
            maior = a
        else:
            maior = b
    else:
        maior = "Valores diferentes de inteiro!"
    return maior

assert maior_inteiro(0, 0) == 0
assert maior_inteiro(5.5, 3.2) == "Valores diferentes de inteiro!"
assert maior_inteiro(3526142, 1.0) == "Valores diferentes de inteiro!"
assert maior_inteiro(True, False) == "Valores diferentes de inteiro!"
print("Passou em todos os testes!")