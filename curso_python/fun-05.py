def par_impar(numero):
    mult_2 =  numero % 2 ==0
    
    if mult_2:
        return f'{numero} é par'
    return f'{numero} é impar'

print(par_impar(2))
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))

       