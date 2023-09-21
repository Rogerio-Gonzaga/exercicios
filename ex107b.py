import moeda

numero=int(input('Digite um numero: '))
print(f'A metade de {numero} é {moeda.metade(numero)}')
print(f'O dobro de {numero} é {moeda.dobro(numero)}')
print(f'{numero} mais 10% é igual {moeda.aumentar(numero,10)}')
print(f'{numero} menos 13% é igual {moeda.diminuir(numero,13)}')