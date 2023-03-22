a1= int(input('Qual o primeiro termo de sua P.A: '))
r= int(input('Qual a razão de sua P.A: '))
c=1

while c < 11:
    print(a1, end='-')
    a1 = a1 + r
    c=c+1
print('FIM')
