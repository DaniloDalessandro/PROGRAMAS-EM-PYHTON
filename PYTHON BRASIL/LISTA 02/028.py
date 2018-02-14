# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

tipo = input('QUAL TIPO DE CARNE: ')
qtd = int(input('QUANTOS KILOS DE CARNE: '))
cartao = input('CARTÃO: ')

if tipo == 'file' and qtd <= 5:
    preco = qtd * 4.90
    if cartao == 'sim':
        preco = preco - (preco * 0.05)
        print(preco)
    else:
        print(preco)
elif tipo == 'file' and qtd > 5:
    preco = qtd * 5.80
    if cartao == 'sim':
        preco = preco - (preco * 0.05)
        print(preco)
    else:
        print(preco)
elif tipo == 'alcatra' and qtd <= 5:
    preco = qtd * 5.90
    if cartao == 'sim':
        preco = preco - (preco * 0.05)
        print(preco)
    else:
        print(preco)
elif tipo == 'alcatra' and qtd > 5:
    preco = qtd * 6.80
    if cartao == 'sim':
        preco = preco - (preco * 0.05)
        print(preco)
    else:
        print(preco)
elif tipo == 'picanha' and qtd <= 5:
    preco = qtd * 6.90
    if cartao == 'sim':
        preco = preco - (preco * 0.05)
        print(preco)
    else:
        print(preco)
elif tipo == 'picanha' and qtd > 5:
    preco = qtd * 7.80
    if cartao == 'sim':
        preco = preco - (preco * 0.05)
        print(preco)
    else:
        print(preco)


