numero=0
soma=0
contador=0
while True:
    numero=int(input('Digite um numero (999 para parar):'))
    if numero == 999:
        break
    soma+=numero
    contador+=1
print(f'A soma total do {contador} numeros digitados foi {soma}.')

##################################################################################

num=cont=som=0
num=int(input('Digite um numero (999 para parar):'))
while num != 999:
    som += num
    cont += 1
    num=int(input('Digite um numero (999 para parar):'))
print(f'Você digitou {cont} numeros  e a soma entre eles foi {som}')
