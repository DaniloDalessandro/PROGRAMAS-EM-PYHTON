# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

n1 = int(input('PRIMEIRO NUMERO: '))
n2 = int(input('SEGUNDO NUMERO: '))
n3 = int(input('TERCEIRO NUMERO: '))

if n1 > n2 and n1 > n3:
    print('{} É O MAIOR NUMERO'.format(n1))
elif n2 > n1 and n2 > n3:
    print('{} É O MAIOR NUMERO'.format(n2))
elif n3 > n1 and n3 > n2:
    print('{} É O MAIOR NUMERO'.format(n3))