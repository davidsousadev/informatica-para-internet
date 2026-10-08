def situacao_aluno(nota):
    resultado = ""
    if type(nota) != int and type(nota) != float:
        resultado = "Tipo Invalido!"        
    elif nota < 0 or nota > 10:
        resultado = "Nota Invalida!"
    else:
        if nota >= 7 and nota <= 10: 
            resultado = "Aprovado"
        else:
            resultado = "Reprovado"
    return resultado

assert situacao_aluno(7) == "Aprovado"
assert situacao_aluno(10) == "Aprovado"
assert situacao_aluno(5) == "Reprovado"
assert situacao_aluno(-5) == "Nota Invalida!"
assert situacao_aluno("A") == "Tipo Invalido!"
assert situacao_aluno(None) == "Tipo Invalido!"
assert situacao_aluno([]) == "Tipo Invalido!"