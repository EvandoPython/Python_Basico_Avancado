
def mult(*args):
    total = 1
    for numero in args:
        total *= numero
    
    return total    


result = mult(1,2,5,7)

print(result)

       