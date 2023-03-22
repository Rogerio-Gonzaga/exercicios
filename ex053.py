frase=str(input('Digite uma frase: ')).strip().upper()
frase1= ''.join(frase.split())
#print(frase1)
frase2= frase1[::-1]
if frase2 == frase1:
    print('Sua frase é um palindromo')
else:
    print('A frase escrita não é palindromo')
# a sacada da casa


