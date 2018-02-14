# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

n = input('QUAL VALOR DESEJA SACAR: ')

if int(n) < 100 or int(n) > 600:
    print('VALOR NÃO PERMITIDO')

n50 = 0
n10 = 0
n5 = 0
n1 = 0

n100 = n[0]
if n[1] == '5':
    n50 = 1
elif int(n[1]) >= 6:
    n50 = 1
    n10 = int(n[1]) - 5
elif int(n[1]) < 5:
    n10 = n[1]

if int(n[2]) == 5:
    n5 = 1
elif int(n[2]) >= 6:
    n5 = 1
    n1 = int(n[2]) - 5
elif int(n[2]) < 5:
    n1 = n[2]

if int(n100) > 0:
    print('{} NOTAS DE 100'.format(n100))
if n50 > 0:
    print('{} NOTAS DE 50'.format(n50))
if n10 > 0:
    print('{} NOTAS DE 10'.format(n10))
if n5 > 0:
    print('{} NOTAS DE 5'.format(n5))
if n1 > 0:
    print('{} NOTAS DE 1'.format(n1))


























