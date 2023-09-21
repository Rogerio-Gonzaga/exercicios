lista=[]
listagem=[]
from random import randint
from time import sleep
print('Valores sorteados:')

for c in range (1,5):
    sleep(1)
    n = randint(1, 6)
    print(f'Jogador {c} tirou {n}')
    listagem.append(c)
    listagem.append(n)
    lista.append(listagem[:])
    listagem.clear()
dados= dict(lista)
sleep(1)

#print(lista)
#print(dados)
print('Ranking dos jogadores:')

for i in sorted(dados, key=dados.get, reverse=True):
    sleep(1)
    print(f'O Jogador {i} tirou {dados[i]}')