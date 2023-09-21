from time import sleep
from random import randint
from operator import itemgetter
dados = {'Jogador1': randint(1,6),
         'Jogador2': randint(1,6),
         'Jogador3': randint(1,6),
         'Jogador4': randint(1,6)}
ranking=[]
print('Valores sorteados!!!')
for k, v in dados.items():
    sleep(1)
    print(f'{k} tirou {v}')

ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
#print(ranking)
for c, l in enumerate(ranking):
    sleep(1)
    print(f'{c+1}º Lugar, O {l[0]} tirou {l[1]}')