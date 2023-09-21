lista=[]
n=0
for n in range(0,5):
    lista.append(int(input(f'Digite um numero para a posição {n}: ')))

print(f'Os valores digitados foram: {lista}')
print(f'O maior valor digitado foi {max(lista)}, nas posiçoes: ',end='')
for pos, lmax in enumerate (lista):
    if max(lista) == lmax:
        print(pos, end='...')
print(f'\nO menor valor digitado foi {min(lista)}, nas posiçoes: ',end='')
for pos2, lmin in enumerate (lista):
    if lmin == min(lista):
        print(pos2, end='...')
#Guanabara comecou com 'x'=maior e menor da lista e usou if > e < para saber se o numero era o meior e menor da lista
