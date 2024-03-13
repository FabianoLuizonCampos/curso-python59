# Módulo Principal da Calculadora
import func_matematica


def main():

    repeticao = True

    while repeticao == True:

        num1 = float(input("Digite o primeiro numero do calculo: "))
        num2 = float(input("Digite o segundo numero do calculo: "))
        
        operacao = input("Digite a operacao (+, -, /, *): ")

        if operacao == "+":
            resultado = func_matematica.soma(num1, num2)
            print("O resultado da operacao eh ", resultado)
        elif operacao == "-":
            resultado = func_matematica.subtracao(num1, num2)
            print("O resultado da operacao eh ", resultado)
        elif operacao == "/":
            resultado = func_matematica.divisao(num1, num2)
            print("O resultado da operacao eh ", resultado)
        elif operacao == "*":
            resultado = func_matematica.multiplicao(num1, num2)
            print("O resultado da operacao eh ", resultado)
        else:
            print("Voce digitou uma opcao invalida!!!")

        continuar = input("Deseja realizar novo calculo (S/N):")

        if continuar == "N":
            repeticao = False
        elif continuar == "S":
            repeticao = True
        else:
            print("Voce digitou uma opcao invalida, então vou repitir!!!")


if __name__ == "__main__":
    main()

