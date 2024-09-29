tupla = (
    'PALAVRA',
    'MOUSE',
    'TECLADO',
    'MONITOR',
    'CELULAR',
    'FONE DE OUVIDO',
)

for i in tupla:
    print(f'Na palavra {i} temos as vogais ', end='')
    for l in i:
        if l in 'AEIOU':
            print(l, end=' ')
    print()