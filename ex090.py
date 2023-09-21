dados = {}
nome=str(input('Nome: '))
dados['Nome']=nome
media=float(input(f'Média de {dados["Nome"]}: '))
dados['Média']=media

if media <= 6:
    dados['Situação']= 'Reprovado'
if media > 6:
    dados['Situação']= 'Aprovado'
for k, v in dados.items():
    print(f'{k} é igual à {v}')