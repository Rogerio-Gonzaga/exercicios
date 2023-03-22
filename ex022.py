nome=input('Me diga seu nome completo:').strip()
print('Seu nome em maiusculo é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
nome2 = ''.join(nome.split())
len(nome2)
print('Seu nome tem o total de letras {}' .format(len(nome2)))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
#subtração de string menos os espaços
pname=(nome.split()[0])
print('O primeiro nome tem o total de letras {}' .format(len(pname)))
print('O primeiro nome tem o total de {} letras'.format(nome.find(' ')))
#nesse exemplo vimos onde esta o primeiro espaço, que separa o primeiro nome e fala quantas letras tem
