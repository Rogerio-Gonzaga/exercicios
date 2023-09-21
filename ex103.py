def ficha(n=0, g=0):
    n=str(input('Nome do jogador: ')).strip()
    g=str(input('Quantos gols ele marcou? ')).strip()
    if n == '':
        n='Desconhecido'
    if g == '':
        g=0

    return f'O Jogador {n} fez {g} gols'

#dessa forma se eu colocar nos gols uma letra, acaba dando erro (aparece a letra)

print(ficha())