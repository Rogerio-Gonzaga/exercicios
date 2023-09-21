import heapq
lista=[]
n=0
for n in range(0,5):
    lista.append(int(input(f'Digite um numero para a posição {n}: ')))

print(f'Os valores digitados foram: {lista}')

menor=heapq.nsmallest(2,lista)
if menor[0] == menor[1]:
    print(f'O menor numero digitado foi o {min(lista)}, nas posicoes: ',end='')
    for pos, n in enumerate(lista):
        if n == min(lista):
            print(pos,end='...')
else:
    print(f'O menor numero digitado foi o {min(lista)}, na posicão: {lista.index(min(lista))}')
maior=heapq.nlargest(2,lista)
if maior[0] == maior[1]:
    print(f'\nO maior numero digitado foi o {max(lista)}, nas posicoes: ',end='')
    for pos2, n in enumerate(lista):
        if max(lista) == n:
            print(pos2,end='...')
else:
    print(f'O maior numero digitado foi o {max(lista)}, na posicão: {lista.index(max(lista))}')
