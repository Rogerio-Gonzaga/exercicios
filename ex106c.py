def ajuda(com):
    help(com)

def titulo(msg):
    tam=len(msg)+4
    print('#'*tam)
    print(f'  {msg}')
    print('*'*tam)



comando=''
while True:
    titulo('SISTEMA DE AJUDA PYHELP')
    comando=str(input('FUNÇAO OU BIBLIOTECA >'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('VOLTE SEMPRE!!!')

