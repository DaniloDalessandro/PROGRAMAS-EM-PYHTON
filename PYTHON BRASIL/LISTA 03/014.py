# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

num = []
tam = len(num)

while tam < 10:
    item = int(input('DIGITE UM NUMERO:'))
    num.append(item)
    tam = len(num)

numpar = []
numimpar = []

for i in range(10):
    aux = num[i] % 2
    if aux == 0:
        numpar.append(num[i])
    else:
        numimpar.append(num[i])

print('NUMEROS IMPARES: {}'.format(numimpar))
print('NUMEROS PARES: {}'.format(numpar))


