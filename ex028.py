import random
#utilizar mais a função from random import randint
from time import sleep
n=random.randint(1,6)

nu=int(input('Digite um numero de 1 à 6: '))
print('PROCESSANDO........')
sleep(2)
print('Pensei no numero {} e voce falou {}'.format(n , nu))
if n==nu:
    print('Acertou miseravi!!!')
else:
    print('EROUUUUU!')
