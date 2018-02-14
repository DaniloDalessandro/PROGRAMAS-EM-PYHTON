# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

tamanho = int(input('TAMANHO EM METROS: '))
litros = tamanho / 3

if tamanho % 54 == 0:
	latas = tamanho / 54
else:
	latas = int(tamanho / 54) + 1

preco = latas * 80
print ('latas {}' .format(latas))
print ('R$ {}' .format(preco))