print('Gerador de Progressão Aritimética')

n1=int(input('Digite o primeiro numero: '))
razao=int(input('Digite a razão da PA: '))
c=1

while True:
    while c <= 10:
        print(f'{n1} +' if c < 10 else f'{n1} =',end=' ')
        n1 = n1 + razao
        c+=1
    print('PAUSA')

    continuar=int(input('Quantos termos deseja mostrar a mais (0 para encerrar)? '))
    if continuar == 0:
        print('Encerrando o programa.')
        break
    else:
        c = c - continuar