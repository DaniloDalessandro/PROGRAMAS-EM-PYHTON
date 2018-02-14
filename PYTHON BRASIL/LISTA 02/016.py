# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

import sys
from math import sqrt

a = int(input(' VALOR DE A: '))
if a == 0:
    print('A EQUAÇÃO NÃO É DO SEGUNDO GRAU.')
    sys.exit('PROGRAMA ENCERRADO')
b = int(input(' VALOR DE B: '))
c = int(input(' VALOR DE C: '))

delta = b ** 2 - 4 * a * c

if delta <= -1:
    print('EQUAÇÃO NÃO POSSUI RAIZES REIAS')
    sys.exit('PROGRAMA ENCERRADO')

if delta == 0:
    print('EQUAÇÃO POSSUI UMA RAIZ REAL')
    r1 = (-b + sqrt(delta))/2*a
    print(r1)

if delta != 0:
    r1 = (-b + sqrt(delta))/2*a
    print(r1)
    r2 = (-b - sqrt(delta))/2*a
    print(r2)
