import datetime

n1=int(input('Digite um ano para analisar. 0 se for o ano atual: '))

if n1==0:
    # n1=(datetime.datetime.now().year)
    n1=(datetime.date.today().year)

#bissexto é divisel por 4 e resta 0
#bissexto é divisivel por 100 e resta 0 se divisivel tanbém por 400 e restar 0

# n1%4==0 and n1%400!=0 or n1%400==0
if n1%100==0 and n1%400==0:
    print(f'{n1} é BISSEXTO')
elif n1%4==0 and n1%100!=0:
    print(f'{n1} é BISSEXTO')
else:
    print(f'{n1} NÃO É BISSEXTO')

