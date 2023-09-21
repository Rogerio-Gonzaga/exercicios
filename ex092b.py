from datetime import date
ano= date.today().year
dados=dict()
dados['nome']=str(input('Nome: '))
nasc=int(input('Ano de nascimento: '))
dados['idade']= ano - nasc
dados['CTPS']=int(input('Carteira de Trabalho (0 caso não tenha): '))
if dados['CTPS'] != 0:
    dados['Contratação']=int(input('Ano de contratação: '))
    dados['Salário']=float(input('Salario: '))
    dados['Aposentadoria']=dados['idade'] + (35+dados['Contratação'])- ano
print('*' * 30)
for k, v in dados.items():
    print(f'--> {k} tem o valor {v}')