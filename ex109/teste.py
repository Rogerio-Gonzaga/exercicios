from ex109 import moedaa

p= float(input('Digite um preço R$: '))
print(f'O Dobro de {moedaa.moeda(p)} é {moedaa.dobro(p, True)}')
print(f'A metade de {moedaa.moeda(p)} é {moedaa.moeda(moedaa.metade(p))}')
print(f'{moedaa.moeda(p)} mais 10% é {moedaa.aumentar(p, 10, True)}')
print(f'{moedaa.moeda(p)} menos 13% é {moedaa.moeda(moedaa.diminuir(p, 13))}')

# conforme formato nos print 1 e 3