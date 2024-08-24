n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))

media=(n1+n2)/2

if media >= 7:
    print(f'Você foi APROVADO. Média: {media}')
elif 5 <= media < 7:
    print(f'Você está de RECUPERAÇÃO. Média: {media}')
else:
    print(f'Você foi REPROVADO. Média: {media}')