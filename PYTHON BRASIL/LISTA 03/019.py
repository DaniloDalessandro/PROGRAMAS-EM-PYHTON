# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

n = int(input('DIGITE O NUMERO DE ITENS: '))

num = []

for i in range(n):
    item = int(input('DIGITE UM NUMERO: '))
    if item > 1000:
        print('VALOR NAO PODE SER MAIOR QUE 1000.')
    else:
        num.append(item)


print(sum(num))
print(max(num))
print(min(num))

