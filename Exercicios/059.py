n1=int(input('Digite o primeiro numero: '))
n2=int(input('Digite o segundo numero: '))
resultado=0

print('''
[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Novos numeros
[5] - Sair do programa
''')

while True:
    opcao=int(input('Digite a opção desejada: '))
    match opcao:
        case 1:
            resultado = n1 + n2
            print(f'O resultado da soma é {resultado}')    
        case 2:
            resultado = n1 * n2
            print(f'O resultado sa multiplicação é {resultado}')
        case 3:
            if n1 > n2:
                print(f'{n1} é maior')
            elif n2 > n1:
                print(f'{n2} é maior')
            else:
                print('Os dois numeros são iguais.')
        case 4:
            n1=int(input('Digite o primeiro numero: '))
            n2=int(input('Digite o segundo numero: '))
        case 5:
            print('Finalizando o programa.')
            break
        case _:
            print('Opção invalida.')