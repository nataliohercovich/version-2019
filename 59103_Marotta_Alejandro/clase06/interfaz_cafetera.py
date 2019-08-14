from maquina_cafe import Cafe
from maquina_cafe import CafeChico
from maquina_cafe import CafePremium
from maquina_cafe import Sensor



# si coloco ¿ en las preguntas salta error Unicode

cafecito = CafeChico()  #inicializo valores globales
cafeprem = CafePremium()
sensor = Sensor()

resultado = (cafecito.__dict__) # tanto cafesito y cafeprem tienen los mismo valores entonces solo lo comparo con uno de los dos
agua,cafe,azucar,leche = tuple(resultado.values())
bandera = sensor.controlar(agua,cafe,azucar,leche) #cuando prenda la maquina verificara si las cantidades son validas



def tipo(coin):
    coin = int(coin) 
    global azucar
    global leche
    print()

    if coin == 1:
        if azucar >= 5: #el sensor siempre verifica que haya mas de 5gr para el correcto funconamiento de toda la maquina
            dulce = input ("Desea colocarle azucar? si/no ")  #la maquina solo tiene si o no que envia un 1 o un 0
            if dulce == 'si':
                cafecito.cafe_con_azucar(1)        
                print('Su cafe chico dulce esta listo')
                return (cafecito.__dict__)  #devuelve un diccionario con los atributos y valores del objeto

            if dulce == 'no':
                cafecito.cafe_con_azucar(0)
                print('Su cafe chico amargo esta listo')
                return (cafecito.__dict__)
        else :
            cafecito.cafe_con_azucar(0)
            print('Su cafe chico amargo esta listo')
            return (cafecito.__dict__)
    
    if coin == 2:
                
        if azucar >= 5: #el sensor siempre verifica que haya mas de 5gr para el correcto funconamiento de toda la maquina
            dulce = input ("Cuantos gramos de azucar desea colocarle? ") #solo hay 6 botones, del 0 al 5
            cafeprem.cafe_con_azucar(dulce)
        else:
            print ('Cafe amargo en proceso...')  #esta opcion saldra solo cuando el sensor avise que no hay azucar y el usuario haya puesto que igual lo queria amargo
            cafeprem.cafe_con_azucar(0)

        if leche >= 40:
            cortado = input ("Desea cafe con leche? si/no ")  #solo hay dos botones si o no
            if cortado == 'si':
                cafeprem.cafe_con_leche(1)
                print('Su cafe premium con leche esta listo')
                return (cafeprem.__dict__)
            if cortado == 'no':
                cafeprem.cafe_con_leche(0)
                print('Su cafe premium esta listo')
                return (cafeprem.__dict__)
        else:
            cafeprem.cafe_con_leche(0)
            print('Su cafe premium esta listo')
            return (cafeprem.__dict__)



def comenzar(coin): 
    
    print ()

    global bandera 
    global azucar
    global leche 
    global agua
    global cafe
    global cafeprem
    global cafecito

    while bandera: #usa valores globales y los reescribe verificando los elementos necesarios para el cafe
        
        resultado = tipo(coin)  #tipo devuelve un diccionario --> lo vuelvo una tupla para conseguir los valores

        agua,cafe,azucar,leche = tuple(resultado.values()) #le asigno una variable a cada valor
                

        #Actualizo valores         
        cafeprem.agua = agua
        cafeprem.gramoscafe = cafe
        cafeprem.azucar= azucar
        cafeprem.leche = leche

        cafecito.agua = agua
        cafecito.gramoscafe = cafe
        cafecito.azucar= azucar
        cafecito.leche = leche
              
        print ()
        bandera = sensor.controlar(agua,cafe,azucar,leche) #verifico si tengo suficientes elementos para hacer el cafe

        #si falta algo al siguiente usuario le avisara antes de que ponga la moneda que falta azucar o leche

        if bandera: #si tengo los suficientes elementos lanzo el main
            main()

    


def main():
    print ()
    if bandera:
        coin = input ("Ingrese 1 moneda para cafe chico o 2 para premium  ")
        comenzar(coin)


main()