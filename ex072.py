extenso=('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze',
         'treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

digito=int(input('Digite um numero de 0 a 20: '))
if digito >=0 and digito <21:
    print(extenso[digito])

else:
    while True:
        digito = int(input('Tente novamente!!! Digite um numero de 0 a 20: '))
        if digito >= 0:
            if digito < 21 :
                print(extenso[digito])
                break
