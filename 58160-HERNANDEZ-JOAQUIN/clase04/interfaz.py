from hexa_to_decimal import hexadecimal_to_decimal
def Hexa_interfaz (decimal_number):

    if not decimal_number:
        return ('Error1')
        

    try:
        numero = str(decimal_number)
        return hexa_to_decimal(numero)

    except:
        return('Error2')
        
    
    

def main():
    decimal_number = input('Ingrese un numero: ')
    result = Hexa_interfaz(decimal_number)
    print(result)
main()
