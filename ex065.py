r= 'S'
c=0
s=0
maior=0
menor= 0
while r == 'S':
    n=int(input('Digite um valor: '))
    r=str(input('Quer continuar? [S/N] ')).upper().strip()
    c=c+1
    s=n+s
    if c == 1:
        maior = n
        menor = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n

print('foram digitados {} numeros e a media deles é {:.2f}'.format(c,(s/c)))
print('maior digitado {} e menor digitado {}'.format(maior,menor))