
    
"""nome ='evando'

print(nome[2])
print(nome[-4])
print('o' in nome)
print('p' in nome)"""

nome = input('Digite um nome: ')
encontrar = input('Digite o que dejesa encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')   
    
    
        