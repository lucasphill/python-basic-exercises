n1=float(input('Qual a velocidade do carro: '))

if n1 > 80:
    n2=(n1-80)*7
    print(f'Você foi multado em {n2:.2f}R$! A velocidade permitida é de 80Km/h. Dirija com cuidado!')
else:
    print(f'Muito bom! Dirija com cuidado!')