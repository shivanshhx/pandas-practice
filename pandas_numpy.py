import pandas as pd
import requests

def get_forex_price(currency):
    url = f"https://min-api.cryptocompare.com/data/price?fsym={currency}&tsyms=USD"
    response = requests.get(url)
    data = response.json()
    return data["USD"]



eur_price = get_forex_price("EUR")
gbp_price = get_forex_price("GBP")
jpy_price = get_forex_price("JPY")

def get_price(coin):
    url = f"https://min-api.cryptocompare.com/data/price?fsym={coin}&tsyms=USD"
    response = requests.get(url)
    return response.json()["USD"]

# Fetch live prices
btc = get_price("BTC")
eth = get_price("ETH")

# Put in DataFrame
data = {
    "ASSET": ["BTC", "ETH", "EUR", "GBP", "JPY"],
    "MARKET": ["Crypto", "Crypto", "Forex", "Forex", "Forex"],
    "Price": [btc, eth, eur_price, gbp_price, jpy_price],
    
}

df = pd.DataFrame(data)
print(df)

# Add new columns
crypto_only = df[df["MARKET"] == "Crypto"]
forex_only  = df[df["MARKET"] == "Forex"]
df["Value_1000"] = 1000 / df["Price"]
df["Expensive"] = df["Price"] > 10000

print(df)

print("\n=== CRYPTO ONLY ===")
print(crypto_only)

print("\n=== FOREX ONLY ===")
print(forex_only)