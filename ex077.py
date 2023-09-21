tupla=('Arroz','Feijao','Macarrao','Leite','Bisnaguinha','Margarina','File de Frango',
       'Carne Moida','Sal','Açucar')
#primeiro ordenamos a lista com os itens da tupla e completamos com o resto da frase 'temos as vogais'.
#o end para manter a linha (continuação) e o \n antes pra pular de linha quando comecar outro.
for item in tupla:
    print(f'\nNa palavra {item.upper()} temos as vogais: ', end=' ')
#criamos outro FOR para repetir a identificação da letra dentro da palavra (cada palavra é uma lista)
    for vogal in item:
#usamos o IF para dar continuidade na identificação da letra
        if vogal in 'aAeEiIoOuU':
#printamos a letra que foi localizada se for identificada
            print(f'{vogal.lower()}', end=' ')







