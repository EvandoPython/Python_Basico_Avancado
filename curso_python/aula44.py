
texto = 'Evando'
interatador = iter(texto)

while True:
    try:
        print(next(interatador))
    except StopIteration:
        break    