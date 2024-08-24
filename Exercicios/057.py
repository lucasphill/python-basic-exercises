while True:
    valor=str(input(f'Digite o sexo (M ou F): ')).upper().strip()
    print(valor)

    if valor == 'M':
        print('Você selecionou Masculino')
        break
    elif valor =='F':
        print('Você selecionou Feminino')
        break
    else:
        print('Digite uma opção valida, M para masculino ou F para feminino.')

#################################################################################

sexo=str(input('Informe o seu sexo: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo=str(input('Dados invlálidos. Por favor, informe seu sexo: ')).strip().upper()
print(f'Sexo {sexo} registrado com sucesso.')