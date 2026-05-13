import pandas as pd


data = {
    "STOCK": ["apple", "tesla", "btc", "eth", "gold" ],
    "price": [189, 260, 81000, 2300, 2028],
    "change": [1.2, -0.5, 2.3, -1.1, 0.3]

}


df = pd.DataFrame(data)
# Basic info
print(df.shape)        # how many rows and columns?
print(df.columns)      # column names
print(df.dtypes)       # data types

# Statistics
print(df["price"].mean())   # average price
print(df["price"].max())    # highest price
print(df["price"].min())    # lowest price

# Filter - only positive changes
winners = df[df["change"] > 0]
print(winners)