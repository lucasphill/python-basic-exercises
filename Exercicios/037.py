n1=int(input('Digite um numero inteiro: '))

print(f'1 - Converter para BINARIO: ')
print(f'2 - Converter para OCTAL: ')
print(f'3 - Converter para HEXADECIMAL: ')

while True:
    opcao=int(input('Digite sua opção: '))
    match opcao:
        case 1:
            print(f'O BINÁRIO do numero {n1} é: {bin(n1)[2:]}')
            break
        case 2:
            print(f'O OCTAL do numero {n1} é: {oct(n1)[2:]}')
            break
        case 3:
            print(f'O HEXADECIMAL do numero {n1} é {hex(n1)}')
            break
        case _:
            print('Opção invalida.')
