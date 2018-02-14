# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

l = int(input('QUANTOS LITROS DE COMBUSTIVEL: '))
t = input('QUAL TIPO DE COMBUSTIVEL: ')

if l <= 20 and t == 'a':
    total = l * 1.90
    preco = total - (total * (3/100))
    print(preco)
elif l > 20 and t == 'a':
    total = l * 1.90
    preco = total - (total * (5 / 100))
    print(preco)

if l <= 20 and t == 'g':
    total = l * 2.50
    preco = total - (total * (4/100))
    print(preco)
elif l > 20 and t == 'g':
    total = l * 1.90
    preco = total - (total * (6 / 100))
    print(preco)