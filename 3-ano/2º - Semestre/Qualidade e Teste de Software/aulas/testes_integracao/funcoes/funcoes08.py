def calcular_imc(peso, altura):
    # Escreva seu código aqui
    pass

def classificar_imc(imc):
    # Escreva seu código aqui
    pass

# Testes de integração

assert classificar_imc(calcular_imc(____, 1.52)) == "Abaixo do peso"
assert classificar_imc(calcular_imc(65.8, ____)) == "Peso normal"
assert classificar_imc(calcular_imc(78.4, 1.64)) == "__________"
assert classificar_imc(calcular_imc(____, 1.89)) == "Obesidade grau I"  # IMC: 31.25
assert classificar_imc(calcular_imc(108.5, ____)) == "Obesidade grau II"  # IMC: 36.68
assert classificar_imc(calcular_imc(125.4, 1.68)) == "__________"
assert classificar_imc(calcular_imc(____, 1.77)) == "Peso normal"
assert classificar_imc(calcular_imc(84.7, ____)) == "Obesidade grau I"  # IMC: 32.12
assert classificar_imc(calcular_imc(99.2, 1.92)) == "__________"
assert classificar_imc(calcular_imc(____, 1.66)) == "Obesidade grau III"  # IMC: 42.00

print("Passou em todos os testes!")

