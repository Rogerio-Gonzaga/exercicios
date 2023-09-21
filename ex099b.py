from time import sleep
def maior(*num):
    maior=0
    print('*'*30)
    print('Analisando os valores!')
    for c in num:
        sleep(0.5)
        print(c, end=' ')
        sleep(0.5)
        if c > maior:
            maior=c
    print(f'foram os valores informados, {len(num)} valores ao total')
    sleep(0.5)
    print(f'O maior valor informado foi {maior}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()