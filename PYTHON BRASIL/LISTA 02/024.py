# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

n1 = float(input('DIGITE O PRIMEIRO NUMERO: '))
n2 = float(input('DIGITE O SEGUNDO NUMERO: '))

op = int(input('DIGITE UMA OPERAÇÃO: '))

print('(1) - PARA SOMA.')
print('(2) - PARA SUBTRAÇÃO.')
print('(3) - PARA MULTIPLICAÇÃO.')
print('(4) - PARA DIVISÃO.')

if op == 1:
    resp = n1 + n2
elif op == 2:
    resp = n1 - n2
elif op == 3:
    resp = n1 * n2
elif op == 4:
    resp = n1 / n2

print(resp)

if resp % 2 == 0:
    print('NUMERO PAR')
else:
    print('NUMERO IMPAR')

if resp == int(resp):
    print('NUMERO INTEIRO')
else:
    print('NUMERO DECIMAL')

if resp > 0:
    print('NUMERO POSITIVO')
else:
    print('NUMERO NEGATIVO')


