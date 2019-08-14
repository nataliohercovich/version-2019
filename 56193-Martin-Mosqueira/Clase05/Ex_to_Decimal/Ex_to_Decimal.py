def Hex(number):
    number = number[::-1].upper()
    num = 0

    for x, y in enumerate(number):
        if number[x] < '0':
            num = num - num
        if number[x] > '0' and number[x] <= '9':
            num = num + 16 ** x * int(number[x])
        if number[x] == 'A':
            num = num + 16 ** x * 10
        if number[x] == 'B':
            num = num + 16 ** x * 11
        if number[x] == 'C':
            num = num + 16 ** x * 12
        if number[x] == 'D':
            num = num + 16 ** x * 13
        if number[x] == "E":
            num = num + 16 ** x * 14
        if number[x] == "F":
            num = num + 16 ** x * 15

    return (num)