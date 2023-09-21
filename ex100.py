from random import randint
from time import sleep
lista=[randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9)]
def sorteio(lista):
    print(f'Sorteando 5 valores para a lista: ',end='')
    for c in lista:
        sleep(0.3)
        print(c, end=' ')
    print('FIM')


def soma(lista):
    i=0
    print(f'Somando valores pares da lista {lista} temos: ', end=' ')
    for par in lista:
        if par %2 ==0:
            i=par+i
    print(i)


sorteio(lista)
soma(lista)
print('#'*70)
