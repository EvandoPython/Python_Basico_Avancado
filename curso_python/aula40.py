while True:
    n1 = input('Digite um numero: ')
    n2 = input('Digite outro numero: ')
    operador = input('Digite o Operador: ')
    
    numeros_validos = None    
    
    try:
       num1 = float(n1)
       num2 = float(n2)
       numeros_validos = True  
    except:
       numeros_validos = None
       
       if numeros_validos is None:
           print('Um dos numeros digitado são inválidos')   
           continue    
    operador_permitidos = '+-/*'
    
    if operador not in operador_permitidos:
        print('Operador Invalido')
        continue
    
    
    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)    
    elif operador == '*':
        print(num1 * num2)        
    elif operador == '/':
        print(num1 / num2)        
    
    sair = input("Quer sair [s]im: ").lower().startswith('s')
    
    if sair is True:
        break
    
print(sair)