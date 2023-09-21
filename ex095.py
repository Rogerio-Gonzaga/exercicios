dados=dict()
dadosfinais=[]
GOL=[]
while True:
    GOL.clear()
    dados['Jogador'] = str(input('Nome do jogador: '))
    dados['Partidas'] = int(input('Quantos jogos jogou? '))
    for c in range(dados['Partidas']):
        gol = int(input(f'Quantos gols ele marcou na {c + 1}º partida? '))
        GOL.append(gol)
        soma=sum(GOL)
    dados['GOLS'] = GOL[:]
    dados['SOMA']=soma
    dadosfinais.append(dados.copy())
    while True:
        opcao=str(input('Quer continuar [S/N]? ')).upper()
        if opcao in 'NS':
            break
        print('Digite S ou N')
    if opcao == 'N':
        break
print('#'*35)
print(dadosfinais)
print('#'*35)
print(f'{"Nº":<4} {"Nome":^10} {"Gols":>10} {"Total":>20}')
for n, t in enumerate(dadosfinais):
    print(f'{str(n):<4} {t["Jogador"]:^10} {str(t["GOLS"]):>10} {t["SOMA"]:>20}')

print('#'*35)
perg=''
while perg != 999:
    perg=int(input('Mostrar dados de qual jogador? '))
    if perg == 999:
        print('Finalizado!!!')
        break
    if perg <= len(dadosfinais)-1:
        print(f'Levantamento do jogador {dadosfinais[perg]["Jogador"]}')








