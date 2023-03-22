n1=int(input('Digite um numero: '))
n2= n1 // 2
n3= n1 % 2
n4= n1 // 3
n5= n1 % 3
n6= n1 // 5
n7= n1 % 5
n8= n1 // 7
n9= n1 % 7

if n1==2 or n1==3 or n1==5 or n1==7:
    print('primo')
elif n1 == 1:
    print('Nao é primo')
elif n3==1:
    #print('Impar')
    if n5 == 0 or n7 == 0 or n9 == 0:
        print('Não é primo')
    elif n5 <= 1 or n7 <= 1 or n9 <= 1:
        print('primo')
    else:
        print('Primo')
else:
    print('Não é primo')
#resoluçao do guanabara bem mais simplificada com 15 linhas




