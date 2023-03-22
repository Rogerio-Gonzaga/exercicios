from random import randint
n=randint(1,10)
tentativa=0
print(n)
nu=0
while n != nu:
    nu=int(input('Me diga um numero de 1 à 10: '))
    if nu !=n:
        tentativa=tentativa+1
print('Acertou e chutou {} vezes antes de acertar'.format(tentativa))
# while not acertou:
# acertou = False
# acertou = True


