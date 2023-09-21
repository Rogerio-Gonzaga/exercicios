from time import sleep
def contagem(i, f, p):
    if p == 0:
        p=1
    if p < 0:
        p=p*-1
    print('*'*30)
    print(f'Contagem de {i} a {f} de {p} em {p}')


    if i < f:
        cont=i
        while cont <= f:
            sleep(0.5)
            print(cont, end=' ')
            cont = cont + p
            sleep(0.5)
        print('FIM')

    if i > f:
        cont=i
        while cont >= f:
            sleep(0.5)
            print(cont, end=' ')
            cont = cont - p
            sleep(0.5)
        print('FIM')


contagem(1, 10, 1)
contagem(10, 0, 2)
print('*'*30)
ini=int(input('Agora diga o inicio: '))
fim=int(input('Agora diga o fim: '))
pas=int(input('Agora diga o passo: '))
contagem(ini,fim,pas)

