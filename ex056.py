soma=0
maioridademan=0
nomeman=''
mulherid=0
for ex in range(0,5):
    nome = str(input('Qual o seu nome: ')).strip().upper()
    idade = int(input('Qual sua idade: '))
    sexo = str(input('qual seu sexo M/F: '))
    soma=(idade+soma)
    soma2=soma/3
    if ex == 1 and sexo in 'Mm':
        maioridademan=idade
        nomeman=nome
    if sexo in 'Mn' and idade > maioridademan:
        maioridademan=idade
        nomeman=nome
    if sexo in 'Ff' and idade < 20:
        mulherid=mulherid+1


print(mulherid)
print(maioridademan,nomeman)
print ('A media de idade de todos são {:.2f} anos'.format(soma2))
