import datetime

nascimento=''
ano_atual=datetime.datetime.today().year
idade=0
maioridade=0
menoridade=0

for i in range(0,7):
    nascimento=int(input(f'Em que ano a {i}ª pessoa nasceu? '))
    idade=ano_atual-nascimento
    print(idade)

    if idade >= 21 :
        maioridade+=1
    else:
        menoridade+=1

print(f'{maioridade} são maiores de idade e {menoridade} são menores.')