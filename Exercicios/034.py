n1=float(input('Digite o salário do funcionário: '))

if n1 <= 1250:
    print(f'O salário passa a ser {n1+(n1*0.15)} com 15% de aumento.')
else:
    print(f'O salário passa a ser {n1+(n1*0.10)} com 10% de aumento.')