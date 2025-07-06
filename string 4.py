qt = 0
txt = input('digite seu texto: ')
for i in range(len(txt)):
    if txt[i] == 'a':
        qt += 1
    elif txt[i] == 'e':
        qt+=1
    elif txt[i] =='i':
        qt+=1
    elif txt[i] == 'o':
        qt+=1
    elif txt[i] == 'u':
        qt+=1

print(qt)
