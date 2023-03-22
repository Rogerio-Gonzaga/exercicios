import random
tiro1 = str(input('Escolha entre Pedra, Papel e Tesoura: '))
#itens = ('Pedra' , 'Papel' , 'Tesoura')
#computador = random.randint(0, 2)
#print('O PC escolheu {}'.format(itens[computador]))
#a forma colocada no exercicio é mais pratica no random, porem no if/else minha formula ficou melhor.
Pedra = str
Papel = str
Tesoura = str
lista = ['Pedra', 'Papel', 'Tesoura']
lista2 = random.choice(lista)
print(lista2)
if tiro1 == 'Pedra' and lista2 == 'Tesoura':
    print('Pedra ganha de Tesoura! Voce Ganhou!')
elif tiro1 == 'Papel' and lista2 == 'Pedra':
    print('Papel ganha de Pedra! Voce ganhou')
elif tiro1 == 'Tesoura' and lista2 == 'Papel':
    print('Tesoura ganha de papel! Voce ganhou')
elif tiro1 == lista2:
    print(' {} e {} empatam!'.format(lista2, tiro1))
else:
    print('{} ganha de {}! Ganhei'.format(lista2, tiro1))


