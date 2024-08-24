print(f'{'':*^26}')
print(f'{'10 NUMEROS DE UMA PA': ^26}')
print(f'{'':*^26}')

n1=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razão: '))
decimo = n1 + (10-1) * razao
# soma=n1
# for c in range(0,10):
#     print(soma,end=' -> ')
#     soma=soma+razao
# print('FIM')
    
for c in range(n1,decimo+razao,razao):
    print(c,end=' -> ')
print('END')