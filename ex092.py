from datetime import date
ano= date.today().year
dados=dict()
nome=str(input('Nome: '))
idade=int(input('Ano de nascimento: '))
CTPS=int(input('Carteira de Trabalho (0 caso não tenha): '))
dados['Nome']=nome
dados['Idade']=ano-idade
dados['CTPS']=CTPS
if CTPS != 0:
    ctt=int(input('Ano de contratação: '))
    dados['Contratação']=ctt
    sal=float(input('Salario: '))
    dados['Salário']=sal
    aposent=(35+ctt)-idade
    dados['Aposentadoria']=aposent
#print(dados)
print('*'*30)
for k, v in dados.items():
    print(f'--> {k} tem o valor {v}')