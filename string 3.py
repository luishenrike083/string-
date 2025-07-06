txt = input('digite seu texto: ')
for i in range(len(txt)):
    if ((txt[i]) >= 'A') and ((txt[i]) <= 'Z' ):
        print('existe letra maíuscula')
        print(txt[i])
    break

