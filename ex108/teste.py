from ex108 import moedaa

p= int(input('Digite um preço R$: '))
print(f'O Dobro de {moedaa.moeda(p)} é {moedaa.moeda(moedaa.dobro(p))}')
print(f'A metade de {moedaa.moeda(p)} é {moedaa.moeda(moedaa.metade(p))}')
print(f'{moedaa.moeda(p)} mais 10% é {moedaa.moeda(moedaa.aumentar(p, 10))}')
print(f'{moedaa.moeda(p)} menos 13% é {moedaa.moeda(moedaa.diminuir(p, 13))}')