import math

cat_op=float(input('Digite o valor do cateto oposto: '))
cat_ad=float(input('Digite o valor do cateto adjacente: '))
print(f'O valor da hipotenusa é: {(cat_op**2 + cat_ad**2) ** (1/2):.2f}')
print(f'O valor da hipotenusa é (com modulo math): {math.hypot(cat_ad, cat_op):.2f}')