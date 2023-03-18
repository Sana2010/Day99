import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import alpaca_trade_api  as tradeapi
%config InlineBackend.figure_format = 'retina'

api = tradeapi.REST('YOUR_API_KEY_HERE',  
                     'YOUR_SECRET_CODE_HERE',
                      'https://paper-api.alpaca.markets')
api.list_positions()

api.submit_order(‘SNAP’, 100, ‘buy’, ‘market’, ‘day’)
api.submit_order(‘SLV’, 100, ‘buy’, ‘market’, ‘day’)
api.submit_order(‘JNJ’, 100, ‘buy’, ‘market’, ‘day’)
api.submit_order(‘AAPL’, 10, ‘buy’, ‘market’, ‘day’)
api.submit_order(‘GLD’, 100, ‘buy’, ‘market’, ‘day’)
api.submit_order(‘GOOG’, 1, ‘buy’, ‘market’, ‘day’)
api.submit_order(‘CAT’, 100, ‘buy’, ‘market’, ‘day’)
api.submit_order(‘EWZ’, 10, ‘buy’, ‘market’, ‘day’)

pos_list = [x.symbol submit_order for x  in api. list_positions()]

def  get_bars(symbol):
     data = api. get_barset(symbol, ‘day’, limit=1000)
     data =  data.df[symbol][‘close’]
     return data

def correlation(equity_list):  
    
    df = pd. DataFrame()
    equity_columns = []
    
    for symbol in equity_list:   
        try:
            symbol_df = get_bars(symbol)
            df = pd.concat([df, symbol_df], axis=1)
            equity_columns.append(symbol)
        except:
            print('Exception with {}'.format(symbol))
            
    df.columns = equity_columns
    
    sum_corr = df.corr().sum().sort_values(ascending=True).index.values
    
    return df[sum_corr].corr()