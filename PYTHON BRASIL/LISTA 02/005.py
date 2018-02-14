# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

n1 = int(input('PRIMEIRA NOTA: '))
n2 = int(input('SEGUNDA NOTA: '))

m = (n1 + n2)/2

if m >= 7 and m != 10:
    print('APROVADO')
elif m < 7:
    print('REPROVADO')
elif m == 10:
    print('APROVADO COM DISTINÇÃO')