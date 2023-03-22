from datetime import date
a1 = int(input('Em qual ano voce nasceu? '))
ano1 = date.today().year
idade = ano1 - a1
#print(idade)
if idade==18:
    print('Voce tem {} anos e estamos em {}, esse ano voce precisa se alistar!'.format(idade, ano1))
elif idade < 18:
    print('Voce tem {} anos, faltam {} anos pro seu alistamento, preparece!'.format(idade, 18-idade))
else:
    print('Ja estamos em {} e vc tem {} anos, passaram-se {} anos da data do seu alistamento!'.format(ano1,idade, idade-18))


