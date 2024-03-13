import os
from tkinter.filedialog import askdirectory


def main():
    # Local da minha pasta
    caminho = askdirectory(title="Selecione uma pasta")
    print(caminho)
    # Listar os arquivos da minha pasta
    lista_arquivos = os.listdir(caminho)
    print(lista_arquivos)

    locais = {
        "documentos": [".docx", ".doc"],
        "planilhas": [".xlsx"],
        "pdfs": [".pdf"], 
    }

    for arquivo in lista_arquivos:

        nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")

        for pasta in locais:
            if extensao in locais[pasta]:
                if not os.path.exists(f"{caminho}/{pasta}"):
                    os.mkdir(f"{caminho}/{pasta}")
                os.rename( 
                            f"{caminho}/{arquivo}", 
                            f"{caminho}/{pasta}/{arquivo}"
                        )





if __name__ == "__main__":
    main()