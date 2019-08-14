def count_letters(palabra)
    for letter in palabra:
        if letter in dic_mio:
            dic_mio[letter]+=1
        else:
            dic_mio[letter]=1 

    return dic_mio