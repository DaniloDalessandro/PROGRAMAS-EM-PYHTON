# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

a = int(input('POPULAÇÃO DO PAIS A:'))
ta = float(input('TAXA DE CRESCIMENTO DO PAIS A:'))
b = int(input('POPULAÇÃO DO PAIS B'))
tb = float(input('TAXA DE CRESCIMENTO DO PAIS B'))
anos  = 0

if a > b:
    print('POPULAÇÃO DO PAIS A JA É MAIS DO QUE A DO PAIS B.')

while a < b:
    a = a + (a * (ta/100))
    b = b + (b * (tb/ 100))
    anos = anos + 1

print('{} anos'.format(anos))