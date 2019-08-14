def hexa_to_deci(num):
    dicto = {'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
    m=''
    d=0
    for i in num:
        if i in dicto:
            m+= str(int(dicto[i]/8))+str(int(dicto[i]/4)%2)+str((int(dicto[i]/2)%2))+str(dicto[i]%2)
        else:
            m+= str(int(int(i)/8))+str(int(int(i)/4)%2)+str(int(int(i)/2)%2)+str(int(i)%2)
    v = len(m)
    for k in m:
        v-= 1
        d+= int(k)*(2**v)
    return d