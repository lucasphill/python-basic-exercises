n1=int(input('Quantos dias o carro ficou alugado? '))
n2=int(input('Quantos Km foram rodados? '))

print(f'O carro alugado por {n1} dias custará {(n1*60)+(n2*0.15):.2f}R$')