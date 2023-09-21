lista=[]
listafinal=[]
for l in range(3):
    for c in range(3):
        lista.append(int(input(f'Digite um numero para posição [{l},{c}]: ')))
        listafinal.append(lista[:])
        lista.clear()
#print(listafinal)
print(f'{ listafinal[0]} { listafinal[1]} { listafinal[2]}')
print(f'{ listafinal[3]} { listafinal[4]} { listafinal[5]}')
print(f'{ listafinal[6]} { listafinal[7]} { listafinal[8]}')

