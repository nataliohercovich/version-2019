from cifrado import encrypt

def main():
    text = input("Texto a encriptar: ")
    key = input("clave: ")
    print(isnumber(text, key))

def isnumber(text, key):
    try:
        return encrypt(text,key)
    except:
        return "Debe ingresar solo letras"

main()