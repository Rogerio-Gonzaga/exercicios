lista = []
for ordem in range(0,5):
    peso = float(input('Me diga o peso de 5 pessoas: '))
    lista.append(peso)
    lista.sort()
print('a pessoa mais pesada tem {:.2f} kg enquanto a mais leve tem {:.2f} kg'.format(lista[-1],lista[0]))











