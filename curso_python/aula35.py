
nome = input("Digite um nome: ")
var = len(nome)

if var <=4:
    print("Seu nome é curto")
elif var >= 5 and var <= 6:
    print("Normal")
else:
    print("Seu nome é muito grande")
print(f"Seu nome tem {var} letras")    

