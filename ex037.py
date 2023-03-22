n=int(input('Digite um numero: '))
n1= format(n , 'b')
#print(n1) tambem pode ser usado bin() e eliminar as 2 primeiras casas com fatiamento [2:]
n2= format(n , 'o')
#print(n2) tbm pode ser usado oct() e eliminar as 2 primeiras casas com fatiamento [2:]
n3= format(n , 'x')
#print(n3) tbm pode ser usado hex() e eliminar as 2 primeiras casas com fatiamento [2:]
print('Voce escolheu o numero {} agora escolha uma opçao abaixo para conversao:'.format(n))
print('\033[0;31;40mOpção 1 - Binario\033[m - \033[0;33;40mOpção 2 - Octal\033[m - \033[0;36;40mOpção 3 - Hexadecimal\033[m')
opção=int(input('Escolha uma opção: '))
print('Voce escolheu a opção {}, segue abaixo sua conversao'.format(opção))
if opção == 1:
    print(n1)
elif opção == 2:
    print(n2)
elif opção == 3:
    print(n3)
else:
    print('Opção não disponivel')