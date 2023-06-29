
'''
//TODO: Calcular o preço final do pedido (total dos hambúrgueres + total das bebidas).

//TODO: Calcular o troco do pedido, considerando o preço final e o valor pago pelo usuário.

//TODO: Imprimir a saída no formato especificado neste desafio.]
'''

valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())

valor_tot_hamburger = valorHamburguer * quantidadeHamburguer
valor_tot_bebidas = valorBebida * quantidadeBebida
troco = valorPago - (valor_tot_hamburger + valor_tot_bebidas)

print(f'O preço final do pedido é R$ {(valor_tot_hamburger + valor_tot_bebidas):.2f}. Seu troco é R$ {troco:.2f}.')