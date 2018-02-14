# POR: DANILO COSTA
# UNIVERSIDADE ESTADUAL DO MARANHÃO
# GRADUANDO EM ENGENHARIA DE COMPUTAÇÃO

# FUNÇÃO QUE CONVERTE DECIMAL PARA BINARIO
def decimalparabinario(n):
    binario = ""
    while(True):
        binario = binario + str(n%2)
        n = n//2
        if n == 0:
            break
    binario = binario[::-1]
    binario = int(binario)
    print('EM BINARIO: {}'.format(binario))
    return binario

# FUNÇÃO QUE CONVERTE DECIMAL PARA OCTAL
def decimalparaoctal(n):
    octal = ""
    while(True):
        octal = octal + str(n%8)
        n = n//8
        if n == 0:
            break
    octal = octal[::-1]
    octal = int(octal)
    print('EM OCTAL: {}'.format(octal))
    return octal

# FUNÇÃO QUE CONVERTE BINARIO PARA DECIMAL
def binarioparadecimal(n):
    decimal = 0
    n = str(n)
    n = n[::-1]
    tam = len(n)
    for i in range(tam):
        if n[i] == "1":
            decimal = decimal + 2**i
    print('EM DECIMAL: {}'.format (decimal))
    return decimal

# FUNÇÃO QUE CONVERTE DECIMAL PARA HEXADECIMAL
def decimalparahexa(n):
    numeros = list("0123456789ABCDEF")
    hexa = ""
    while (True):
        hexa = hexa + numeros[n % 16]
        n = n // 16
        if n == 0:
            break
    hexa = hexa[::-1]
    hexa = str(hexa)
    print('EM HEXADECIMAL: {}'.format(hexa))
    return hexa

# FUNÇÃO QUE CONVERTE BINARIO PARA OCTAL
def binarioparaoctal(n):
    decimal = 0
    n = str(n)
    n = n[::-1]
    tam = len(n)
    for i in range(tam):
        if n[i] == "1":
            decimal = decimal + 2**i

    return decimalparaoctal(decimal)

# FUNÇÃO QUE CONVERTE BINARIO PARA HEXADECIMAL
def binarioparahexa(n):
    decimal = 0
    n = str(n)
    n = n[::-1]
    tam = len(n)
    for i in range(tam):
        if n[i] == "1":
            decimal = decimal + 2**i

    return decimalparahexa(decimal)

# FUNÇÃO QUE CONVERTE OCTAL PARA DECIMAL
def octalparadecimal(n):
    num = 0
    p = 0
    while (n > 0):
        num += 8 ** p * (n % 10)
        n //= 10
        p += 1
    print('EM DECIMAL: {}'.format(num))
    return num

# FUNÇÃO QUE CONVERTE OCTAL PARA BINARIO
def octalparabinario(n):
    num = 0
    p = 0
    while (n > 0):
        num += 8 ** p * (n % 10)
        n //= 10
        p += 1
    return decimalparabinario(num)

# FUNÇÃO QUE CONVERTE OCTAL PARA HEXADECIMAL
def octalparahexa(n):
    num = 0
    p = 0
    while (n > 0):
        num += 8 ** p * (n % 10)
        n //= 10
        p += 1
    return decimalparahexa(num)

# FUNÇÃO QUE IMPRIME LETRAS NOS RESULTADOS DAS CONVERSOES HEXADECIMAIS
def auxhex(num):
    numeros = ['0', '1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    for i in range(len(numeros)):
        if num == numeros[i]:
            return i

# FUNÇÃO QUE CONVERTE HEXADECIMAL PARA DECIMAL
def hexadecimalparadecimal(n):
    decimal = 0
    p = 0
    for num in range(len(n),0,-1):
        decimal = decimal + 16 ** p * auxhex(n[num - 1])
        p += 1
    print(decimal)

# FUNÇÃO QUE CONVERTE HEXADECIMAL PARA BINARIO
def hexadecimalparabinario(n):
    decimal = 0
    p = 0
    for num in range(len(n),0,-1):
        decimal = decimal + 16 ** p * auxhex(n[num - 1])
        p += 1
    decimalparabinario(decimal)
    return decimal

# FUNÇÃO QUE CONVERTE HEXADECIMAL PARA OCTAL
def hexadecimalparaoctal(n):
    decimal = 0
    p = 0
    for num in range(len(n),0,-1):
        decimal = decimal + 16 ** p * auxhex(n[num - 1])
        p += 1
    decimalparaoctal(decimal)
    return decimal

print('-------------CONVERSÃO DE BASES----------------')
print('[1] - BINARIO P/ DECIMAL.')
print('[2] - DECIMAL P/ BINARIO.')
print('[3] - DECIMAL P/ OCTAL.')
print('[4] - DECIMAL P/ HEXADECIMAL.')
print('[5] - BINARIO P/ OCTAL.')
print('[6] - BINARIO P/ HEXADECIMAL.')
print('[7] - OCTAL P/ DECIMAL.')
print('[8] - OCTAL P/ BINARIO.')
print('[9] - OCTAL P/ HEXADECIMAL.')
print('[10] - HEXADECIMAL P/ DECIMAL.')
print('[11] - HEXADECIMAL P/ BINARIO.')
print('[12] - HEXADECIMAL P/ OCTAL.')

op = int(input('ESCOLHA UMA OPÇÃO: '))


if op == 1:
    n = int(input('DIGITE UM NUMERO: '))
    binarioparadecimal(n)
if op == 2:
    n = int(input('DIGITE UM NUMERO: '))
    decimalparabinario(n)
if op == 3:
    n = int(input('DIGITE UM NUMERO: '))
    decimalparaoctal(n)
if op == 4:
    n = int(input('DIGITE UM NUMERO: '))
    decimalparahexa(n)
if op == 5:
    n = int(input('DIGITE UM NUMERO: '))
    binarioparaoctal(n)
if op == 6:
    n = int(input('DIGITE UM NUMERO: '))
    binarioparahexa(n)
if op == 7:
    n = int(input('DIGITE UM NUMERO: '))
    octalparadecimal(n)
if op == 8:
    n = int(input('DIGITE UM NUMERO: '))
    octalparabinario(n)
if op == 9:
    n = int(input('DIGITE UM NUMERO: '))
    octalparahexa(n)
if op == 10:
    n = input('DIGITE UM NUMERO: ')
    hexadecimalparadecimal(n)
if op == 11:
    n = input('DIGITE UM NUMERO: ')
    hexadecimalparabinario(n)
if op == 12:
    n = input('DIGITE UM NUMERO: ')
    hexadecimalparaoctal(n)

