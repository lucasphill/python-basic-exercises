numero=int(input('Ver a tabuada de qual valor (0 para finalizar)? '))
while True:
    for i in range(1,11):
        print(f'{numero} X {i} = {i*numero}')
    numero=int(input('Qual outra tabuada quer ver (0 para finalizar)? '))
    if numero == 0:
        print('Encerrando o programa.')
        break