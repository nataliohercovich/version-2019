from hexa_to_deci import hexa_to_deci
def interfaz_hexa_to_deci(num):
    dicto= {'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
    if not num:
        return 'Por favor, ingrese un numero'
    try:
        if int(num)<0:
            return 'Ingresar un numero hexadecimal positivo'
        else:     
            return hexa_to_deci(num)
    except:
        for i in num:
            if not i in dicto:
                try:
                    int(i)
                except:
                    return 'Debe ingresar un numero hexadecimal positivo'
    return hexa_to_deci(num)