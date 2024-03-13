class Carro:
    
    # Caractericas 
    ano = 0

    # Função Construtora: toda vez que o objeto for criado, ela é executada
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # Funcionalidades
    def imprimirDados(self):
        print("A marca do meu carro eh ", self.marca, " e o modelo eh ", self.modelo)
