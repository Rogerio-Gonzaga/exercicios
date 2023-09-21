lista=[]
dados=dict()
jogador=str(input('Nome do jogador: '))
dados['Jogador']=jogador
partidas=int(input('Quantas partidas ele jogou? '))
dados['Partidas']=partidas
for c in range(partidas):
    gol=int(input(f'Quantos gols ele marcou na {c+1}º partida? '))
    lista.append(gol)
dados['GOLS']=lista
soma=sum(lista)
dados['Total']=soma
#print(dados)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')

print(f'O jogador {jogador} jogou {partidas} partidas')
for num, p in enumerate(lista):
    print(f'==> Na partida {num+1} fez {p} Gols')
print(f'Fez um total de {soma} Gols')
