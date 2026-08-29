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

    print(f"fetching data for {ticker}")
    df = get_stock_data(ticker)
    print("raw data: ")
    print(df)

    # fetch data -api
    # - call a get stock data function using ticker from api
    # - use days to filter
    # - print stats
    # - plot graphs

if __name__ == "__main__":
    main()