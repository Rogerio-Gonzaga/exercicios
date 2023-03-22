maior=0
menor=0
for ordem in range(1,6):
    peso = float(input('Me diga o peso da {}º pessoa: '.format(ordem)))
    if ordem == 1:
        maior=peso
        menor=peso
    else:
        if peso>maior:
            maior=peso
        if peso<menor:
            menor=peso
print('O maior peso entre os 5 é {:.2f} kg'.format(maior))
print('O menor peso entre os 5 é {:.2f} km'.format(menor))

