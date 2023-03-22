opcao='S'
maior18=0
homem=0
mulher20=0
c=0
while opcao !='N':

    print('Cadastre uma pessoa!')
    print('-' * 20)
    i=int(input('Digite sua idade: '))
    if i > 17:
       maior18=maior18+1
    while True:

        s=str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
        if s == 'M':
            homem=homem+1
        if s == 'F' and i < 20:
            mulher20=mulher20+1
        if s == 'M' or s == 'F':
            break

    while True:
        print('-' * 20)
        opcao=str(input('Quer continuar [S/N]: ')).upper().strip()[0]
        if opcao=='S' or opcao == 'N':
            break
print(f'De todos cadastrados, {maior18} pessoas são maiores de 18 anos')
print(f'De todos, {homem} são homens')
print(f'{mulher20} mulheres com menos de 20 anos')
