# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

n1 = int(input('DIGITE O PRIMEIRO NUMERO: '))
n2 = int(input('DIGITE O SEGUNDO NUMERO: '))

num = []

while n1 < n2 - 1:
    n1 = n1 + 1
    num.append(n1)

while n1 > n2 + 1:
    n1 = n1 - 1
    num.append(n1)

print(num)