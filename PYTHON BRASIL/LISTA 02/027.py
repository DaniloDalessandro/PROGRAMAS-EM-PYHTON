# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

k1 = int(input('QUANTOS KILOS DE MORANGO: '))
k2 = int(input('QUANTOS KILOS DE MAÇA: '))

if k1 <= 5:
    total = k1 * 2.50
    print('PREÇO DO MORANGO: {}'.format(total))
elif k1 > 5:
    total = k1 * 2.20
    print('PREÇO DO MORANGO: {}'.format(total))

if k2 <= 5:
    total2 = k2 * 1.80
    print('PREÇO DA MAÇA: {}'.format(total2))
elif k2 > 5:
    total2 = k2 * 1.50
    print('PREÇO DA MAÇA: {}'.format(total2))

ktotal = k1 + k2
ctotal = total + total2

if ktotal >= 8 or ctotal >= 25:
    ctotal = ctotal - (ctotal * (10/100))
    print('PREÇO COM DESCONTO: {}'. format(ctotal))
