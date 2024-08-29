numeros = ('Zero','Um','Dois','Tres','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez',
           'Onze','Doze','Treze','Catorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')

while True:
    try:
        entrada = int(input('Digite um numero de 0 a 20 para mostrá-lo por extenso: '))
        print(numeros[entrada])
    except:
        print('Numero inválido')
        break
