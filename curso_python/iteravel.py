import sys

iterable = ['Eu','Tenho','__iter__']
iterator = iter(iterable)

generator = ( n for n in range(100))
print(sys.getsizeof(generator))


 
  
 