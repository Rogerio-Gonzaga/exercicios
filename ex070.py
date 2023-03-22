total=0
pmaxmil=0
pmaxbarato=0
itembarato= ''
opcao = ''
while opcao != 'N':
    print('*'*20)
    print('Lojas Mão de Vaca')
    print('*'*20)
    item=str(input('Nome do item: ')).upper().strip()
    pr=float(input('Preço:R$ '))
    if total == 0 and pr > 0:
        itembarato=item
        pmaxbarato=pr
    if pr < pmaxbarato:
        itembarato=item
        pmaxbarato=pr
    if pr > 0:
        total=total+pr

        if pr >= 1000:
           pmaxmil=pmaxmil+1

    while True:
        opcao=str(input('Quer continuar [S/N]: ')).upper().strip()[0]
        if opcao == 'S' or opcao == 'N':
            break
print('*'*20)
print(f'O valor total dos itens é {total:.2f}')
print(f'Temos {pmaxmil} itens com preço acima de R$ 1000,00')
print(f'O item mais barato custou {pmaxbarato:.2f} e foi o/a {itembarato}')