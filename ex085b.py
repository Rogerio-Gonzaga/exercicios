lista=[[],[]]
dados=0
for c in range (0,7):
    dados=int(input(f'Digite um numero para posição {c+1}º: '))
    if dados %2 ==0:
        lista[0].append(dados)
    else:
        lista[1].append(dados)
print(lista)
#lista[0].sort()
#lista[1].sort()
print(f'Os numeros pares são {sorted(lista[0])} e os impares são {sorted(lista[1])}')