# OS - Operating System ou Sistema Operacional
# Pastas (Diretórios)
#  - Locais (Caminhos / Path)
import os
import datetime
from datetime import date

def main():
    # diretorio = "c:/Temp"
    # arquivos =  os.listdir(diretorio)

    # for arquivo in arquivos:
    #     print(arquivo)

    # novo_diretorio = "/SENAI"
    # os.makedirs(novo_diretorio)

    data_hoje = str(date.today())
    novo_diretorio = "/SENAI/" + data_hoje
    #novo_diretorio = "/SENAI/2024-02-16"
    #print(novo_diretorio)
    os.makedirs(novo_diretori-o)
-
if __name__ == "__main__":
    main()