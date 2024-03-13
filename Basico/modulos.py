PI = 3.14159

#Funcao Basica
def saudadoesSenai():
    print("Ola novo aluno, seja bem vindo")

def saudadacao():
    print("Ola")

#Funcao com Argumento e Retorno de Valor
def calculaAreaCirculo(raio):
    area_circulo = PI * (raio ** 2)
    return area_circulo

#Funcao Main - Principal
def main():
    r = float(input("Digite o raio do circulo:"))
    area = calculaAreaCirculo(r)
    print("A area eh ", area)


if __name__ == "__main__":
    main()
    



