def calcular_imc(peso, altura):
    return peso / (altura * altura)

def classificar_imc(imc):
    if imc < 18.5:
        print(imc)
        return "Abaixo do peso"
    elif imc < 25:
        print(imc)
        return "Peso normal"
    elif imc < 30:
        print(imc)
        return "Sobrepeso"
    elif imc < 35:
        print(imc)
        return "Obesidade grau I"
    elif imc < 40:
        print(imc)
        return "Obesidade grau II"
    else:
        print(imc)
        return "Obesidade grau III"


# Testes de integração

assert classificar_imc(calcular_imc(40, 1.52)) == "Abaixo do peso"
assert classificar_imc(calcular_imc(65.8, 1.63)) == "Peso normal"
assert classificar_imc(calcular_imc(78.4, 1.64)) == "Sobrepeso"
assert classificar_imc(calcular_imc(111.61, 1.89)) == "Obesidade grau I"
assert classificar_imc(calcular_imc(108.5, 1.72)) == "Obesidade grau II"
assert classificar_imc(calcular_imc(125.4, 1.68)) == "Obesidade grau III"
assert classificar_imc(calcular_imc(65, 1.77)) == "Peso normal"
assert classificar_imc(calcular_imc(84.7, 1.624)) == "Obesidade grau I"
assert classificar_imc(calcular_imc(99.2, 1.92)) == "Sobrepeso"
assert classificar_imc(calcular_imc(115.72, 1.66)) == "Obesidade grau III"

print("Passou em todos os testes!")