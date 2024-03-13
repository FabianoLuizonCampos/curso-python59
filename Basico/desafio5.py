# Peça ao usuário para inserir um nome de usuário e uma senha. 
# Verifique se o nome de usuário é "admin" e a senha é "admin123". 
# Exiba uma mensagem de boas-vindas se as credenciais estiverem 
# corretas, caso contrário, exiba uma mensagem de erro.

# LOGIN_ADMIN = "admin"
# SENHA_ADMIN = "admin123"

# login = input("Digite seu login: ")
# senha = input("Digite sua senha: ")

# if login == LOGIN_ADMIN and senha == SENHA_ADMIN:
#     print("Seja bem vindo administrador")
# else:
#     print("Erro de login/senha")

LOGIN_ADMIN = "admin"
SENHA_ADMIN = "admin123"

def isAdmin(login, senha):
    if login == LOGIN_ADMIN and senha == SENHA_ADMIN:
        return True
    else:
        return False

def main():
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    verifica = isAdmin(login, senha)
    if verifica == True:
        print("Ola Admin, seja bem vindo")
    else:
        print("Erro")


if __name__ == "__main__":
    main()