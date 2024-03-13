#Variavel do tipo lista
lista_de_frutas = ["maçã", "banana", "laranja", "uva"]

#Variavel do tipo tupla
tupla_de_cores = ("vermelho", "azul", "verde", "amarelo")

#Variavel do tipo dicionario
dicionario_de_pessoas = {
    "nome": "Alice",
    "idade": 25,
    "cidade": "Mauá"
}

#Exibindo os valores das variaveis
print("Minha lista de frutas:", lista_de_frutas)
print("Tupla de cores:", tupla_de_cores)
print("Dicionario de pessoas:", dicionario_de_pessoas)

#Acessando elementos especificos
print("\nA segunda fruta da minha lista eh:", lista_de_frutas[1])

print("A cor verde esta na tupla", "verde" in tupla_de_cores)
print("A cor roxo esta na tupla", "roxo" in tupla_de_cores)
print("O segundo elemento da minha tupla eh:", tupla_de_cores[1])

print("A idade de", dicionario_de_pessoas["nome"], " eh ", 
      dicionario_de_pessoas["idade"])