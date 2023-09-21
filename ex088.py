from random import randint
from time import sleep
lista=[]
tot=1
listafinal=[]

n=int(input('Quantos jogos voce quer? '))
print('SORTEANDO NUMEROS')
while tot <= n:
    cont = 0
    tot=tot+1
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont = cont + 1
        if cont >= 6:
            break
    lista.sort()
    listafinal.append(lista[:])
    lista.clear()
#print(listafinal)
for i, seq in enumerate(listafinal):
    sleep(1)
    print(f'Na posição {i+1}º temos o jogo {seq}')

