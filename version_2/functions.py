# functions.py
import time
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from tkinter.messagebox import showerror


def stock_market_data(start_date, end_date, interval):
    try:
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        start_date_converted = int(time.mktime(start_date.timetuple()))
        end_date_converted = int(time.mktime(end_date.timetuple()))

        html_string = (f'https://query1.finance.yahoo.com/v7/finance/download/CDR.WA?'
                        f'period1={start_date_converted}&period2={end_date_converted}&interval={interval}&events=history&includeAdjustedClose=true')

        df = pd.read_csv(html_string)
        df['Date'] = pd.to_datetime(df['Date'])

        plt.figure(figsize=(10, 5))
        plt.plot(df['Date'], df['Close'], label='Close Price')
        plt.xlabel('Date')
        plt.xticks(rotation=45)
        plt.ylabel('Price')
        plt.title('CD Projekt Red Stock Price')
        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as exc:
        showerror("Error", str(exc))