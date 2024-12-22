frase=str(input('Digite uma frase: ')).upper().replace(' ','')
inverso=''
for letra in range(len(frase)-1,-1,-1):
    inverso+=frase[letra]
    # print(inverso)

if inverso == frase:
    print('Sua frase é um PALINDROMO')
else:
    print('Sua frase NÃO É um palindromo')