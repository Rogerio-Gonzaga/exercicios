import math
co=float(input('Me diga o valor do cateto oposto: '))
ca=float(input('Agora me de o valor do cateto adjacente: '))
h= math.hypot(co,ca)
print(' Se o cateto oposto vale {} e o cateto adjacente vale {}, entao a hipotenusa vale {:.2f}'
      .format(co,ca,h))