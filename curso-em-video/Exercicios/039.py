import datetime

n1=int(input('Digite o ano de nascimento: '))
ano_atual=datetime.datetime.now().year #datetime.date.today().year
idade_atual=ano_atual-n1

print(f'Quem nasceu em {n1} tem(ou terá) {idade_atual} neste ano.')

if(idade_atual<18):
    print(f'Ainda faltam {18-idade_atual} anos para se alistar, que ocorrerá em {n1+18}')
elif(idade_atual==18):
    print(f'Você está no ano de se alistar, {ano_atual}.')
else:
    print(f'Você já passou do período de alistamento que foi em {n1+18}')