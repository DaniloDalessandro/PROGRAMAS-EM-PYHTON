# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

l1 = int(input('DIGITE O PRIMEIRO LADO DO TRIANGULO: '))
l2 = int(input('DIGITE O SEGUNDO LADO DO TRIANGULO: '))
l3 = int(input('DIGITE O TERCEIRO LADO DO TRIANGULO: '))

if l1 + l2 > l3:
    print('É UM TRIANGULO.')
elif l1 + l3 > l2:
    print('É UM TRIANGULO.')
elif l2 + l3 > l1:
    print('É UM TRIANGULO.')
else:
    print('NÃO É TRIANGULO.')

if l1 == l2 and l2 == l3:
    print('TRIANGULO IQUILATERO.')
elif l1 == l2 or l1 == l3 or l2 == l3:
    print('TRIANGULO ISOCELES.')
elif l1 != l2 or l1 != l3 or l2 != l3:
    print('TRIANGULO ESCALENO.')