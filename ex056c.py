media=0
manvelho=0
nomevelho=0
mulherid=0
for ordem in range (1,5):
    nome=str(input('Nome da {}º pessoa: '.format(ordem))).strip().upper()
    idade=int(input('Idade da {}º pessoa: '.format(ordem)))
    sexo=str(input('Sexo da {}º pessoa M/F: '.format(ordem))).strip().upper()
    media=media+idade
    mediaf=media/2
    if ordem == 1 and sexo in 'M':
        manvelho=idade
        nomevelho=nome
    if sexo in 'M' and idade >manvelho:
        manvelho=idade
        nomevelho=nome
    if sexo in 'F' and idade <20:
        mulherid=mulherid+1

print(mediaf)
print(manvelho,nomevelho)
print(f'mulher com menos de 20 anos = {mulherid}')


