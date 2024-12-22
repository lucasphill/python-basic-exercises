triangulo=[]
triangulo.append(int(input('Digite o tamanho do primeiro segmento: ')))
triangulo.append(int(input('Digite o tamanho do segundo segmento: ')))
triangulo.append(int(input('Digite o tamanho do terceiro segmento: ')))
triangulo.sort()

if triangulo[0]+triangulo[1] <= triangulo[2]:
    print('Não é possivel fazer um triangulo com esses valores.')
elif triangulo[0] == triangulo[1] == triangulo[2]:
    print('Este é um triangulo equilátero.')
elif triangulo[0] != triangulo[1] != triangulo[2]:
    print('Este é um triangulo escaleno.')
else:
    print('Este é um triangulo isósceles')