dados=[]
lista1=[]
lista2=[]
for c in range (0,7):
    numero=int(input(f'Me diga um numero para posição {c+1}: '))
    if numero %2 ==0:
        lista1.append(numero)
    else:
        lista2.append(numero)
dados.append(lista1)
dados.append(lista2)
print(f'Numeros pares {sorted(lista1)}')
print(f'Numeros impares {sorted(lista2)}')
print(dados)