numPedidos = int(input())

for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    ehVegano = input()

    #TODO: Tendo em vista a variável booleana "ehVegano", imprima a saída deste desafio.
    if ehVegano == 's':
      ehVegano = 'Vegano'
    else:
      ehVegano = 'Nao-vegano'
    print(f'Pedido {i}: {prato} ({ehVegano}) - {calorias} calorias')