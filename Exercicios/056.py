idade_total=0
idade_homem_mais_velho=0
quantidade_mulheres_menores_20=0

for p in range(1,5):
    nome=str(input(f'Digite o nome da {p}ª pessoa: ')).title()
    idade=int(input(f'Digite a idade da {p}ª pessoa: '))
    sexo=str(input(f'Digite o sexo da {p}ª pessoa (M ou F): ')).upper()
    idade_total+=idade

    if sexo == 'M' and idade > idade_homem_mais_velho:
        nome_homem_mais_velho=nome
        idade_homem_mais_velho=idade
    elif sexo == 'F' and idade <= 20:
        quantidade_mulheres_menores_20+=1

print(f'\nIdade do homem mais velho: {idade_homem_mais_velho}')
print(f'Nome do homem mais velho: {nome_homem_mais_velho}')
print(f'Quantidade de mulheres menores que 20 anos: {quantidade_mulheres_menores_20}')
print(f'Média de idades é: {idade_total/4:.2f}')