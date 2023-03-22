s = 0
co = 0
for c in range (1, 501):
    d = c % 2
    d2 = d == 0
    if d2 == False:
        #print(c)
        if c // 3 and c % 3 == 0:
            s=s+c
            co=co+1
#guanabara quebrou os numeros pares pulando de 2 em 2 começando com impar

print('A soma de todos os numeros impares que dividem por 3 são: {}' .format(s))
print('existem {} numeros impares que dividem por 3'.format(co))