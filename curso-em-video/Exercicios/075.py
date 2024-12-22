tupla = ()
i = 0
contNumPar = 0
numsPar = ()

while i < 4:
    i+=1
    valor = int(input("Digite um numero de 0 a 9: "))
    tupla = tupla + (valor,)

    if valor % 2 == 0: contNumPar +=1 
    if valor % 2 == 0: numsPar = numsPar + (valor,)

print(f'Você digitou os valores: {tupla}')
print(f'O numero 9 aparece {tupla.count(9)} vezes')
print(f'O numero 3 aparece na {tupla.index(3)+1}ª posição') if 3 in tupla else print('O numero 3 não foi digitado')
print(f'O ultimo numero digitado foi {tupla[-1]}')
print(f'Quantidade de numeros pares é de {contNumPar}')
print(f'Os numeros pares digitados foram {numsPar}') if len(numsPar) != 0 else print('Não foram digitados numeros pares')