numero=soma=contador=0
while True:
    numero=int(input('Digite um numero (999 para parar):'))
    if numero == 999:
        break
    soma+=numero
    contador+=1
print(f'A soma total do {contador} numeros digitados foi {soma}.')