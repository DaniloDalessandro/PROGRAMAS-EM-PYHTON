# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

p = []

p1 = p.append(input('TELEFONOU PARA VITIMA? '))
p2 = p.append(input('ESTEVE NO LOCAL DO CRIME? '))
p3 = p.append(input('MORA PERTO DA VITIMA? '))
p4 = p.append(input('JA TRABALHOU COM A VITIMA? '))
p5 = p.append(input('DEVIA A VITIMA? '))

tot = 0

for sim in p:
    tot = int(p.count('sim'))

print(tot)
if tot == 2:
    print('SUSPEITA!')
elif tot == 3 or tot == 4:
    print('CUMPLICE')
elif tot == 5:
    print('ASSASINO')
else:
    print('INOCENTE')
