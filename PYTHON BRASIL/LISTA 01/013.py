# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

h = float(input('QUAL SUA ALTURA?'))
s = input('QUAL SEU SEXO?')

if (s == 'f'):
    p = (62.1*h) - 44.7
    if (p > 50) and (p < 60):
      print('PESO IDEAL')
    elif(p < 50):
      print('ABAIXO DO PESO')
    else:
      print('ACIMA DO PESO')

if (s == 'm'):
    p = (72.7*h) - 58
    if (p > 65) and (p < 75):
      print('PESO IDEAL')
    elif(p < 60):
      print('ABAIXO DO PESO')
    else:
      print('ACIMA DO PESO')