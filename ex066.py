n=c=s=0
while True:
    n=int(input('Digite um numero, (para parar digite 999): '))
    if n == 999:
        break
    c=c+1
    s=n+s
print(f'a soma de todos os {c} numeros digitados é {s}')