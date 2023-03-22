import math
kg=float(input('Me diga seu peso: '))
alt=float(input('Me diga sua altura: '))
imc= kg/(alt**2)
print('Seu IMC é ',imc.__ceil__())
if imc < 18.5:
    print('Voce esta abaixo do peso recomendado!')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Cuidado, voce está com sobrepeso!')
elif imc <= 40:
    print('voce esta em grau de obesidade, cuidado!')
else:
    print('Voce esta com grau de obesidade morbida!!!')
