import math
co=float(input('Me diga o valor do cateto oposto: '))
ca=float(input('Agora me de o valor do cateto adjacente: '))
h= (co **2 + ca **2) ** (1/2)
h1=math.sqrt(h)
print(' Se o cateto oposto vale {} e o cateto adjacente vale {}, entao a hipotenusa vale {:.2f}'
      .format(co,ca,h))




