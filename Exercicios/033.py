n1=int(input('Digite o primeiro numero: '))
n2=int(input('Digite o segundo numero: '))
n3=int(input('Digite o terceiro numero: '))

'''
menor=n1 # verificando menor com if
if n2 < n1 and n2 < n3:
    menor=n2
if n3 < n1 and n3 < n2
    menor=n3
'''

lista=[n1, n2, n3]
crescente=sorted(lista)
print(sorted(lista))

print(f'O menor valor foi {crescente[0]}')
print(f'O maior valor foi {crescente[2]}')