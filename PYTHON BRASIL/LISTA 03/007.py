# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

num = []
tam = len(num)

while tam < 5:
    item = int(input('DIGITE UM NUMERO: '))
    num.append(item)
    tam = len(num)

maior = max(num)
print(maior)
