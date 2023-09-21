lista=[]
listapar=[]
listaimpar=[]

while True:
    num = int(input('Digite um numero: '))
    lista.append(num)
    opcao = str(input('Quer continuar: [S/N]? ')).upper().strip()
    if opcao == 'N':
        break

for item in range (0,len(lista)):

    if lista[item] %2 ==0:
        listapar.append(lista[item])
#usou elif lista[item] %2 ==1:
    else:
        listaimpar.append(lista[item])

print(f'Os numeros digitados foram {lista}')
print(f'Os pares são {listapar}')
print(f'Os impares são {listaimpar}')
