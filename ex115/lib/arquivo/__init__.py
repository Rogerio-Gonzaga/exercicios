from ex115.lib.interface import *

def arquivoexiste(nome):
    try:
        a= open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Arquivo não criado')
    else:
        print('Arquivo criado com sucesso')

def lerarquivo(nome):
    try:
        a=open(nome, 'rt')
    except:
        print('Erro ao carregar lista!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} {dado[1]:>3} anos')

    finally:
        a.close()

def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a= open(arq, 'at')
    except:
        print('Houve um erro ao abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao escrever os dados!')
        else:
            print(f'{nome} adicionado com sucesso')
            a.close()

