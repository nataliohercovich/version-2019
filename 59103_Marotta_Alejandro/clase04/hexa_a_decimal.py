
def obtener_caracter(caracter): #cada caracter tiene el mismo valor que su posicion
    c =['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for x in range (len(c)):
        if caracter == c[x]:
            return x



def hexa_decimal (hexa):
    
    decimal = 0
    
    potencia = len(hexa)-1 #ya que si por ejemplo son 4 num la potencia max es de 3
    for letter in hexa:
        decimal = decimal + 16 ** potencia * obtener_caracter(letter)
        potencia -=1
        
    return decimal
    


