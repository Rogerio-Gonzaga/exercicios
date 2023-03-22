dias=int(input('Quantos dias foram utilizados na locação? '))
km=float(input('Quantos km foram rodados? '))
v1= dias*60
v2= km*0.15
v3= v1+v2
print('O carro foi alugado por {} dias e foram rodados {}km, \n'
      ' ficando assim um valor de {:.2f} a ser pago pelo aluguel'.format(dias,km,v3))
