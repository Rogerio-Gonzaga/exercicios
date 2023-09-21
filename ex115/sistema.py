from ex115.lib.interface import *
#import * importa toda biblioteca
from time import sleep
from ex115.lib.arquivo import *

arq = 'Cursoemvideo.txt'
if not arquivoexiste(arq):
    criararquivo(arq)




while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair Do Sistema'])
    if resposta == 1:
        lerarquivo(arq)
    elif resposta == 2:
        cabecalho('Novo CADASTRO')
        nome=str(input('Nome: '))
        idade=leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo Do Sistema')
        break
    else:
        print('\033[31mERRO! Digite uma opção valida\033[m')
    sleep(1.5)