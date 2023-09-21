time=[]
jogador={}
partidas=[]

while True:
    jogador.clear()
    jogador['Nome']=str(input('Nome do Jogador: '))
    tpart = int(input(f'Quantas patidas {jogador["Nome"]} jogou? '))
    partidas.clear()
    for c in range(tpart):
        partidas.append(int(input(f' Quantos gols {jogador["Nome"]} fez na {c+1} partida?  ')))
    jogador['Gol']=partidas[:]
    jogador['Total']=sum(partidas)
    time.append(jogador.copy())
    while True:
        resp=str(input('Quer continuar [S/N]: ')).upper()
        if resp in 'SN':
            break
        print('Digite apenas S ou N')
    if resp == 'N':
        break
print('#*'*30)
print('COD. ',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('#*'*30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for nick in v.values():
        print(f'{str(nick):<15}',end='')
    print()
print('#*'*30)
while True:
    busca=int(input('Qual jogador quer buscar dados:(999 parar!) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO!!! o codigo {busca} não pertence a nenhum jogador!')
    else:
        print(f'Levantando dados do jogador {time[busca]["Nome"]}')
        for i, g in enumerate(time[busca]['Gol']):
            print(f'   No jogo {i+1} fez {g} gols.')
print('#*'*30)
print('VOLTE SEMPRE')
