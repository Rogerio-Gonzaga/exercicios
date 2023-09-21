lista = []
for linha in range(5):
    n = int(input("Digite um número: "))
    for pos, num in enumerate(lista):
        if n < num:
            lista.insert(pos, n)
            break
    else:
        lista.append(n)
print(lista)






