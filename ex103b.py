def ficha(jog='Desconhecido', gol=0):
    print(f'O Jogador {jog} fez {gol} Gols no Campeonato!!!')


n = str(input('Nome do jogador: '))
g = str(input(f'Quantos gols o jogador {n} marcou? '))
if g.isnumeric():
    g = int(g)
else:
    g=0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n,g)