nome=str(input('Digite seu nome completo: ')).strip()
lista=nome.split()
print(f'Seu primeiro nome é: {lista[0]}')
print(f'Seu ultimo nome é: {lista[len(lista)-1]}')