# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

n = int(input('DIGITE UM NUMERO: '))

if (n % 4) == 0 and n % 100 != 0 or n % 400 == 0:
    print('ANO É BISSEXTO')
else:
    print('ANO NÃO É BISSEXTO')





