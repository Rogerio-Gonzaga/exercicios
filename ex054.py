from datetime import date
#print(ano)
#menor
a1=0
#maior
a2=0
ano = date.today().year
for c in range(0,7):
    nasc = int(input('Me diga o ano de nascimento de 7 pessoas: '))
    a3= ano-nasc
    if a3>= 17:
        a1=a1+1
    else:
        a2=a2+1
print('Desses 7 citados {} são maiores e {} são menores de idade'.format(a1,a2))
# o contador comeca em 0 e vai somando 1 cada vez que a condição acontece.









