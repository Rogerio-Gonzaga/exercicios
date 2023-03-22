numero = int(input('Digite um Numero até 9999: '))
#print('Unidade:', numero[3])
#print('Dezena:', numero[2])
#print('Centena:', numero[1])
#print('Milhar:', numero[0])
#exercicio mais dificil ate o momento, não consegui fazer sozinho
u=numero//1 %10
d=numero//10 %10
c=numero//100 %10
m=numero//1000 %10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))