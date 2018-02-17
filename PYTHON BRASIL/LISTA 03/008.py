# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

num = []
tam = len(num)

while tam < 5:
    item = int(input('DIGITE UM NUMERO: '))
    num.append(item)
    tam = len(num)

soma = sum(num)

print('SOMA: {}'.format(soma))

media = soma/tam

print('MEDIA: {} '.format(media))

