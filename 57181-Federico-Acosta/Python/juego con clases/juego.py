from gng import ComputerAgainstHumanGame, HumanAgainstComputerGame

def main():
  x = 0
  y = 0
  while x == 0:
    opcion = input("\nPara adivinar el numero de la maquina ingresa '1'\nPara que la maquina adivine tu numero ingresa '2': ")
    if opcion == "1":
      juego = HumanAgainstComputerGame()
      intento = 0
      while juego.is_playing == True:
        y = 0
        intento = intento + 1
        while y == 0:
          adv = input("\nTrata de adivinar mi numero: ")
          if adv.isnumeric() == True:
            adv_int = int(adv)
            if adv_int < 101 and adv_int > 0:
              juego.play(adv_int)
              y = 1
            else:
              print("\nEl numero debe ser entre 1 y 100")
          else:
            print("\nDebe ingresar solo un numero entre 1 y 100")
      print(f"Ganaste en {intento} intentos")
      x = 1          
    elif opcion == "2":
      intento = 0
      juego = ComputerAgainstHumanGame()
      while juego.is_playing == True:
        intento = intento + 1
        print(juego.input_text)
        y = 0
        while y == 0:
          respuesta = input("\nCual es tu respuesta?: ")
          if respuesta != "+" and respuesta != "-" and respuesta != "=":
            print("Responda solo con '+' , '-' , o '='")
          else:
            y = 1
        juego.play(respuesta)
      print(f"\nLa maquina gano en {intento} intentos")
      x = 1
    else:
      print("\nDebe ingresar solo '1' o '2'")




main()