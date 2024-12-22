tabela = (
    'Monster', 11.99,
    'Celular', 4500.00,
    'Fone de ouvido', 210.97,
    'Mouse', 180,
    'Oculos', 1100,
    'Teclado', 320.50,
)

print('='*42)
print(f'{'Lista de Preços':^40}')
print('='*42)

for i in range(0, len(tabela),2):
    print(f'{tabela[i]:.<30} R$ {tabela[i+1]:>7}')

print('='*42)