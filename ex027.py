nome=input('Me diga seu nome completo: ').strip()
primeironome= nome.split()
ultimonome= nome.rsplit()[-1:]
print('Seu primeiro nome é:' , primeironome[0])
print('seu ultimo nome é:' ,ultimonome[0])
#abaixo a versao do curso
print('Seu ultimo nome é: {}'.format(primeironome[len(primeironome)-1]))
#preciso usar mais a função .format