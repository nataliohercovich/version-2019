from maquina_cafe import Cafe
from maquina_cafe import CafeChico
from maquina_cafe import CafePremium


# si coloco ¿ en las preguntas salta error Unicode

def tipo(coin):
    coin = int(coin)
    if coin == 1:
        bebida = CafeChico()
        dulce = input ("Desea colocarle azucar? ")  #la maquina solo tiene si o no que envia un 1 o un 0
        if dulce == 'si':
            bebida.cafe_con_azucar(1)
            print('Su cafe chico dulce esta listo')
            return ('Su cafe chico dulce esta listo')

        if dulce == 'no':
            bebida.cafe_con_azucar(0)
            print('Su cafe chico amargo esta listo')
            return ('Su cafe chico amargo esta listo')
    
    if coin == 2:
        bebida = CafePremium()
        
        dulce = input ("Cuantos gramos de azucar desea colocarle? ") #solo hay 6 botones, del 0 al 5
        bebida.cafe_con_azucar(dulce)

        leche = input ("Desea cafe con leche? ")  #solo hay dos botones si o no
        if leche == 'si':
            bebida.cafe_con_leche(1)
            print('Su cafe premium con leche esta listo')
            return ('Su cafe premium con leche esta listo')
        if leche == 'no':
            bebida.cafe_con_leche(0)
            print('Su cafe premium esta listo')
            return ('Su cafe premium esta listo')

            



def main():
    coin = input ("Ingrese 1 moneda para cafe chico o 2 para premium  ")
    tipo(coin)


main()