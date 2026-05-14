import matplotlib.pyplot as plt
import matplotlib.style as style
import requests
import pandas as pd

def get_price(coin):
    url = f"https://min-api.cryptocompare.com/data/price?fsym={coin}&tsyms=USD"
    response = requests.get(url)
    return response.json()["USD"]

# Live prices
coins  = ["BTC", "ETH", "BNB", "SOL", "XRP"]
prices = [get_price(c) for c in coins]

# Dark theme
plt.style.use("dark_background")

# Create figure
fig, axes = plt.subplots(2, 1, figsize=(12, 10))

# Chart 1 - Bar chart
axes[0].bar(coins, prices, color=["#F7931A", "#627EEA", "#F3BA2F", "#9945FF", "#00AAE4"])
axes[0].set_title("🔥 Live Crypto Prices", fontsize=16, pad=15)
axes[0].set_ylabel("Price (USD)")
axes[0].grid(axis="y", alpha=0.3)

# Add price labels on bars
for i, (coin, price) in enumerate(zip(coins, prices)):
    axes[0].text(i, price, f"${price:,.0f}", ha="center", va="bottom", fontsize=9)

# Chart 2 - Horizontal bar
axes[1].barh(coins, prices, color=["#F7931A", "#627EEA", "#F3BA2F", "#9945FF", "#00AAE4"])
axes[1].set_title("📊 Price Comparison", fontsize=16, pad=15)
axes[1].set_xlabel("Price (USD)")
axes[1].grid(axis="x", alpha=0.3)

plt.tight_layout(pad=3)
plt.suptitle("Shivansh's Crypto Dashboard", fontsize=18, y=1.02)
plt.show()