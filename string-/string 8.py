lista = []
qt = []

txt = input('texto: ').split()


for palavra in txt:
    if palavra not in lista:
        lista.append(palavra)
        qt.append(1)
    else:
        index = lista.index(palavra)
        qt[index] += 1

for i in range(len(lista)):
    print(lista[i], qt[i])
        
        

