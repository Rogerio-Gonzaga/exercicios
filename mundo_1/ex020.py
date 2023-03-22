import random
n1=input('Diga o nome do primeiro aluno: ')
n2=input('Diga o nome do segundo aluno: ')
n3=input('Diga o nome do terceiro aluno: ')
n4=input('Diga o nome do quarto aluno: ')
lista=[n1,n2,n3,n4]
random.shuffle(lista)
print('Os alunos sorteados são: ')
print(lista)


