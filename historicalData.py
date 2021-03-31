import pandas as pd
import time
import ccxt

pd.set_option('expand_frame_repr', False)

bitmex = ccxt.bitmex()
limit = 500
current_time = int(time.time()//60 * 60 * 1000)
since_time = current_time - limit * 60 * 1000

# data = bitmex.fetch_ohlcv(symbol='BTC/USD',timeframe='1d', limit=500, since= since_time)
data = bitmex.fetch_ohlcv(symbol='BTC/USD', limit=500, since= since_time)
df = pd.DataFrame(data)
df = df.rename(columns={0: 'time', 1: 'open', 2: 'high', 3: 'low', 4: 'close', 5: 'vol'})
df['time'] = pd.to_datetime(df['time'], unit='ms') + pd.Timedelta(hours=9)
df = df.set_index('time', drop=True)
df.to_csv('bitmax_btc_data.csv')
print(df)