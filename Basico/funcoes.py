#Funcao Básica - Não tem argumento e não tem retorno
def saudacao():
    print("Ola, seja bem vindo!!!")

#Funcao Argumento
def saudacaoPersonalizada(nome):
    print("Ola ", nome, " seja bem vindo(a)!!" )

#Funcao com Retorno de Valor
def elevadoCubo(num):
    cubo = num * num * num
    return cubo

#Funcao com Valor Padrao de Argumento
def potencia(base, exponte = 2):
    resultado = base ** exponte
    return resultado
    
#Funcao Principal - main()
def main():
    #Chamando a funcao basica
    saudacao()
    #Chamando a funcao com argumento
    saudacaoPersonalizada("SENAI")
    #Chamando a funcao com argumento
    saudacaoPersonalizada("Jairo Candido")
    #Chamando a funcao com retorno de valor
    valor_cubo = elevadoCubo(2) 
    print("Dois elevado ao cubo", valor_cubo)
    print("Tres elevado ao cubo", elevadoCubo(3))
    #Chamando a funcao com valor padrao de argumento
    res1 = potencia(2, 3)
    print("A potencia 1: ", res1)
    res2 = potencia(2)
    print("A potencia 2: ", res2)

#Condicao de Executar Primeiro a funcao main()
if __name__ == "__main__":
    main()