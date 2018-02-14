# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO


arquivo = float(input('TAMANHO DO ARQUIVO EM MB: '))
velocidade = float(input('VELOCIDADE DE DOWN EM Mbps: '))

taprox = float(arquivo/velocidade)

minu = float(taprox/60)

print('TEMPO: {} MINUTOS'.format(minu))
