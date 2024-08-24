print('ANALISADOR DE TRIANGULOS')
n1=float(input('Digite o valor do primeiro segmento: '))
n2=float(input('Digite o valor do segundo segmento: '))
n3=float(input('Digite o valor do terceiro segmento: '))

triangulo=[n1,n2,n3]
triangulo.sort()
print(triangulo)

if n1+n2 > n3:
    print('Você pode formar um triangulo!')
else:
    print('Você não pode formar um triangulo.')