import yfinance as yf
import matplotlib.pyplot as plt

ticker=input("Enter stock Name:: ")
data=yf.download(ticker,start="2021-01-01",end="2023-10-13")

plt.figure(figsize=(10,5))
plt.plot(data["Close"])
plt.title(f"{ticker}Stock Chart")
plt.xlabel("Date")
plt.ylabel("Price (INR)")
plt.show()
