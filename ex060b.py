n = int(input('Digite um numero: '))
c=1
t=n
while c ==1:
    if t > 1:
        t=t-1
        print('{}*{} = {}'.format(n, t, (n * t)))
        n = n * t

    else:
        break
