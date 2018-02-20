# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

n1 = 0
n2 = 1
n3 = 0
print(n1)
print(n2)

while True:
    n3 = n2 + n1
    n1 = n2
    n2 = n3
    print('{}'.format(n3))
