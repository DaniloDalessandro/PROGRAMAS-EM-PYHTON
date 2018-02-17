# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

nome = input('DIGITE UM NOME: ')
tam = len(nome)

while tam < 3:
    nome = input('DIGITE UM NOME: ')
    tam = len(nome)

idade = int(input('DIGITE A IDADE: '))

while idade < 0 or idade > 150:
    idade = int(input('DIGITE A IDADE: '))

salario = int(input('DIGITE O SALARIO: '))

while salario < 0:
    salario = int(input('DIGITE O SALARIO: '))

sexo = input('DIGITE O SEXO: ')

while sexo != 'm' and sexo != 'f':
    sexo = input('DIGITE O SEXO: ')

ec = input('DIGITE SEU ESTADO CIVIL: ')

while ec != 's' and ec != 'c' and ec != 'v' and ec != 'd':
    ec = input('DIGITE SEU ESTADO CIVIL: ')



