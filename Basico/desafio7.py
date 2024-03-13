# Faça um programa que leia 5 números e informe o maior número.

# lista vazia
numeros = []

# captura dos numeros utilizando o for e acrescentando na lista
# atraves do metodo append
for i in range(5):
    num = int(input("Numero: "))
    numeros.append(num)

#impressao na tela para vericar tudo ok
print(numeros)

#Solucao 1
# maior = 0

# for num in numeros:
#     if maior < num
#         maior = num

#Solucao 2
maior = max(numeros)


print(maior)
