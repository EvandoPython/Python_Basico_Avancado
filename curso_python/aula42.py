frase = 'O python é uma linguagem de progtamação foi criada por Guido van Rossum'

i = 0
while i < len(frase):
    letra_atual = frase[i] 
    
    qnt_v_letra_ap = frase.count(letra_atual)
    print(letra_atual,   qnt_v_letra_ap)
    i += 1