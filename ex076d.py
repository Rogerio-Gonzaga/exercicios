lista=('Arroz',23.90,'Feijão',11,'Macarrão',3.80,'Leite',4.20,'Bisnaguinha',6,'Margarina',6.40,'File de Frango',
       12.30,'Carne Moida',37.90,'Sal',2.50,'Açucar',4.90)
print('='*43)
print(f"{'Lista de compras':^43}")
print('='*43)
for item in range (0, len(lista)):
    if item %2==0:
        print(f'{lista[item]:.<35}',end=' ')
    else:
        print(f'R${lista[item]:>5.2f}')
print('='*43)