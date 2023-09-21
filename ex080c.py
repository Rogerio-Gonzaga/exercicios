lista=[]
for ordem in range (0,5):
    numero=int(input('Digite um numero: '))
#if ordem == 0 or numero >= lista[-1]: --- mesmo comando simplificado.
    if ordem == 0:
        lista.append(numero)
        print('numero adicionado ao final da lista')
    elif numero >= lista[-1]:
        lista.append(numero)
        print('numero adicionado ao final da lista')
    else:
#guanabara usou while e pra isso ele criou um pos=0 e colocou um contador de pos
        for pos, list in enumerate(lista):
            if numero <= list:
                lista.insert(pos,numero)
                print(f'numero adicionado na posição {pos}')
                break

print(lista)


