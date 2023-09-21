temp=[]
princ=[]
mai=men=0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))

    if len(princ) == 0:
        mai=men=temp[1]
    else:
        if temp[1] > mai:
            mai=temp[1]
        if temp[1] < men:
            men=temp[1]

    princ.append(temp[:])
    temp.clear()
    resp=str(input('Quer continuar [S/N]:  '))
    if resp in 'Nn':
        break
print(f'Voce cadastrou {len(princ)} pessoas')
print(f'O maior peso foi {mai}, peso de ',end='')
for n in princ:
    if n[1] == mai:
        print(f'[{n[0]}]',end=' ')
print()
print(f'O menor peso foi {men}, peso de ',end='')
for n in princ:
    if n[1] == men:
        print(f'[{n[0]}]',end=' ')
print()
