# Leitura e Escrita de Arquivos

def main():
    #Abrir um arquivo para escrever nele, caso não exista
    # o arquivo será criado
    #Write
    # arquivo = open("texto.txt", "w+")

    #Abrir um arquivo para adicionar texto
    #Append
    arquivo = open("Arquivos/texto.txt", "a+")

    pessoas = ["Ana", "Joao", "Bia", "Jose"]
    salarios = [5000, 2300, 6200, 9000]

    for i in range(4):
        arquivo.write("Nome: ")
        arquivo.write(pessoas[i])
        arquivo.write("\tSalario: ")
        arquivo.write(str(salarios[i]))
        arquivo.write("\n")

    #Fechar o arquivo quando finalizar as alteraçoes
    arquivo.close()

if __name__ == "__main__":
    main()