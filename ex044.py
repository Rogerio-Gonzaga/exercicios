preco = float(input('Qual o valor do produto? '))
preco2= preco+(20/100*preco)
print('Qual será a forma de pagamento?''\n'
                '( 1 ) - a vista no dinheiro\n'
                '( 2 ) - a vista no cartão\n'
                '( 3 ) - parcelado em 2x\n'
                '( 4 ) - parcelado em 3x ou mais')
pag=int(input('Opção: ' ))
if pag == 1:
    print('Pagando a vista no dinheiro voce tem 10% de desconto, ficando assim o valor de R${:.2f}'.format(preco-(preco*10/100)))
elif pag == 2:
    print('Pagando a vista no cartao voce tem 5% de desconto, ficando assim o valor de R${:.2f}'.format(preco-(preco*5/100)))
elif pag == 3:
    print('Parcelando em 2x ficara 2 parcelas de R${:.2f}'.format(preco/2))
elif pag == 4:
    print('Em quantas vezes voce irá parcelar (de 3x até 10x 20% de juros):')
    x=int(input( ))
    print('Parcelando em {} vezes ficará {} parcelas de {:.2f}'.format(x, x, preco2/x))
else:
    print('opção não disponivel')














