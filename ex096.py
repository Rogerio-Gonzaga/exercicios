s=0
def area(a,b):
    s = a * b
    print(f'A area de um terreno de {a} x {b} é de {s:.2f}m²')


print('Controle de terreno')
print('*'*20)
a=float(input('Qual a largura do seu terreno? '))
b=float(input('Qual o cumprimento do seu terreno? '))
area(a, b)
area(a, b)