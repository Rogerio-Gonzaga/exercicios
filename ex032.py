from datetime import date
ano=int(input('Digite um ano qualquer: '))
#formula do exercicio if ano%4 == 0 and ano % 100 !=0 or ano % 400 == 0:
if ano == 0:
    ano = date.today().year
    print(ano)
if ano % 400 == 0 & ano % 4 ==0 :
    print('É bissexto')
elif ano % 100 ==0 & ano % 4 == 0:
    print('Não é bissexto!')
elif ano % 4 == 0:
    print('É bissexto')
else:
    print('Não é bissexto!')