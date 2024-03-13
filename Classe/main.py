import carro
from carro import *

def main():
    carro1 = Carro("Toyota", "Etios")
    carro2 = Carro("Fiat", "Uno")

    

    #print("Modelo do carro 1: ", carro1.modelo)
    carro1.imprimirDados()
    carro2.imprimirDados()

if __name__ == "__main__":
    main()