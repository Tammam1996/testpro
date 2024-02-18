import yfinance as yf
msft = yf.Ticker("MSFT")
msft_data = msft.history(period="1d")

msft_data.head()