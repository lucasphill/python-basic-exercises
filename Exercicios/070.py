total=float(0)
produtos_mais_1000=contador=preco_produto_mais_barato=0
continuar=' '
while True:
    nome=str(input('Nome do produto: '))
    preco=float(input('Preco do produto: '))

    if contador == 0:
        produto_mais_barato = nome
        preco_produto_mais_barato = preco
    
    if preco < preco_produto_mais_barato:
        preco_produto_mais_barato = preco

    if preco > 1000:
        produtos_mais_1000+=1

    total = preco+total
    contador+=1
    while continuar not in 'SN':
        continuar=str(input('Deseja continuar (S/N)? ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'Valor total da compra: {total}')
print(f'Quantidade de produtos mais caros que 1000: {produtos_mais_1000}')
print(f'O nome do produto mais barato é {produto_mais_barato} e custou {preco_produto_mais_barato}')
print(f'Quantidade de produtos registrados: {contador}')