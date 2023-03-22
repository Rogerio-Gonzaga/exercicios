sexo= 'F' and 'M'
#usado while sexo not in 'FM": no exercicio do guanabara
while sexo:
    sexo=str(input('Qual o seu sexo [F/M]: ')).upper().strip()[0]
    if sexo=='M' or sexo=='F':
        print('Seu sexo é {}'.format(sexo))
        break




