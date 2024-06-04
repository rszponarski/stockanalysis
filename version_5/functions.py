import time
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from tkinter.messagebox import showerror
from wig20_40_data import WIG20, mWIG40  # Importujemy słowniki z aliasami spółek


def stock_market_data(selected_stock, start_date, end_date, interval, show_volume=False, show_extremes=False):
    try:
        # Konwersja dat do obiektów datetime
        if interval == '1d':
            start_date = start_date.strftime('%Y-%m-%d')
            end_date = end_date.strftime('%Y-%m-%d')
        elif interval == '1wk':
            start_date = (end_date - datetime.timedelta(weeks=1)).strftime('%Y-%m-%d')
        elif interval == '1mo':
            start_date = (end_date - datetime.timedelta(days=30)).strftime('%Y-%m-%d')

        start_date_converted = int(time.mktime(datetime.datetime.strptime(start_date, '%Y-%m-%d').timetuple()))
        end_date_converted = int(time.mktime(datetime.datetime.strptime(end_date, '%Y-%m-%d').timetuple()))

        # Uzyskanie aliasu spółki na podstawie wyboru użytkownika
        if selected_stock in WIG20:
            alias = WIG20[selected_stock]
        elif selected_stock in mWIG40:
            alias = mWIG40[selected_stock]
        else:
            raise ValueError("Selected stock not found in WIG20 or mWIG40 dictionary.")

        # Utworzenie URL z wybranym aliasem spółki
        url = (f'https://query1.finance.yahoo.com/v7/finance/download/{alias}?'
               f'period1={start_date_converted}&period2={end_date_converted}&interval={interval}&events=history&includeAdjustedClose=true')

        df = pd.read_csv(url)
        df['Date'] = pd.to_datetime(df['Date'])

        fig, ax1 = plt.subplots(figsize=(10, 5))

        ax1.plot(df['Date'], df['Close'], label='Close Price', color='blue')
        ax1.set_xlabel('Date')
        ax1.set_ylabel('Price, PLN', color='blue')
        ax1.tick_params('y', colors='blue')
        ax1.tick_params(axis='x', labelcolor='black')

        if show_volume:
            ax2 = ax1.twinx()
            ax2.bar(df['Date'], df['Volume'], color='green', alpha=0.5, label='Volume')
            ax2.set_ylabel('Volume', color='green')
            ax2.tick_params('y', colors='green')
            ax2.tick_params(axis='x', labelcolor='black')

            # Format volume axis labels to avoid scientific notation
            formatter = FuncFormatter(lambda x, _: f'{int(x):,}')
            ax2.yaxis.set_major_formatter(formatter)

        if show_extremes:
            max_value = df['Close'].max()
            min_value = df['Close'].min()
            max_date = df.loc[df['Close'].idxmax(), 'Date']
            min_date = df.loc[df['Close'].idxmin(), 'Date']

            ax1.plot(max_date, max_value, 'ro')  # Max value marker
            ax1.plot(min_date, min_value, 'ro')  # Min value marker

            ax1.text(max_date, max_value, f'{max_value:.2f} PLN', ha='left', va='bottom')  # Text for max value
            ax1.text(min_date, min_value, f'{min_value:.2f} PLN', ha='left', va='bottom')  # Text for min value

        plt.title(f'{selected_stock} Stock Price')
        ax1.legend(loc='upper left')
        if show_volume:
            ax2.legend(loc='upper left', bbox_to_anchor=(0, 0.92))
        plt.grid(True)

        plt.show()
    except Exception as exc:
        showerror("Error", str(exc))


def get_preset_dates(option):
    end_date = datetime.datetime.now()
    if option == 1:  # Last week
        start_date = end_date - datetime.timedelta(weeks=1)
    elif option == 2:  # Last month
        start_date = end_date - datetime.timedelta(days=30)
    elif option == 3:  # Last quarter
        start_date = end_date - datetime.timedelta(days=90)

    return start_date, end_date
