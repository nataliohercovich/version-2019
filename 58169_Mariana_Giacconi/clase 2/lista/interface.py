from list_of_numbers import find_max

def input_list_numbers():
    listNums=[]
    print('ingrese 4 numeros para la lista:')
    for x in range(0,4):
        listNums.append(input('numero' + str(x)+':'))
    return listNums

def list_of_numbers_interface(data):
    print(find_max(data))

def main():
    a=input_list_numbers()
    list_of_numbers_interface(a)


"""run"""
main()