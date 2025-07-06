txt = input('digite seu texto: ')
qt = 0
for i in range(len(txt)):
    
    if ( (txt[i]) >= 'a' and (txt[i]) <= 'z' ):
        qt += 1
        if qt > 0:
            print('O texto contém letras minúculas')

            
if qt == 0:
    print('O texto contém apenas letras maiusculas')






        
        
        
           

    

