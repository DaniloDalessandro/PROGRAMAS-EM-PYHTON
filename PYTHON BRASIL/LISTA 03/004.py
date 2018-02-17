# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

a = 80
b = 200
anos  = 0

if a > b:
    print('POPULAÇÃO DO PAIS A JA É MAIOR DO QUE A DO PAIS B.')

while a < b:
    a = a + (a * (3/100))
    b = b + (b * (1.5/ 100))
    anos = anos + 1

print('{} anos'.format(anos))