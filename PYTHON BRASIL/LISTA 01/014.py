# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

peso = int(input('QUANTOS DE PEIXE? '))

if (peso <= 50):
    print('SEM MULTA!')
elif(peso > 50):
    m = (peso - 50)*4
    print('MULTA DE {}'.format(m))

