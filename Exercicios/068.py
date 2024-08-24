import random
vitorias=0
while True:
    numero=int(input('Digite um valor numerico: '))
    fator=' '
    while fator not in 'PARIMPAR':
        fator=str(input('Par ou impar? ')).upper().strip()
        print(fator)
    computador=random.randint(0,10)
    soma=numero+computador
    print(f'Você jogou {numero} e o computador {computador}. No total deu {soma}')
    if soma%2==0 and fator == 'PAR':
        print('Deu PAR! Você venceu!')
        vitorias+=1
    if soma%2==0 and fator == 'IMPAR':
        print(f'Deu PAR! Você PERDEU! Foram {vitorias} vitórias!')
        break
    if soma%2!=0 and fator == 'PAR':
        print(f'Deu IMPAR! Você PERDEU! Foram {vitorias} vitórias!')
        break
    if soma%2!=0 and fator == 'IMPAR':
        print('Deu IMPAR! Você VENCEU!')
        vitorias+=1