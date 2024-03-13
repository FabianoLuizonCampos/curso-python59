# Peça ao usuário para inserir um nome de usuário e uma senha. 
# Verifique se o nome de usuário é "admin" e a senha é "admin123". 
# Exiba uma mensagem de boas-vindas se as credenciais estiverem 
# corretas, caso contrário, exiba uma mensagem de erro.
LOGIN_ADMIN = "admin"
SENHA_ADMIN = "admin123"

def isAdmin(login, senha):
    if login == LOGIN_ADMIN and senha == SENHA_ADMIN:
        return True
    else:
        return False
    
def imprimeLogin(verifica):
    if verifica:
        print("Ola Admin, seja bem vindo")
    else:
        print("Erro")

def main():
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    imprimeLogin(isAdmin(login,senha))


if __name__ == "__main__":
    main()