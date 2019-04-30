from hexa_to_decimal import hexa_to_decimal

def main():
    var_number = input("Ingrese un numero en hexadecimal: ")
    print(ishexa(var_number))

def ishexa(var_number):
    try:
        int(var_number,16)
        return hexa_to_decimal(var_number)
    except:
        return "ERROR: debe ingresar un numero hexadecimals"
main()