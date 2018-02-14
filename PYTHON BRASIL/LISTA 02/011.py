# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

salario = float(input('QUAL SEU SALARIO: '))

if salario < 280:
    print('SALARIO ATUAL : {}'.format(salario))
    print('AUMENTO DE 20%.')
    print('VALOR DO AUMENTO: {}'.format((salario * (20/100))))
    print('SALARIO ATUALIZADO: {}'.format(salario + (salario * (20/100))))
elif salario > 280 and salario < 700:
    print('SALARIO ATUAL : {}'.format(salario))
    print('AUMENTO DE 15%.')
    print('VALOR DO AUMENTO: {}'.format((salario * (15 / 100))))
    print('SALARIO ATUALIZADO: {}'.format(salario + (salario * (15 / 100))))
elif salario > 700 and salario < 1500:
    print('SALARIO ATUAL : {}'.format(salario))
    print('AUMENTO DE 10%.')
    print('VALOR DO AUMENTO: {}'.format((salario * (10 / 100))))
    print('SALARIO ATUALIZADO: {}'.format(salario + (salario * (10 / 100))))
elif salario > 1500:
    print('SALARIO ATUAL : {}'.format(salario))
    print('AUMENTO DE 5%.')
    print('VALOR DO AUMENTO: {}'.format((salario * (5 / 100))))
    print('SALARIO ATUALIZADO: {}'.format(salario + (salario * (5 / 100))))


