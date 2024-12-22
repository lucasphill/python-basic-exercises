valor_casa=float(input('Digite o valor da casa: '))
salario=float(input('Digite o salário: '))
tempo=int(input('Digite quanto tempo para pagar em anos: '))

#prestacao não pode exceder 30% do salario mensal

tempo_mes=tempo*12 #meses a pagar
prestacao=valor_casa/tempo_mes #valor por mes
salario_ocupado=salario*0.30 #valor do salario que pode ser gasto com isso

if prestacao >= salario_ocupado:
    print(f'Emprestino NEGADO. Prestações muito altas. Prestação: {prestacao}, salário possivel: {salario_ocupado}')
else:
    print(f'Emprestimo APROVADO. Prestação: {prestacao}, salário possivel: {salario_ocupado}')