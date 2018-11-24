import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as web

def get_adj_close(ticker, start, end):
    start = start
    end = end
    info = web.DataReader(ticker, data_source='yahoo', start=start, end=end)['Adj Close']
    return pd.DataFrame(info)


apple =  get_adj_close('aapl', '23/11/2017', '22/11/2018')
tesla = get_adj_close('tsla', '23/11/2017', '22/11/2018')
amazon = get_adj_close('amzn', '23/11/2017', '22/11/2018')
intel = get_adj_close('intc', '23/11/2017', '22/11/2018')


adobe = get_adj_close('adbe', '01/11/2016', '01/11/2018')
accenture = get_adj_close('acn', '01/11/2016', '01/11/2018')

plt.style.use('tableau-colorblind10')
#Available Styles plt.style.available
#['seaborn-dark', 'seaborn-darkgrid', 'seaborn-ticks', 'fivethirtyeight', 'seaborn-whitegrid', 'classic', '_classic_test', 'fast', 'seaborn-talk', 'seaborn-dark-palette', 'seaborn-bright', 'seaborn-pastel', 'grayscale', 'seaborn-notebook', 'ggplot', 'seaborn-colorblind', 'seaborn-muted', 'seaborn', 'Solarize_Light2', 'seaborn-paper', 'bmh', 'tableau-colorblind10', 'seaborn-white', 'dark_background', 'seaborn-poster', 'seaborn-deep']

#Part 1
apple[['Adj Close']].plot(figsize=(12,6))
plt.title('APPLE')
plt.ylabel('Price (USD)')
plt.show();

tesla[['Adj Close']].plot(figsize=(12,6))
plt.title('Tesla')
plt.ylabel('Price (USD)')
plt.show();


amazon[['Adj Close']].plot(figsize=(12,6))
plt.title('Amazon')
plt.ylabel('Price (USD)')
plt.show();

intel[['Adj Close']].plot(figsize=(12,6))
plt.title('Intel Corporation')
plt.ylabel('Price (USD)')
plt.show();


#Part 2
adobe[['Adj Close']].plot(figsize=(12,6))
plt.title('Adobe Inc')
plt.ylabel('Price (USD)')
plt.show();

accenture[['Adj Close']].plot(figsize=(12,6))
plt.title('Accenture')
plt.ylabel('Price (USD)')
plt.show();



'''

import quandl
quandl.ApiConfig.api_key = 'ai_xDLz4oinvyixQpQFZ'

data = quandl.get_table('WIKI/PRICES', ticker = ['AAPL', 'MSFT', 'WMT','FB','TSLA','AMZN','INTC','ADBE','TCS','KO','CAP','ACN'], 
                        qopts = { 'columns': ['ticker', 'date', 'adj_close'] }, 
                        date = { 'gte': '2018-01-22', 'lte': '2018-11-1' }, 
                        paginate=True)
print(data)



#Part 1
fig, axes = plt.subplots(2, 2, figsize=(24, 12));
plt.subplots_adjust(wspace=1, hspace=1);
target1 = [axes[0][0]]
target2 = [axes[0][1]]
target3 = [axes[1][0]]
target4 = [axes[1][1]]

apple[['Adj Close']].plot(subplots=True, ax=target1)
plt.title('APPLE')
plt.ylabel('Price (USD)')
plt.show();

tesla[['Adj Close']].plot(subplots=True, ax=target2)
plt.title('Tesla')
plt.ylabel('Price (USD)')
plt.show();


amazon[['Adj Close']].plot(subplots=True, ax=target3)
plt.title('Amazon')
plt.ylabel('Price (USD)')
plt.show();

intel[['Adj Close']].plot(subplots=True, ax=target4)
plt.title('Intel Corporation')
plt.ylabel('Price (USD)')
plt.show();


#Part 2
fig, axes = plt.subplots(2, 1, figsize=(12, 6));
plt.subplots_adjust(wspace=0.5, hspace=0.5);
target1 = [axes[0][0]]
target2 = [axes[1][0]]

adobe[['Adj Close']].plot(subplots=True, ax=target1)
plt.title('Adobe Inc')
plt.ylabel('Price (USD)')
plt.show();

accenture[['Adj Close']].plot(subplots=True, ax=target2)
plt.title('Accenture')
plt.ylabel('Price (USD)')
plt.show();
'''
