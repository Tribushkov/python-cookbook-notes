prices = {
       'ACME': 45.23,
       'AAPL': 612.78,
       'IBM': 205.55,
       'HPQ': 37.20,
       'FB': 10.75
}

max_price = max(zip(prices.values(), prices.keys()))
print max_price  # (612.78, 'AAPL')

prices_sorted = sorted(zip(prices.values(), prices.keys()))
