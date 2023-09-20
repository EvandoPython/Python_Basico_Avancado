
entrada = input("Digite a hora numeros inteiros: ")

try:
    hora = int(entrada)
    if hora >= 0 and hora <= 11:
        print("Bom dia")
        
    elif hora >=12 and hora <17:
        print("Boa tarde")
    elif hora >=1 and hora <= 23:
        print("Boa noite")
    else:
        print("Noão conheço essa hora ")        
        
    
except:
    print("Digite apenas numeros inteiros ")        
       
    
           
 
     
    