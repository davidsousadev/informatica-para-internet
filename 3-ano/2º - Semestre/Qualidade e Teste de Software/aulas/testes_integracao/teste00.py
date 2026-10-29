


def somar(num1, num2):
    if(type(num1) == int or type(num1 == float) and (type(num2) == int) or type(num2) == float):
        return num1 + num2
    
def calcular_media(nota1, nota2):
    return somar(nota1, nota2) / 2

# Teste Unitário
assert somar(1.2, 3) == 4.2
assert somar(2, 3.2) == 5.2
print("Testes de unitário realizado com sucesso!")

# Teste de integração
assert calcular_media(8, 6) == 7
assert calcular_media(5, 5) == 5
print("Testes de integração realizado com sucesso!")