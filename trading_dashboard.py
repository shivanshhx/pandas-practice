import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

# ── FETCH LIVE PRICES ──────────────────
def get_price(symbol):
    url = f"https://min-api.cryptocompare.com/data/price?fsym={symbol}&tsyms=USD"
    response = requests.get(url)
    return response.json()["USD"]

print("Fetching live prices...")

# All markets
assets  = ["BTC", "ETH", "BNB", "SOL", "EUR", "GBP"]
markets = ["Crypto", "Crypto", "Crypto", "Crypto", "Forex", "Forex"]
prices  = [get_price(a) for a in assets]

# ── BUILD DATAFRAME ────────────────────
df = pd.DataFrame({
    "Asset"  : assets,
    "Market" : markets,
    "Price"  : prices,
})

# ── NUMPY ANALYSIS ─────────────────────
df["Mean"]    = np.mean(prices)
df["Std"]     = np.std(prices)
df["Z_Score"] = ((df["Price"] - df["Mean"]) / df["Std"]).round(2)
df["Signal"]  = df["Z_Score"].apply(lambda x: "BUY 🟢" if x < -0.5 else "HOLD 🟡" if x < 0.5 else "SELL 🔴")

# ── PRINT DASHBOARD ────────────────────
print("\n" + "="*60)
print("         SHIVANSH'S LIVE TRADING DASHBOARD")
print("="*60)
print(df[["Asset", "Market", "Price", "Signal"]].to_string(index=False))
print("="*60)

# ── MATPLOTLIB CHARTS ──────────────────
plt.style.use("dark_background")
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

colors = ["#F7931A", "#627EEA", "#F3BA2F", "#9945FF", "#3498db", "#e74c3c"]

# Chart 1 - Prices
axes[0].bar(df["Asset"], df["Price"], color=colors)
axes[0].set_title("Live Prices", fontsize=14)
axes[0].set_ylabel("Price (USD)")
axes[0].grid(axis="y", alpha=0.3)
for i, (asset, price) in enumerate(zip(assets, prices)):
    axes[0].text(i, price, f"${price:,.0f}", ha="center", va="bottom", fontsize=8)

# Chart 2 - Signals
signal_colors = ["green" if "BUY" in s else "yellow" if "HOLD" in s else "red" for s in df["Signal"]]
axes[1].bar(df["Asset"], df["Z_Score"], color=signal_colors)
axes[1].set_title("Buy/Hold/Sell Signals", fontsize=14)
axes[1].set_ylabel("Z Score")
axes[1].axhline(y=0, color="white", linestyle="--", alpha=0.5)
axes[1].grid(axis="y", alpha=0.3)

plt.suptitle("Shivansh's Trading Dashboard", fontsize=16)
plt.tight_layout()
plt.show()