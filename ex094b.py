Galera=[]
pessoas = dict()
soma=media=0
while True:
    pessoas.clear()
    pessoas['Nome']=str(input('NOME: '))
    while True:
        pessoas['Sexo']=str(input('Sexo [M/F]: ')).upper()
        if pessoas['Sexo'] in 'MF':
            break
        print('Digite apenas M ou F')
    pessoas['Idade']=int(input('Idade: '))
    soma=soma+pessoas['Idade']
    Galera.append(pessoas.copy())
    while True:
        resp=str(input('Quer continuar [S/N]: ')).upper()
        if resp in 'SN':
            break
        print('Digite apenas S ou N')
    if resp == 'N':
        break
print(Galera)
print(f'A) Ao todo temos {len(Galera)} pessoas cadastradas')
media = soma / len(Galera)
print(f'B) A media de idade é de {media:5.2f} anos')
print('C) As mulheres cadastradas são: ', end='')
for p in Galera:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]}', end='... ')
print()
print('D) Lista das pessoas acima da média: ')
for p in Galera:
    if p['Idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v} ; ' , end='')
        print()
print('<<<<ENCERRADO>>>>')
