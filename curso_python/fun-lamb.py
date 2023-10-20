lista = [
    {'nome': 'Silva','sobrenome': 'Jose'},
     {'nome': 'Luzireno','sobrenome': 'Nobre'},
    
       
]

def ordena(item):
    print(item)
    return item ['nome']

lista.sort(key=lambda item: item['nome'])
for item in lista:
    print(item)       