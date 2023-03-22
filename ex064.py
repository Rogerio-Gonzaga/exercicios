n=c=s=0
while n != 999:
    n=int(input('Digite um numero:(999 para encerramento): '))
    if n != 999:
        c=c+1
        s=n+s
print('todos os digitados {} e somam-se {}'.format(c,s))

#guanabara colocou o n=int(input('Digite um numero:(999 para encerramento): ')) fora e dentro do while ao inves do if