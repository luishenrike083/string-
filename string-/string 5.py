letras = []

texto = input('digite o texto : ')
for i in range(len(texto)):
    print(texto[i])
    if texto[i] not in letras :
        letras.append(texto[i])

print('AS LETRAS QUE FAZEM PARTE DO TEXTO SAO',letras)
