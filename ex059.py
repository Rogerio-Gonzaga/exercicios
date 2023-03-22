opcao=0
while opcao != 5:
    n1=int(input('Digite um numero: '))
    n2=int(input('Digite outro numero: '))
    print('Agora escola uma das opçoes abaixo:')
    print('OPÇÃO 1: SOMAR')
    print('OPÇÃO 2: MULTIPLICAR')
    print('OPÇÃO 3: MAIOR')
    print('OPÇÃO 4: NOVOS NUMEROS')
    print('OPÇÃO 5: SAIR')

    opcao=int(input('Escolha uma opção: '))
    if opcao == 1:
        r=n1+n2
        print('A soma dos numeros é' ,r)
    elif opcao == 2:
        r=n1*n2
        print(' A multiplicação dos numeros é' ,r)
    elif opcao ==3:
        if n1 > n2:
            print('o maior numero é' ,n1)
        elif n2 > n1:
            print('o maior numero é',n2)

print('FIM')
