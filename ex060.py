n=int(input('Digite um numero: '))
for c in range(n-1,0,-1):
    print('{}*{} = {}'.format(n, c, (n * c)))
    n = n * c


