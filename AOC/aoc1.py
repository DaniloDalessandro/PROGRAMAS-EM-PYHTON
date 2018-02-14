# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

#CODIFICAÇÃO CRIADA POR MIM
alfabeto={'a':'00000','b':'00001','c':'00010', 'd':'00011', 'e':'00100','f':'00101',
'g':'00110','h':'00111','i':'01000','j':'11000','l':'01001', ' ':' ',
'm':'01010','n':'01011','o':'01100','p':'01101','q':'01110','r':'01111','s':'10000',
't': '10001','u':'10010','v':'10011','w':'10100','x':'10101','y':'10110','z':'10111'}

texto = input('DIGITE UM TEXTO: ')

saida=""

for i in texto:
    saida=saida+alfabeto[i]

print('EM BINARIO: {}'.format(saida))
