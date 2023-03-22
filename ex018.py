from math import radians, sin, cos, tan
num=int(input('Digite um angulo em graus: '))
sen=sin(radians(num))
cos=cos(radians(num))
tag=tan(radians(num))
print('Para o angulo que vc escolheu {}º, o seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'
.format(num,sen,cos,tag))



