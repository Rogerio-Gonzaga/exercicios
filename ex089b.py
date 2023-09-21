lista= list()
while True:
    nome=str(input('Nome: '))
    not1=int(input('Nota 1: '))
    not2=int(input('Nota 2: '))
    opcao=str(input('Quer continuar [S/N]? '))
    media= (not1+not2)/2
    lista.append([nome,[not1,not2],media])
    if opcao in 'Nn':
        break
#print(lista)
print('#'*35)
print(f'{"Nº":<5} {"Nome":<10} {"Media":>15}')
for n, item in enumerate(lista):
    print(f'{n:<5} {item[0]:<10} {item[2]:>15}')
perg=''
while perg != 999:
    perg=int(input('As notas de qual aluno vc precisa? (999 interrompe): '))
    if perg == 999:
        print('Finalizado!!!')
    if perg <= len(lista)-1:
        print(f'As notas do aluno {lista[perg][0]} são {lista[perg][1]}')