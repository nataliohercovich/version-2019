def hexa_to_decimal(hexa_digito):
    if hexa_digito.isdecimal():
       dec = int(hexa_digito)

    if hexa_digito.isalpha():
       if hexa_digito == 'A':
           dec = 10
       elif hexa_digito == 'B':
           dec = 11
       elif hexa_digito == 'C':
           dec = 12
       elif hexa_digito == 'D':
           dec = 13
       elif hexa_digito == 'E':
           dec = 14
       elif hexa_digito == 'F':
           dec = 15
       else:
           dec = 0
    return dec

def hexadecimal_to_decimal(hexadec):
    dec = 0
    decimal_number = 0
    n = 0
    hexadec = hexadec[::-1]
    count = len(hexadec)
    for n in range(count):
       dec = hexa_to_decimal(hexadec[n])
       decimal_number += dec*pow(16,n)

    return str(decimal_number)