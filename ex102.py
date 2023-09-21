def fatorial(n, show=False):
    """
    Exercicio calcula o fatorial de um numero
    :param n: é o numero para qual teremos o fatorial
    :param show: para ativar ou desativar a conta junto com a resposta
    :return: é o resultado do calculo fatorial
    """
    f=1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print('x', end='')
            else:
                print('=',end='')
        f=f*c
    return f


n=int(input('Digite um numero: '))
print(fatorial(n,show=False))
help(fatorial)
