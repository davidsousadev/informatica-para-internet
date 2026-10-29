





def impar_ou_par(a):
    if type(a) == int:
        if a % 2 == 0:
            a = True
        else: 
            a = False
    else:
        a = "Tipo de dado invalido!"
    return a

assert impar_ou_par(5) == False
assert impar_ou_par(False) == True
assert impar_ou_par([]) == "Tipo de dado invalido!"
print("Passou em todos os testes!")