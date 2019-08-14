def main():
  x = 0
  y = 0
  while x == 0:
    opcion = input("Ingrese:\n1 - Para adivinar el numero de la maquina\n2 - Para que la maquina adivine tu numero)
    if opcion == "1":
      juego = HumanAgainstComputerGame()
      intento = 0
      while juego.is_playing == True:
        y = 0
        intento = intento + 1
        while y == 0:
          numero_adivinado = input("\nTrata de adivinar mi numero: ")
          if adv.isnumeric() == True:
            num = int(numero_adivinado)
            if num_adv < 101 and num_adv > 0:
              juego.play(num_adv)
              y = 1
            else:
              print("\nDebe ingresar un numero de 2 cifras que vaya del 1 al 100")
          else:
            print("\nDebe ingresar un numero de 2 cifras que vaya del 1 al 100")
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
          respuesta = input("\nCual es tu respuesta?: \nseleccione:\n+ = si es que su numero es mas grande\n- = si es que su numero es mas chico\n= : si los numeros coinciden")
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