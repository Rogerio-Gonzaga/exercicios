print('='*30)
print('BANCO DO PYTHON')
print('='*30)
sq=int(input('Qual o valor a ser sacado: R$ '))

n50=int(sq/50)
if n50>=1:
    print(f'{n50} notas de 50,00')
sq=sq-(n50*50)
n20=int(sq/20)
if n20>=1:
    print(f'{n20} notas de 20,00')
sq=sq-(n20*20)
n10=int(sq/10)
if n10>=1:
    print(f'{n10} notas de 10,00')
sq=sq-(n10*10)
n1=int(sq/1)
if n1>=1:
    print(f'{n1} notas de 1,00')




