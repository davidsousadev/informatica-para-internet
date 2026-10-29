"""
Questão 4 - Conversão de temperatura: Converta uma temperatura em graus Celsius para Fahrenheit e exiba o resultado. Utilize a fórmula F = (C × 9/5) + 32, em que C representa a temperatura em Celsius e F representa a temperatura em Fahrenheit.

"""

def conversor_c_f(c):
    if c == -300:
        f = "Temperatura invalida"
    elif type(c) == int or type == float:
        f = (c * 9/5) + 32 
    return f

assert conversor_c_f(37) == 98.6
print("Passou em todos os testes!")