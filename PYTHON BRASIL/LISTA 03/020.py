# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO


def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

n = int(input('DIGITE UM NUMERO PARA CALCULO DE FATORIAL: '))

while n > 16:
    print('DIGITE UM NUMERO MAIOR QUE 16')
    n = int(input('DIGITE UM NUMERO PARA CALCULO DE FATORIAL: '))

if n < 16:
    resp = fatorial(n)
    print(resp)

