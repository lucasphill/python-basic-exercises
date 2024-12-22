largura=float(input('Digite a largura da parede: '))
altura=float(input('Digite a altura da parede: '))

area=largura*altura
#2m de parede usa 1l de tinta
tinta=area/2

print(f'A parede de altura {altura}m por {largura}m de largura tem area de {area}m².')
print(f'Para printar essa parede, será necessário {tinta:.2f} litros de tinta.')