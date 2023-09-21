from datetime import date
def voto(texto):
    if id <= 15:
        print(f'Com {id} anos: Não Vota')
    elif id >= 65:
        print(f'Com {id} anos: Voto Opcional')
    else:
        print(f'Com {id} anos: Voto Obrigatorio')


ano=date.today().year
nasc= int(input('Qual seu ano de nascimento?  '))
id=ano-nasc
voto(id)
#Correto seria colocar return ao inves de print() no exercicio