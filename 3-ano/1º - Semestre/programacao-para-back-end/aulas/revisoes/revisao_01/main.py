"""
    Crie uma calculadora usando if, elif, else e módulos.
"""

from operacoes import somar

numero1 = int(input("Digite o 1º numero: "))
numero2 = int(input("Digite o 2º numero: "))

operacao = input("Qual a operação: +, -, * ou / ").strip()

print("Resultado: ")
if operacao == "+":
    print(somar(numero1, numero2))
