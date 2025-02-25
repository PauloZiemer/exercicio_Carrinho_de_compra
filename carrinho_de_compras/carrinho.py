def carrinho_de_Mercado():
    quantidade_Itens = int(input("Quantidade de itens: "))
    valor_Total = 0

    for n in range(quantidade_Itens):
        itens = float(input("Valor do item: "))
        valor_Total +=itens

    print(f"O total da compra é de R${valor_Total:.2f}.")

carrinho_de_Mercado()