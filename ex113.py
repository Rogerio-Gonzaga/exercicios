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

def leiareal(msg):
    while True:
        try:
            n2=float(input(msg))
        except Exception as erro:
            print('\033[0;31mERRO!!! Digite um numero valido!\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mNumero não digitado\033[m')
            return 0
        else:
            break
    return n2


inteiro=leiaint('Digite um numero inteiro: ')
real=leiareal('Digite um numero real: ')
print(f'Os valores digitados foram {inteiro} e {real}')