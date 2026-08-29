import pandas as pd

def get_stock_data(ticker: str) -> pd.DataFrame:        # take ticker string and returns the dataframe
    #will call an api n return a dataframe with columns like date and closing price

    #placeholder dataframe for testing
    data = {
        "date": pd.date_range(end=pd.Timestamp.today(), periods=10),
        "close price": [100 +i for i in range(10)]      #list of closing prices
    }
    df = pd.DataFrame(data)         # turn dictionary into a table
    return df