lista=[]
exp=input('Digite uma expressao: ')
lista.append(exp)

if exp[0] == '(':
    if exp.count('(') == exp.count(')'):
        print('Valida')
    else:
        print('Invalida')
elif exp[0] == ')':
    print('Invalida')


