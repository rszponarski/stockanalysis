import time
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from tkinter.messagebox import showerror


def stock_market_data(start_date, end_date, interval, show_volume=False):
    try:
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        start_date_converted = int(time.mktime(start_date.timetuple()))
        end_date_converted = int(time.mktime(end_date.timetuple()))

        html_string = (f'https://query1.finance.yahoo.com/v7/finance/download/CDR.WA?'
                        f'period1={start_date_converted}&period2={end_date_converted}&interval={interval}&events=history&includeAdjustedClose=true')

        df = pd.read_csv(html_string)
        df['Date'] = pd.to_datetime(df['Date'])

        # gdyopcja wyświetlania wolumenu ---> zaznaczona, generuj wykres z wolumenem
        if show_volume:
            plt.figure(figsize=(12, 6))
            ax1 = plt.subplot(2, 1, 1)
            ax1.plot(df['Date'], df['Close'], label='Close Price')
            ax1.set_xlabel('Date')
            ax1.set_ylabel('Price')
            ax1.set_title('CD Projekt Red Stock Price')
            ax1.legend()
            ax1.grid(True)

            ax2 = plt.subplot(2, 1, 2)
            ax2.bar(df['Date'], df['Volume'], color='blue', alpha=0.5, label='Volume')
            ax2.set_xlabel('Date')
            ax2.set_ylabel('Volume')
            ax2.legend()
            ax2.grid(True)

            plt.tight_layout()
            plt.show()
        # gdy opcja wyświetlania wolumenu nie jest zaznaczona-- generuj wykres bez wolumenu
        else:
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
