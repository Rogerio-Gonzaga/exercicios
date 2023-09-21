lista=[[],[],[]]
dados=0
for l in range(3):
    for c in range(3):
        dados=(int(input(f'Digite um numero para posição [{l},{c}]: ')))
        if l == 0:
            lista[0].append(dados)
        elif l == 1:
            lista[1].append(dados)
        elif l == 2:
            lista[2].append(dados)
print(f'[{lista[0][0]:^5}] [{lista[0][1]:^5}] [{lista[0][2]:^5}]')
print(f'[{lista[1][0]:^5}] [{lista[1][1]:^5}] [{lista[1][2]:^5}]')
print(f'[{lista[2][0]:^5}] [{lista[2][1]:^5}] [{lista[2][2]:^5}]')