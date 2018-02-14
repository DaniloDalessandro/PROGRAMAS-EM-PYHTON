# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

salariohora = float(input('QUANTO VC GANHA POR HORA? '))
numdias = int(input('QUANTAS HORAS TRABALHA NO MES? '))

salariobruto = salariohora*numdias
print('SALARIO BRUTO: {}'.format(salariobruto))

inss = (8/100)*salariobruto
print('INSS: {}'.format(inss))

sindi = (5/100)*salariobruto
print('SINDICATO: {}'.format(sindi))

ir = (11/100)*salariobruto
print('INPOSTO DE RENDA: {}'.format(ir))

sliquido = salariobruto - ir - sindi - inss
print('SALARIO LIQUIDO: {}'.format(sliquido))