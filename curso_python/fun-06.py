
#def duplicar(numero):
#   return numero *2

#print(duplicar(2))


def criar_mult(mult):
    def multiplicar(numero):
        return numero * mult
    return multiplicar

duplicar = criar_mult(2)
triplicar = criar_mult(3)

print(duplicar(2))
print(triplicar(2))

       