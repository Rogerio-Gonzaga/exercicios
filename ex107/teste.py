from ex107 import moedaa

p= int(input('Digite um preço R$: '))
print(f'O Dobro de {p:.2f} é {moedaa.dobro(p):.2f}')
print(f'A metade de {p:.2f} é {moedaa.metade(p):.2f}')
print(f'{p:.2f} mais 10% é {moedaa.aumentar(p, 10):.2f}')
print(f'{p:.2f} menos 13% é {moedaa.diminuir(p, 13):.2f}')