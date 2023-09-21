lista=[]
dados=[]
opcao='S'
pmax=0
pmin=999
while opcao != 'N':
    nome=str(input('Nome: '))
    peso=int(input('Peso: '))
    opcao=str(input('Quer continuar? [S/N] ')).upper().strip()
    dados.append(nome)
    dados.append(peso)
    lista.append(dados[:])
    dados.clear()
print(f'Total de {len(lista)} pessoas cadastradas')
for p in lista:
    if p[1] >= 70:
        print(f'{p[0]} considerado pesado')

    else:
        print(f'{p[0]} considerado leve')
print(lista)
for pes in lista:
    if pes == 0:
        pmax=pes[1]
        pmin=pes[1]

    else:
        if pes[1] > pmax:
            pmax= pes[1]
        if pes[1] < pmin:
            pmin=pes[1]
print(f'O menor peso foi {pmin} e o maior peso foi {pmax}')
