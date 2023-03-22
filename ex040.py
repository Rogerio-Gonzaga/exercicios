n1=float(input('Nota do primeiro semestre: '))
n2=float(input('Nota do segundo semestre: '))
nf= (n1+n2)/2
if nf < 5.0:
    print('Sua média final foi {}, infelizmente voce foi Reprovado!'.format(nf))
elif nf >= 7.0:
    print('Parabéns, sua média foi {}, voce está aprovado!!!'.format(nf))
else:
    print('Sua nota foi {}, voce está de recuperação!'.format(nf))

