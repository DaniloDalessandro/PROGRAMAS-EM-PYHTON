# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

data = input('DIGITE UMA DATA NO FORMATO AA/BB/CCCC: ')

if len(data) < 8:
    print('DATA INVALIDA!')
elif data[2] != '/' and data[5] != '/':
    print('DATA INVALIDA: COLOQUE (/)')

dataseparada = data.split('/')

if int(dataseparada[0]) > 31 and int(dataseparada[0]) > 1:
    print('DATA INVALIDA 3')
elif int(dataseparada[1]) > 12 and int(dataseparada[1]) > 1:
    print('DATA INVALIDA 4')
elif int(dataseparada[1]) == 2 and int(dataseparada[0]) > 28:
    print('DATA INAVALIDA')
elif int(dataseparada[1]) == 4 and int(dataseparada[0]) == 31:
    print('DATA INAVALIDA')
elif int(dataseparada[1]) == 6 and int(dataseparada[0]) == 31:
    print('DATA INAVALIDA')
elif int(dataseparada[1]) == 9 and int(dataseparada[0]) == 31:
    print('DATA INAVALIDA')
elif int(dataseparada[1]) == 11 and int(dataseparada[0]) == 31:
    print('DATA INAVALIDA')
else:
    print('DATA VALIDA')



