def leiaint(msg):
    while True:
        n=str(input(msg))
        if n.isnumeric():
            type(n)
            if n is int():
                break
            break
        else:
            print('Digite um numero inteiro')

    return n

n=leiaint('Digite um numero:')
print(f'Voce acabou de digitar o numero: {n} ')