lista=('Arroz',23.90,'Feijão',11,'Macarrão',3.80,'Leite',4.20,'Bisnaguinha',6,'Margarina',6.40,'File de Frango',
       12.30,'Carne Moida',37.90,'Sal',2.50,'Açucar',4.90)
print('='*60)
print(f"{'Lista de compras':^60}")
print('='*60)
for item in range(0, len(lista)):
       if item %2==0:
              print(f"{lista[item]:.<35}{'R$':^} {lista[item+1]:>5.2f}")
              #print('{:.<35} R$ {:>5.2f}'.format((lista[item]),(lista[item+1]) ))