from api import get_stock_data

def get_user_inp():
    ticker = input("Enter stock ticker(e.g, AAPL, TSLA): ").strip().upper()
    days_inp = input("Enter number of days to visualise: ").strip()

    # convert days inp into int and validate
    try:
        days = int(days_inp)            #try to convert inp to int, if fail then stop function
    except ValueError:
        print("Number of days must be an integer")
        return None, None
        
    return ticker, days


def main():
    # get user input
    ticker, days = get_user_inp()
    if ticker is None or days is None:
        return 
    
    # - call a get stock data function using ticker from api
    print(f"fetching data for {ticker}")
    df = get_stock_data(ticker)
    print("raw data:")
    print(df)                   # print full table
    
    # filter the last n days
    df_last_days = df.tail(days)
    print(f"\nLast {days} days:")
    print(df_last_days)         #print filtered table


    df_last_days = df_last_days.dropna(subset =['Close']) #remove last row if nan
    #calc stats
    highest = df_last_days['Close'].max()
    lowest = df_last_days['Close'].min()
    average = df_last_days['Close'].mean()

    start_price = df_last_days['Close'].iloc[0]
    end_price = df_last_days['Close'].iloc[-1]
    percent_change = ((end_price - start_price) / start_price) * 100

    print("\nStats:")
    print(f"Highest closing price: {highest:.2f}")
    print(f"Lowest closing price: {lowest:.2f}")
    print(f"Average closing price: {average:.2f}")
    print(f"percent change over {days} days: {percent_change:.2f}")

if __name__ == "__main__":
    main()