from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError
CMC_PRO_API_KEY = 'b85fb01e-f258-44cf-87aa-49bc91643c7c'
cmc = CoinMarketCapAPI(CMC_PRO_API_KEY)
r = cmc. cryptocurrency_quotes_latest(symbol='BTC')

print(r.data['k'])