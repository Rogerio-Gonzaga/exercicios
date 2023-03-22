vcasa=float(input('Qual o valor da casa? '))
sal=float(input('Qual o seu salario? '))
temp=int(input('Em quantos anos vc pretende pagar? '))
mes= temp*12
#print(mes)
v1= vcasa/mes
print('O valor da sua mensalidade ficará {:.2f}'.format(v1))
if v1 < (sal*30/100):
    print('Seu emprestimo foi aprovado!')
else:
    print('Infelizmente seu emprestimo não foi aprovado!')
