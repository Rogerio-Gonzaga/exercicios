ordem=''
nf=0
n1=int(input('Digite um numero: '))
n2=int(input('Digite outro numero: '))
n3=int(input('Digite mais um numero: '))
n4=int(input('Agora um ultimo numero: '))
ordem=n1,n2,n3,n4
print('Voce digitou os numeros:', ordem)
print('O numero 9 apareceu {} vezes'.format(ordem.count(9)))
if 3 in ordem:
    print('O valor 3 apareceu a {}º posição'.format(ordem.index(3)+1))
else:
    print('O valor 3 não foi digitado')
for c in ordem:
    if c %2 ==0:
        nf=nf+1

print(f'Quantidade de numeros pares é {nf}')