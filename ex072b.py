#formula do guanabara com bem menos linhas, usando o end= para adicionar o texto 'ao contexto da frase'
extenso=('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze',
         'treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    digito = int(input('Digite um numero de 0 a 20: '))
    if 0 <= digito <=20:
        break
    print('Tente novamente. ', end='')
print(f'Voce digitou o numero {extenso[digito]}')
