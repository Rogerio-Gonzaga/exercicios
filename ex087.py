lista=[[],[],[]]
dados=0
par = impar = 0
soma3 = 0
for l in range(3):
    for c in range(3):
        dados=(int(input(f'Digite um numero para posição [{l},{c}]: ')))

        if dados %2 == 0:
            par=par+dados
        else:
            impar=impar+dados

        if l == 0:
            lista[0].append(dados)
        elif l == 1:
            lista[1].append(dados)
        elif l == 2:
            lista[2].append(dados)

for l in range(3):
    for c in range(3):
        print(f'[{lista[l][c]:^5}]',end='')
    print()

print(f'A soma dos valores impares é: {impar}')
print(f'A soma dos valores pares é: {par}')
print(f'A soma da terceira COLUNA é: {lista[0][2]+lista[1][2]+lista[2][2]}')
print(f'O Maior valor da 2 linha é {max(lista[1])}')


