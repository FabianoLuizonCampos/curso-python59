peso = int(input("Digite seu peso:"))
altura = float(input("Digite sua altura:"))

#Expressao
#imc = peso / (altura * altura)
imc = peso / (altura ** 2)

print("O valor do IMC eh: ", imc)

#print("O nome do modulo eh ", __name__)