# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

n1 = float(input('PRIMEIRA NOTA: '))
n2 = float(input('SEGUNDA NOTA: '))

m = (n1 + n2)/2

if m > 9 and m <= 10:
    print('CONCEITO: A - APROVADO')
elif m > 7.5 and m <= 9:
    print('CONCEITO: B - APROVADO')
elif m > 6 and m <= 7.5:
    print('CONCEITO: C - APROVADO')
elif m > 4 and m <= 6:
    print('CONCEITO: D - REPROVADO')
elif m <= 4:
    print('CONCEITO: E - REPROVADO')