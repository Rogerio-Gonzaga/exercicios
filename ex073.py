tabela=('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians',
        'Flamengo', 'Atletico PR', 'Atletico MG', 'Fortaleza',
        'São Paulo', 'America MG', 'Botafogo', 'Santos', 'Goias',
        'Bragantino', 'Curitiba', 'Cuiaba', 'Ceara', 'Atletico GO',
        'Avai', 'Juventude')
print('Lista do Brasileirão em 2022:' ,tabela)
print('='*40)
print('Os 4 primeiros:' ,tabela[0:4])
print('='*40)
print('Os 4 ultimos:' ,tabela[16:20])
#print('Os 4 ultimos:' ,tabela[-4:])
print('='*40)
print('O Corinthians se encontra na posição {}º'.format(tabela.index('Corinthians')+1))
#print(f'O Corinthians se encontra na posicão {tabela.index("Corinthians")+1}º')
#para usar espas dentro de outras aspas, uma tem que ser duplas e a outra simples
print('='*40)
print('Todos os times em ordem alfabetica:', sorted(tabela))
print('='*40)
#for pos, time in enumerate (tabela):
#        print(f'O Time {time} ficou na posição {pos+1}º')