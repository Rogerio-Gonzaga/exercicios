sal=float(input('Me diga seu salario meu jovem: '))
if sal>= 1250.00:
    print('Parabens, seu novo salario é {:.2f}'.format(sal+(10/100*sal)))
else:
    print('Parabens, seu novo salario é {:.2f}'.format(sal + (15 / 100 * sal)))