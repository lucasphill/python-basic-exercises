import datetime

ano=int(input('Qual o ano de nascimento do atleta? '))
ano_atual=datetime.date.today().year
idade=ano_atual-ano

print(f'A idade do atleta é: {idade}')

if idade <= 9:
    print('Categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JUNIOR')
elif idade <= 25:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')