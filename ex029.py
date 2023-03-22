km=float(input('Diga a qual velocidade voce passou no radar: '))
if km<=80:
    print('Parabens, voce anda certinho meu brother!')
else:
    print('Vish meu irmao, voce foi multado em {:.2f} reais!!!'.format((km-80)*7))
