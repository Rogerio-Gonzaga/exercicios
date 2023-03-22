n=1
c=0

while n > 0:
    n = int(input('Digite um numero para ver sua tabuada: '))
    if n < 1:
        print('Programa encerrado!')
        break
    for c in range (0,10):
        c=c+1
        print(f'{n}x{c} = {n * c}')

