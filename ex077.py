tupla=('Arroz','Feijão','Macarrão','Leite','Bisnaguinha','Margarina','File de Frango',
       'Carne Moida','Sal','Açucar')

for item in range(0, len(tupla)):
    if 'a' in tupla or 'e' in tupla or 'i' in tupla or 'o' in tupla or 'u' in tupla:
        print('Na Palavra', tupla[item], 'temos as vogais {}'.format(tupla[item]))