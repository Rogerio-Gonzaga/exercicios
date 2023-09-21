lista=[]
exp=str(input('Digite uma expressao: '))
for simbolo in exp:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Valido')
else:
    print('Invalido')