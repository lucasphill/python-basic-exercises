maiores_de_idade=0
quantos_homens=0
quantas_mulheres_menos_20=0

while True:
    sexo=' '
    
    while True:
        try:
            idade=int(input('Insira a idade da pessoa: '))
            break
        except:
            print('Valor inválido, insira um número')
    
    while sexo not in 'MmFf':
        sexo=str(input('Insira o sexo da pessoa (M ou F): ')).upper().strip()[0]
    if sexo == 'M':
        quantos_homens += 1
    if idade > 18:
        maiores_de_idade += 1
    if idade <= 20 and sexo == 'F':
        quantas_mulheres_menos_20 += 1

    continuar = str(input('Deseja continuar (S/N)? ')).upper().strip()
    if continuar in 'Nn':
        break

print(f'Maiores de idade = {maiores_de_idade}')
print(f'Homens = {quantos_homens}')
print(f'Mulheres menores de 20 = {quantas_mulheres_menos_20}')