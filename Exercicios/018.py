import math

a1=float(input('Digite um angulo para identificar o SEN, COS e TAN: '))
s=math.sin(math.radians(a1))#utilizando modulo math para converter angulo em radianos
c=math.cos(a1*(math.pi/180))#sem utilizar modulo para converter angulo em radianos
t=math.tan(math.radians(a1))#sin cos e tan somente funciona se o valor informado for em radianos

print(f'Angulo: {a1} \nSeno: {s:.1f} \nCosseno: {c:.1f}\nTangente: {t:.1f}')