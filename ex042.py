m1=int(input('Me diga uma medida: '))
m2=int(input('Me diga outra medida: '))
m3=int(input('Me diga mais uma medida: '))
if m1+m2 > m3 and m2+m3 > m1 and m3+m1 > m2:
    print('Suas medidas formam um triangulo')
    if m1 == m2 and m2 == m3 and m1 == m3:
         print('Seu triangulo tem todos os lados iguais, sendo assim equilatero')
    elif m1!=m2 and m2!=m3 and m3!=m1:
         print('Seu triangulo tem todos os lados diferentes, sendo assim escaleno')
    else:
         print(' Seu triangulo tem apenas 2 lados iguais sendo assim um isosceles')
else:
    print('Suas medidas não formam um triangulo')