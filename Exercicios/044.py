print('BEM VINDO AO MERCADO')
valor=float(input('Insira o valor da compra (R$): '))

print('''Como deseja pagar?
      [1] - A vista (desconto de 10%)
      [2] - A vista no cartão (desconto de 5%)
      [3] - 2x no cartão (sem desconto)
      [4] - 3x no cartão ou mais (20% de juros)''')

while True:
    opcao=int(input('Escolha uma opção: '))
    match opcao:
        case 1:
            print(f'O valor a pagar será de {valor-valor*0.10}')
            break
        case 2:
            print(f'O valor a pagar será de {valor-valor*0.05}')
            break
        case 3:
            print(f'O valor a pagar é {valor} em 2x de {valor/2}')
            break
        case 4:
            parcelas=int(input('Quantas parcelas?'))
            print(f'O valor a pagar será de {valor+valor*0.20} em {parcelas}x de {(valor+valor*0.20)/parcelas}')
            break
        case _:
            print('Opção invalida')
