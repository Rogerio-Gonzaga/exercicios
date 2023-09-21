lista=[]

while True:
#podendo-se usar -> lista.append(int(input('Digite um numero: ')))
    num=int(input('Digite um numero: '))
    lista.append(num)
    opcao = str(input('Quer continuar: [S/N]? ')).upper().strip()
#guanabara normalmente usa -> if opcao in 'Nn':
    if opcao == 'N':
        break
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} numeros')
print(f'Os valores digitados foram {lista} em ordem decrescente')
if 5 in lista:
    print(f'O Numero 5 aparece na lista na posição {lista.index(5)+1}º')
else:
    print('O numero 5 não aparece na lista!')


