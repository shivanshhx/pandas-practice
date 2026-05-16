import numpy as np
import requests
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def get_price(coin):
    url = f"https://min-api.cryptocompare.com/data/price?fsym={coin}&tsyms=USD"
    response = requests.get(url)
    return response.json()["USD"]


current_price = get_price("BTC")
print(f"Current BTC price: ${current_price:,.2f}")


np.random.seed(42)
noise = np.random.randn(10) * 500
history = [current_price - 4500 + (i *500) + noise[i] for i in range(10)]


days = np.array(range(1, 11)).reshape(-1, 1)
prices = np.array(history)


model = LinearRegression()
model.fit(days, prices)

future = np.array(range(11, 16)).reshape(-1, 1)
predictions = model.predict(future)


print("\n BTC PRICE PREDICTION ")
for i, pred in enumerate(predictions):
    print(f"DAY {11+i}: ${pred:,.2f}")


plt.style.use("dark_background")
plt.figure(figsize=(12, 6))
plt.plot(days, prices, color="cyan", marker="o", label="historical")
plt.plot(future, predictions, color="orange", marker="o",
          linestyle="--", label="predicted")
plt.axvline(x=10.5, color="white", linestyle="--", alpha=0.5)
plt.title("BTC Price Predictions", fontsize = 16)
plt.xlabel("Days")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(alpha=0.3)
plt.show()