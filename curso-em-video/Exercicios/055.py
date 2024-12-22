peso_maior=0
peso_menor=0

for i in range(1,4):
    peso_novo=int(input(f'Digite o peso da {i}ª pessoa: '))
    if i == 1:
        peso_maior=peso_novo
        peso_menor=peso_novo
    else:
        if peso_novo > peso_maior:
            peso_maior=peso_novo
        elif peso_novo < peso_menor:
            peso_menor=peso_novo

print(f'O maior peso foi {peso_maior} e o menor foi {peso_menor}')