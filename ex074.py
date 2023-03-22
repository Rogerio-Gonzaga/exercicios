import random
n1=random.randint(1,10)
n2=random.randint(1,10)
n3=random.randint(1,10)
n4=random.randint(1,10)
n5=random.randint(1,10)
ordem=(n1,n2,n3,n4,n5)
print('Os valores sorteados foram: ',ordem)
ordem=sorted(ordem)
#print(ordem)
print('O maior: ',ordem[-1])
print('O menor: ',ordem[0])



