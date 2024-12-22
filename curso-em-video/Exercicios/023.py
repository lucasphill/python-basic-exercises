n1=int(input('Digite um numero até 9999: '))

print(f'\nAnalisando o numero {n1}\n')

unidade=(n1)-(n1//10)*10
#(1234)-(1234//10=123)*10=1230 - 1230-1234=4
dezena=(n1//10)-(n1//100)*10
#(1234//10=123)-(1234//100=12)*10=120 - 123-120=3
centena=(n1//100)-(n1//1000)*10
#(1234//100=12)(1234//1000=1)*10=10 - 12-10=2
milhar=n1//1000
#1234//1000=1
'''
u=(n1 // 1) % 10
d=(n1 // 10) % 10
c=(n1 // 100) % 10
m=(n1 // 1000) % 10

1234/1= 1234/10=123 - resta 4
1234/10= 123/10=12 - resta 3
1234/100= 12/10=1 - resta 2
1234/1000= 1/10=0.1 - resta 1

Pra quem achou a explicação complicada:
Veja os exemplos abaixo.
Divisão: 1234 / 10 = 123,4
Divisão inteira: 1234 //10 = 123
Módulo: 1234 % 10 = 4
Pra ele descobrir a centena ele faz isso:
Faz a divisão inteira por 100: 1234 // 100 = 12
Depois pega o resultado e dividi por 10, mas pega só o resto dessa divisão (que é o módulo): 12 % 10 = 2
Ou seja, a centena é 2.
'''

print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')