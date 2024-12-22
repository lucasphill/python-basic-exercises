soma=0
quantidade=0
for i in range(0,500):
    if i%2!=0:
        if i%3==0:
            soma=i+soma
            quantidade+=1
            # print(i)

print(f'A soma dos {quantidade} é de {soma}')