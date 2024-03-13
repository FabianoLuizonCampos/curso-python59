import os
import PyPDF2
# pip install pypdf2

def main():
    
    merger = PyPDF2.PdfMerger()

    lista_arquivos = os.listdir("arquivos")
    lista_arquivos.sort()
    print(lista_arquivos)

    for arquivo in lista_arquivos:
        if ".pdf" in arquivo:
            merger.append(f"arquivos/{arquivo}")

    merger.write("PDF_Final.pdf")

if __name__ == "__main__":
    main()