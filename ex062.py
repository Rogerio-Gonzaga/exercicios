a1= int(input('Qual o primeiro termo de sua P.A: '))
r= int(input('Qual a razão de sua P.A: '))
c=1
mais=10
total =0
while mais !=0:
    total=total+mais
    while c <= total:
        print(a1 , end='  ')
        a1 = a1 + r
        c=c+1
    mais=int(input('\nMais qts termos: '))

print('\nFIM')















