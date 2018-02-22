# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

n = int(input('DIGITE O NUMERO DE ITENS: '))

num = []

for i in range(n):
    item = int(input('DIGITE UM NUMERO: '))
    num.append(item)

print(sum(num))
print(max(num))
print(min(num))
