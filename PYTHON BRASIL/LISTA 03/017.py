# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

n = int(input('DIGITE UM NUMERO PARA CALCULO DE FATORIAL: '))

resp = fatorial(n)
print(resp)
