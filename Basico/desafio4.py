# Crie um programa que verifique qual é a condição do aluno em 
# relação a sua promoção escolar
# nota >= 70    /   APROVADO
# nota >= 40 e nota < 70    / EXAME
# nota < 40     /   REPROVADO,
# frequencia > 75 / APROVADO ou EXAME

nota = int(input("Digite sua nota: "))
frequencia = int(input("Digite sua frequencia"))

if nota < 0 or nota > 100 or frequencia < 0 or frequencia > 100:
    print("Nota e/ou Frequencia Invalida!!!")
else:
    if nota >= 70 and frequencia >= 75:
        print("Aprovado!!!")
    elif nota >= 40 and nota < 70 and frequencia >= 75:
        print("Exame!!!")
    else:
        print("Reprovado!!!")
