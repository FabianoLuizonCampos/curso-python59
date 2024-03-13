# GLOBAL
variavel_global = 5
variavel = 6

def func1():
    # LOCAL
    global variavel_global
    variavel = 1
    variavel_global = 6
    print("Func1: ", variavel)
    print("Func1: ", variavel_global)

def func2():
    # LOCAL
    variavel = 2
    print("Func2: ", variavel)
    print("Func2: ", variavel_global)


def main():
    # LOCAL
    variavel = 3
    print("Main: ", variavel)
    print("Main: ", variavel_global)

    func1()
    func2()

if __name__ == "__main__":
    main()