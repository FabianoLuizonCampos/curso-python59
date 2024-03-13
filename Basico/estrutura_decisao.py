# As estruturas de decisão ou condicionais em Python 
#são usadas para tomar decisões com base em condições. 

# if

idade = int(input("Digite sua idade: "))

# if idade < 18:
#     print("Voce deve aguardar ate as 12h para ir embora!!")
# else:
#     if idade >= 18 and idade < 30:
#         print("Seu horario eh as 11h45")
#     else:
#         print("Voce esta livre")

if idade < 18:
    print("Voce deve aguardar ate as 12h para ir embora!!")
elif idade >= 18 and idade < 30:
    print("Seu horario eh as 11h45")
elif idade >= 30 and idade < 40:
    print("Seu horario eh as 11h00")
else:
    print("Voce esta livre")