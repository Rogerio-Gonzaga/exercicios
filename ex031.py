km=float(input('Digite a distancia que irá percorrer: '))
if km<=200:
    print('O Valor a se pagar pela passagem é R${:.2f}!'.format(km*0.50))
else:
    print('O valor a se pagar pela passagem é R${:.2f}!'.format(km*0.45))
