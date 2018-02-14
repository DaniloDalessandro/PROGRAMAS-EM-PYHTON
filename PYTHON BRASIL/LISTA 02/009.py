# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

lista = []

for i in range(3):
    x = int(input('NUMERO: '))
    lista.append(x)

lista.sort(reverse=True)

print(lista)

