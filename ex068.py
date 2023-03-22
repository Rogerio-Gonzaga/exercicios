import random
n=0
c=0
P= 'PAR'
I= 'IMPAR'
while True:
    n=int(input('Digite um numero: '))
    player=str(input('Agora escolha Impar ou Par [I/P]: ')).upper().strip()[0]
    pc=random.randint(1,10)
    print('coloco', pc)

    if (n+pc) %2==0:
        print(f'{n}+{pc} = {n+pc} -> PAR')

        if (n+pc) %2==0 and player == 'P':
            print('Ganhou!')
            c = c + 1
        if player == 'I':
            print('Perdeu!')
            break
    else:
        print(f'{n}+{pc} = {n+pc} -> Impar')
        if player == 'I':
            print('Ganhou!')
            c = c + 1
        else:
            print('Perdeu!')
            break
print(f'Voce Ganhou {c} vezes!!!')