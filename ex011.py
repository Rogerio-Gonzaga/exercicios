altura=float(input('Qual a altura da parede? '))
largura=float(input('Qual a largura da parede? '))
area=altura*largura
tinta=area/2
print(' Se a Altura da sua parede é {} e a largura é {}, sua area equivale a {:.2f}m², \n '
'Para pintar essa parede vc irá precisa de {:.2f} litros de tinta' .format(altura,largura,area,tinta))
