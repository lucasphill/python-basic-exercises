#cedulas de 50,20,10 e 1
valor_saque=int(input('Qual o valor a ser sacado? '))
quantidade_cedulas_50=0
quantidade_cedulas_20=0
quantidade_cedulas_10=0
quantidade_cedulas_1=0

while valor_saque > 0:
    if valor_saque >= 50:
        valor_saque-=50
        quantidade_cedulas_50+=1
    elif valor_saque >= 20:
        valor_saque-=20
        quantidade_cedulas_20+=1
    elif valor_saque >= 10:
        valor_saque-=10
        quantidade_cedulas_10+=1
    elif valor_saque >= 1:
        valor_saque-=1
        quantidade_cedulas_1+=1

print(f'Quantidade de notas de 50 {quantidade_cedulas_50}')
print(f'Quantidade de notas de 20 {quantidade_cedulas_20}')
print(f'Quantidade de notas de 10 {quantidade_cedulas_10}')
print(f'Quantidade de notas de 1 {quantidade_cedulas_1}')

'''
valor = int(inpuy('Qual valor quer sacar? R$'))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced +=1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}')
        if ced ==50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
'''