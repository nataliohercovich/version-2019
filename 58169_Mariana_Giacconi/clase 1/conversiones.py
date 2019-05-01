"""variables globales"""
I = 1
V = 5
X = 10
L = 50
C = 100
AA=''
BB=''
CC=''
numero=0

"""romanos a decimales"""
def unidades_romanas(num):
    if num=='I':
        return I
    if num=='V':
        return V
    if num=='X':
        return X
    if num=='L':
        return L
    if num=='C':
        return C

def romano_a_decimal(R):
    
    largo = len(R)

    if largo==1:
        AA = R[0]
        AAA = unidades_romanas(AA)
        return AAA

    if largo==2:
        AA = R[0]
        BB = R[1]
        AAA = unidades_romanas(AA)
        BBB = unidades_romanas(BB)
        if AAA==BBB:
            numero = AAA+BBB 
            return numero
        if AAA>BBB:
            numero = AAA+BBB
            return numero
        if AAA<BBB:
            numero = BBB-AAA 
            return numero

    if largo==3:
        AA = R[0]
        BB = R[1]
        CC = R[2]
        AAA = unidades_romanas(AA)
        BBB = unidades_romanas(BB)
        CCC = unidades_romanas(CC)
        if BBB==CCC:
            numero = CCC+AAA+BBB 
            return numero
        if BBB>CCC:
            numero = CCC+AAA+BBB
            return numero
        if BBB<CCC:
            numero = CCC+BBB-AAA 
            return numero


"""decimales a romanos"""
def decimal_a_romano(E):
    import math
    Unidad=["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    Decena=["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    Centena=["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    N=int(E)
    u= N % 10
    d=int(math.floor(N/10))%10
    c=int(math.floor(N/100))
    if(N>=100): 
        return Centena[c]+Decena[d]+Unidad[u]
    else:
        if(N>=10):
            return Decena[d]+Unidad[u]
        else:
            return Unidad[N]

            
    

    