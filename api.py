import pandas as pd
import yfinance as yf

def get_stock_data(ticker: str) -> pd.DataFrame:        # take ticker string and returns the dataframe
    #download data from yahoo finance so connect tot eh stock market
    df =yf.download(ticker, period="1y")        #last year of data

    df = df.reset_index()       #turn the date index into a column

    #flattern multi index cols
    df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]

    df = df[['Date', 'Close']]

    return df