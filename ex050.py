s = 0
co=0
for c in range(0,6):
    n=int(input('Digite um numero: '))
    n1 = n//2
    n2 = n%2
    if n2 == 0:
        #print(n)
        s=s+n
        co=co+1
print('A Soma de todos os {} numeros pares que voce digitou fica no valor de {}'.format(co,s))

