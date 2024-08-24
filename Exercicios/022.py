nome=str(input('Digite seu nome completo: ')).strip()
# nome='Lucas Phill Soares Correa Pinto'

print(f'\nAnalisando seu nome...\n')
print(f'Seu nome em MAIÚSCULAS é: {nome.upper()}')
print(f'Seu nome em minúsculas é: {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome)-nome.count(' ')} letras.')
print(f'Seu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} letras')