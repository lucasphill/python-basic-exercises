n1=int(input('Digite a distancia da viagem: '))
#50c por km até 200km ou 45c acima de 200

# if 0<=n1<=200:
#     print(f'A viagem custará {n1*0.50:.2f}R$ a 0.50R$ por KM')
# else:
#     print(f'A viagem custará {n1*0.45:.2f}R$ a 0.45R$ por KM')

print(f'A viagem custará {n1*0.50:.2f}' if n1<=200 else f'A viagem custará {n1*0.45:.2f}')
#com operador ternário