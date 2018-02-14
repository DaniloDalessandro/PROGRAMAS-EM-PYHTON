# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

h = float(input('QUANTAS HORAS TRABALHA NO MÊS: '))
v = float(input('QUAL O VALOR DE SUA HORA: '))

sbruto = h * v

print('SALARIO BRUTO: {}'.format(sbruto))

if sbruto <= 900:
    ir = 0
    print('ISENTO')
elif sbruto > 900 and sbruto <= 1500:
    ir = sbruto * (5 / 100)
    print('IR: {} '.format(ir))
elif sbruto <= 1500 and sbruto > 2500:
    ir = sbruto * (10 / 100)
    print('IR: {}'.format(ir))
elif sbruto >= 2500:
    ir = sbruto * (20 / 100)
    print('IR: {}'.format(ir))

ir = ir + 0
inss = sbruto * (10/100)
fgts = sbruto * (11/100)
sind = sbruto * (3/100)
totdes = sind + inss + ir
sliquido = sbruto - sind - inss - ir

print('INSS: {}'.format(inss))

print('FGTS: {}'.format(fgts))

print('TOTAL DE DESCONTOS: {}'.format(totdes))

print('SALARIO LIQUIDO: {}'.format(sliquido))



