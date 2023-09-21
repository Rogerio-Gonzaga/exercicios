def notas(*n, sit=False):
    """
    dicionacios podem ser adicionados a qualquer momento no programa, ou seja, podemos colocar quantas notas
    quisermos.
    :param n: é a quantidade de numeros para notas podendo ser qlqr quantidade devido o *
    :param sit: situação da media, podendo ou não ser usada no programa
    :return: retorna o valor inteiro do programa (todos os dicionarios)
    """
    a = dict()
    a['qtd'] = len(n)
    a['maior'] = max(n)
    a['menor'] = min(n)
    a['media'] = sum(n)/len(n)
    if sit:
        if a['media'] >= 7:
            a['situação'] = 'BOA'
        elif a['media'] <= 5:
            a['situação'] = 'RUIM'
        else:
            a['situação'] = 'ATENÇÃO'
    return a



resp= notas(7.5, 9.5, 5, 8, 6, sit=True)
print(resp)