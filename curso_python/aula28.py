nome = input("Digite seu Nome: ")
idade = input("Digite sua Idade: ")

if nome and idade:
    print(f' Seu nome é {nome}') 
    print(f' Seu nome invertido é {nome[::-1]}')    
     
    if ' ' in nome:
        print(f' Seu nome contem espaços')  
    else:
        print(f' Seu nome não contem espaços') 
     
    print(f'Seu nome é tem {len(nome)}')    
    print(f'A primeira letra do seu nome é {nome[0]}')    
    print(f'A ultima letra do seu nome é {nome[-1]}')      
  

else:
    print('Desculpa. voce deixou campos vazios')

