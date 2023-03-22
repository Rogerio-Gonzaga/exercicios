#c=3 por ja ter printado o c1 e c2 antes do while
c=3
n=int(input('Digite quantos numeros vc quer na sequecia: '))
t1=0
t2=1
t3=0
print('{}-> {}'.format(t1,t2),end='-> ')
while c <= n:
    t3 = t1 + t2
    print(t3, end='-> ')
    t1=t2
    t2=t3
    c=c+1
print('FIM')