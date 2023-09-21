dados=dict()
lista=[]
listaidade=[]
qtd=0
media=0
mulher=[]
acmedia=0
while True:
    nome=str(input('Nome: '))
    dados['Nome']=nome
    sexo=str(input('Sexo[M/F]: ')).upper()
    dados['Sexo']=sexo
    if sexo in 'Ff':
        mulher.append(nome)
    idade=int(input('Idade: '))
    dados['Idade']=idade
    listaidade.append(idade)
    lista.append(dados.copy())
    qtd=qtd+1
    opcao=str(input('Quer continuar [S/N]? ')).upper()
    if opcao in 'Nn':
        break
#print(lista)
print(f'Temos {qtd} pessoas cadastradas')
media=(sum(listaidade)/(qtd))
print(f'A Média de idades é {media:.2f}')
print(f'As mulheres cadastradas são {mulher}')
print('Pessoas acima da media de idade')
for item in lista:
    if item['Idade'] > media:
        print(item)

