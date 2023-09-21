listamax=[]
lista1=[]
lista2=[]
med=0
while True:
    nome=str(input('Nome: '))
    lista2.append(nome)
    lista1.append(lista2[:])
    lista2.clear()

    for c in range(2):
        not1=int(input(f'Nota {c+1}: '))
        lista2.append(not1)
    med = sum(lista2[:])
    lista1.append(lista2[:])
    med = med / 2
    lista2.clear()
    lista2.append(med)
    lista1.append(lista2[:])
    lista2.clear()
    listamax.append(lista1[:])
    lista1.clear()
    opcao=str(input('Quer continuar: '))
    if opcao in 'Nn':
        break
print(listamax)
print('@*#'*15)
print('Nº',' '*2, 'NOME',' '*10,'MÉDIA')
for i, item in enumerate(listamax):
    print(f'{i+1} {item[0]}          {item[2]}')
n=''
while n != 999:
    n=int(input('Mostrar as notas de qual aluno?(999 interrompe): '))
    if n > len(listamax):
        print('Numero invalido!')
    if n 


