# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

n = int(input('DIGITE UM NUMERO: '))
if n >= 1000:
    print('DIGITE UM NUMERO MENOR QUE 1000')

num = str(n)
tam = len(num)

if tam == 3:
    centena = num[0]
    dezena = num[1]
    unidade = num[2]
    print('{} centenas, {} dezenas e {} unidades'.format(centena,dezena,unidade))

if tam == 2:
    dezena = num[0]
    unidade = num[1]
    print('{} dezenas e {} unidades'.format(dezena,unidade))

if tam == 1:
    unidade = num[0]
    print('{} unidades'.format(unidade))