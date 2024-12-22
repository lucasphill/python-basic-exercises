numero=int(input('Digite um numero: '))
soma=contador=0
continuar='S'
maior = menor = numero
while continuar == 'S':
    if numero > maior:
        maior=numero
    if numero < menor:
        menor=numero
    soma=numero+soma
    contador+=1
    continuar=str(input('Quer continuar (S para sim e N para encerrar.): ')). upper()
    if continuar == 'S':
        numero=int(input('Digite um numero: '))

print(f'\nA soma entre eles foi de {soma}')
print(f'A media entre eles foi de {soma/contador}')
print(f'O maior numero foi {maior}')
print(f'O menor numero foi {menor}')

#########################################################################################