n1 = int(input('Me diga um numero: '))
n2 = int(input('Me diga outro numero: '))
print('Voce escolheu o numero {} e o numero {}'.format(n1, n2))
if n1 > n2:
    print('O Primeiro numero {} é maior que o segundo numero {}'.format(n1, n2))
elif n2 > n1:
    print('O segundo numero {} é maior que o primeiro numero {}'.format(n2, n1))
else:
    print('Os dois numeros são iguais')
