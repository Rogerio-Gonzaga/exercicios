from datetime import date
ano=int(input('Qual o ano de nascimento do aluno? '))
aano= date.today().year
idade= aano-ano
if idade <= 9:
    print('Voce tem {} anos, esta na categoria Mirim'.format(idade))
elif idade <=14:
    print('Voce tem {} anos, esta na categoria Infantil'.format(idade))
elif idade <=19:
    print('Voce tem {} anos, esta na categoria Junior'.format(idade))
elif idade <=25:
    print('Vonce tem {} anos, esta na categoria Senior'.format(idade))
else:
    print('Voce tem {} anos, esta na categoria Master'.format(idade))


