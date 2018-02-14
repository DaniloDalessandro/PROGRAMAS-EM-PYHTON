# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

n1 = float(input('DIGITE A PRIMEIRA NOTA: '))
n2 = float(input('DIGITE A SEGUNDA NOTA: '))
n3 = float(input('DIGITE A TERCEIRA NOTA: '))

m = (n1 + n2 + n3)/3

if m >= 7 and m < 9.9:
    print('APROVADO')
elif m < 7:
    print('REPROVADO')
elif m == 10:
    print('APROVADO COM DISTINÇÃO')
