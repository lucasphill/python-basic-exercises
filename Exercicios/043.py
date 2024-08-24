peso=float(input('Digite seu peso(kg): '))
altura=float(input('Digite sua altura : '))
imc=peso/altura**2
#18.5 - 25 - 30 - 40
print(f'Seu IMC é {imc:.2f}')
if imc < 18.5:
    print('Você está abaixo do peso (abaixo de 18.5)')
elif imc < 25:
    print('Você está no peso ideal (Entre 18.5 e 25)')
elif imc < 30:
    print('Você está com sobrepeso (Entre 25 e 30)')
elif imc < 40:
    print('Você está em obesidade (Entre 30 e 40)')
else:
    print('Você está em obesidade morbida (Acima de 40)')