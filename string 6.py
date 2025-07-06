while True:
    num = input('Número: ')
    valido = True
    for s in num:
        if(s < '0') or (s > '9'):
            valido = False
            break
    if (valido == True):
        break


print('Numero', num)
