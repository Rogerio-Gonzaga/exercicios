ordem=(int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite mais um numero: ')),
       int(input('Digite o ultimo numero: ')))
print('Voce digitou os numeros:' ,ordem)
print(f'O numero 9 apareceu {ordem.count(9)} vezes')
if 3 in ordem:
    print(f'O numero 3 foi digitado na posição {ordem.index(3)+1}º')
else:
    print('O numero 3 não foi digitado!')
print('Os numero pares são: ',end=' ')
for par in ordem:
    if par %2==0:
        print(par, end=' ')