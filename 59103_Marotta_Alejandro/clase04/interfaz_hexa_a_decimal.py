from hexa_a_decimal import hexa_decimal

class ValorNoValido(Exception): #creo mi propia excepcion
    pass


def interfaz_hexadecimal (valor):
    try:
        hexadecimal = valor.upper() #por si el usuario escribe en minusculas
        validos ={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,
        '8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15} #creo un diccionario con caracteres validos
        
        for letter in hexadecimal:   
            if letter in validos:
                pass
            else :
                raise ValorNoValido  #si un caracter no esta dentro del diccionario de validos largo una exception
        
        return hexa_decimal(hexadecimal)
        
       
    
    except ValorNoValido:
        print ("---------ERROR----------")
        print ('El valor no es valido')
        print ('\n')
        return False

    except Exception as ex: #por las dudas que se me pase algo
        print ("---------ERROR----------")
        print ("Disculpe,solo acepto numeros hexadecimales positivos")
        print (ex)  #imprimo la excepcion para saber que sucedio
        print ('\n')
        return False #devuelvo valores booleanos para poder compararlos en el test
    





def main():
    hexadecimal = input("Dame un numero Hexadecimal: ") 
    print ('\n')
        
    decimal = interfaz_hexadecimal(hexadecimal)
    
    if decimal != False : #si el valor que me devolvio la funcion es False que no escriba esta linea
        print ("EL valor en decimal es:",decimal)
        print ('\n')

main()
