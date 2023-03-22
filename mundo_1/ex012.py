vi=float(input('Valor da peça:R$ '))
vf=vi-(5/100*vi)
print(' O valor da peça é R${}, caso o pagamento seja à vista vc terá 5% de desconto,\n ' 
'chegando ao valor de R${:.2f}'.format(vi,vf))