lista=[]

for c in range (0,5):
    n=int(input('Digite um numero: '))
    print('numero adicionado!')
    for pos, num in enumerate(lista):
        if n < num:
            lista.insert(pos,n)
            break
    else:
        lista.append(n)
print(lista)


