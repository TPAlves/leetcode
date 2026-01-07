# Two PTR (Two Pointers): técnica que usa dois índices percorrendo uma estrutura de dados
# para resolver problemas em O(n) tempo. Muito usado em arrays ordenados ou sequências.
# 
# Problema: Best Time to Buy and Sell Stock (LeetCode #121)
# Objetivo: Encontrar o maior lucro comprando e vendendo uma ação uma única vez.
# Estratégia: Manter o menor preço de compra (l) e calcular lucro com cada preço de venda (r).

def maxProfit(prices):
    l, r = 0, 1  # esquerda=comprar, direita=vender
    max_profit = 0

    while r < len(prices):
        # Transação lucrativa
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
        else:
            l = r
        r += 1
    return max_profit


# Exemplo de uso
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # Saída: 5




