import GDAX as gdax

publicClient = gdax.PublicClient(product_id="BTC-EUR")
trade = publicClient.getProductTrades(product="BTC-EUR")

print(trade)



