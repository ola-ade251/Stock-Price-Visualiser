from api import get_stock_data
import matplotlib.pyplot as plt

def get_user_inp():
    ticker = input("Enter stock ticker(e.g, AAPL, TSLA): ").strip().upper()
    days_inp = input("Enter number of days to visualise: ").strip()

    compare = input("would you like to compare with another ticker? (yes/no): ").strip().lower()
    compare_ticker = None
    if compare == "yes":
        compare_ticker = input("Enter ticker you would like to compare: ").strip().upper()

    # convert days inp into int and validate
    try:
        days = int(days_inp)            #try to convert inp to int, if fail then stop function
    except ValueError:
        print("Number of days must be an integer")
        return None, None, None
        
    return ticker, days, compare_ticker


def main():
    # get user input
    ticker, days, compare_ticker = get_user_inp()
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

    if compare_ticker:
        df_compare = get_stock_data(compare_ticker)
        df_compare_last_days = df_compare.tail(days).dropna(subset =['Close']) #remove last row if nan


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


    #plotting graphs
    plt.figure(figsize=(10, 5))
    #main
    plt.plot(df_last_days['Date'], df_last_days['Close'], marker ='o', linestyle='-', color='blue', label=ticker)
    #compare
    if compare_ticker:
        plt.plot(df_compare_last_days['Date'], df_compare_last_days['Close'], marker ='o', linestyle='-', color='orange', label = compare_ticker)

    plt.title(f"{ticker} closing prices (last {days} days)")
    plt.xlabel("Date")
    plt.ylabel("Closing price $")
    plt.grid(True)
    plt.xticks(rotation = 45)
    plt.legend()
    plt.tight_layout()

    plt.show()

if __name__ == "__main__":
    main()