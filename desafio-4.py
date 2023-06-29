def main():
    n = int(input())

    total = 0

    for i in range(n):
        pedido = input().split()

        if len(pedido) >= 2:
            nome = pedido[0]
            valor = float(pedido[1])
            total += valor
        else:
            print("Formato de pedido inválido. Digite novamente.")

    # Aplicar cupom de desconto
    desconto = input()
    if desconto == "10%":
        total *= 0.9  # Aplica 10% de desconto
    elif desconto == "20%":
        total *= 0.8  # Aplica 20% de desconto

    print(f"Valor total: {total:.2f}")


if __name__ == "__main__":
    main()