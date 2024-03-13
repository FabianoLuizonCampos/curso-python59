# Biblioteca de funções matemáticas para cálculo
# -----> def nome(argumentos):
# Argumentos é as informações que é necessárias para a função 
# executar suas tarefas
# return é a resposta ou resultado das tarefas da função

def soma(num1, num2):
    res = num1 + num2
    return res

def subtracao(num1, num2):
    res = num1 - num2
    return res

def multiplicao(num1, num2):
    res = num1 * num2
    return res

def divisao(num1, num2):
    try:
        res = num1 / num2        
    except ZeroDivisionError:
        print("Erro: Nao eh possivel fazer divisao por zero!!")
    else:
        return res