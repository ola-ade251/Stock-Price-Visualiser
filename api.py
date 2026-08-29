import pandas as pd
import yfinance as yf

def get_stock_data(ticker: str) -> pd.DataFrame:        # take ticker string and returns the dataframe
    #download data from yahoo finance so connect tot eh stock market
    df =yf.download(ticker, period="1y")        #last year of data

    df = df.reset_index()       #turn the date index into a column
    df = df[['Date', 'Close']]

    return df