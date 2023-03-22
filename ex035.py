m1=int(input('Me diga uma medida: '))
m2=int(input('Me diga outra medida: '))
m3=int(input('Me diga mais uma medida: '))
if m1+m2 > m3 and m2+m3 > m1 and m3+m1 > m2:
#if (m1 + m2 < m3) or (m2 + m3 < m1) or (m1 + m3 < m2):
    print('Suas medidas podem formar um triangulo')

else:
    print('Suas medidas nao formam um triangulo')