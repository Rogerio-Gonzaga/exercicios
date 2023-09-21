lista=[]
listapar=[]
listaimpar=[]
n=''
while True:
    num = int(input('Digite um numero: '))
    lista.append(num)
    opcao = str(input('Quer continuar: [S/N]? ')).upper().strip()
    if num %2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)
    if opcao == 'N':
        break
print(f'Os numeros digitados foram {lista}')
print(f'Os pares são {listapar}')
print(f'Os impares são {listaimpar}')