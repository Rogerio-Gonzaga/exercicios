frase=input('Digite uma frase: ').strip()
frase2=frase.lower()
print('Quantidade de vezes que letra a aparece a letra A:' , frase2.count('a'))
print('A primeira letra A aparece na posição:', frase2.find('a') )
print('A ultima letra A aparece na posição:', frase2.rfind('a') )