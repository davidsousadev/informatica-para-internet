nota = float(input("Digite sua nota: "))

if nota <= 10 and nota >= 0:
    if nota == 10:
        print("Aprovado, parabéns!")
    elif nota >= 6 and nota < 10:
        print("Aprovado!")
    else:
        print("Reprovado!")
else:
    print("Nota invalida!")