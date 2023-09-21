def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except Exception as erro:
            print('\033[0;31mERRO!!! Digite um numero valido!\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mNumero não digitado\033[m')
            return 0
        else:
            break
    return n

def linha(tam = 42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('Menu Pricipal')
    c=1
    for item in lista:
        print(f'\033[33m{c} \033[m- \033[34m{item}\033[m')
        c+=1
    print(linha())
    opc=leiaint('\033[32mSua Opção:\033[m ')
    return opc

