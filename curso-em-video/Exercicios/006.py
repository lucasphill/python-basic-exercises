from math import sqrt 

n1=int(input('Digite um numero: '))

print(f'O dobro do numero é: {n1*2}')
print(f'O triplo do numero é: {n1*3}')
print(f'A raiz quadrada do numero é (por meio): {n1**(1/2):.2f}') #potencia por meio
print(f'A raiz quadrada do numero é (por função): {pow(n1,(1/2)):.2f}') #potencia por meio com função
print(f'A raiz quadrada do numero é (por biblioteca math): {sqrt(n1):.2f}') #usando biblioteca math