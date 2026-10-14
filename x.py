def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

# Teste unitário
resultado = calcular_media(8, 6)
if resultado == 7:
    print("Teste aprovado!")
else:
    print("Teste falhou!")
print("Média:", resultado)