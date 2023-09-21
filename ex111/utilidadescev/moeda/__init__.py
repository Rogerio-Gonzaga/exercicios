def aumentar(preco=0, taxa=0, formato=False):
    r= preco + (preco* taxa/100)
    return r if formato == False else moeda(r)


def diminuir(preco=0, taxa=0, formato=False):
    r= preco - (preco* taxa/100)
    return r if formato == False else moeda(r)


def dobro(preco=0, formato=False):
    r= preco*2
    return r if formato == False else moeda(r)


def metade(preco=0, formato=False):
    r= preco/2
    return r if formato == False else moeda(r)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')


def resumo(preco=0, taxaalt=10, taxamen=13):
    print('*'*30)
    print('Resumo do Valor'.center(30))
    print('*'*30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco,True)}')
    print(f'Metade do preço: \t{metade(preco,True)}')
    print(f'{taxaalt}% de aumento: \t{aumentar(preco, taxaalt, True)}')
    print(f'{taxamen}% de redução: \t{diminuir(preco, taxamen, True)}')
    print('*'*30)
    return ''
