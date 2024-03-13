# Peça ao usuário para inserir um valor em reais e, 
# em seguida, converta esse valor para dólares 
# utilizando uma taxa de câmbio predefinida.
# Taxa de cambio - 1 dólar = 4.96 reais


TAXA_CAMBIO = 4.96

real = float(input("Digite o valor em reais para conveter em dolar:"))

#Calculo da conversão de real para dolar
dolar = real / TAXA_CAMBIO
#Arredondamento do valor em dolar para 2 casas decimais
dolar_arredondado = round(dolar, 2)

print("O valor convertido eh: ", dolar_arredondado)