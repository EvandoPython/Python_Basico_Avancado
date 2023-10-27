import copy

produtos = [
    {'nome': 'Produto 5','preco': 10.00},
    {'nome': 'Produto 1','preco': 22.32},
    {'nome': 'Produto 3','preco': 10.11},
    {'nome': 'Produto 2','preco': 105.7},
    {'nome': 'Produto 4','preco': 69.90},
  
]
novos_produtos = copy.deepcopy(produtos)

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')

produtos_ordenados_por_nome = sorted(
    produtos,
    key=lambda p: p['nome']
)

