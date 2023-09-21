lista=[]
opcao='S'
while opcao == 'S':
    n=(int(input('Digite um numero: ')))
    if n in lista:
        print('Esse numero ja esta na lista')
    else:
        lista.append(n)
        print('Numero adicionado...')
    opcao=str(input('Quer continuar [S/N]: ')).upper().strip()
print(f'Aque estao os numeros escolhidos: {sorted(lista)}')
