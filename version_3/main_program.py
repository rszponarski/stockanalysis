import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, StringVar, Checkbutton, BooleanVar
from tkinter.messagebox import showerror
import pandas as pd
import os
from functions import download_data

def input_data():
    start_date = start_date_var.get()
    end_date = end_date_var.get()
    stock_market_data(start_date, end_date, volume_checkbox_var.get())

def stock_market_data(start_date, end_date, show_volume=False):
    try:
        if not os.path.exists('stock_data.csv'):
            download_data()  # pobierz dane jeśli plik nie istnieje, po pierwszym wyszukiwaniu na pewno nie istnieje

        df = pd.read_csv('stock_data.csv')
        df['Date'] = pd.to_datetime(df['Date'])

        # Wyświetlenie generowanego URL dla debugowania
        print(f'Generowany URL: https://query1.finance.yahoo.com/v7/finance/download/CDR.WA?period1={start_date}&period2={end_date}&interval=1d&events=history&includeAdjustedClose=true')

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
        else:
            mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
            df_filtered = df.loc[mask]

            plt.figure(figsize=(10, 5))
            plt.plot(df_filtered['Date'], df_filtered['Close'], label='Close Price')
            plt.xlabel('Date')
            plt.xticks(rotation=45)
            plt.ylabel('Price')
            plt.title('CD Projekt Red Stock Price')
            plt.legend()
            plt.grid(True)
            plt.show()
    except Exception as exc:
        showerror("Error", str(exc))


root = Tk()
root.title("CD Projekt Red Stock Price Data downloader")

Label(root, text="Start Date (YYYY-MM-DD):").grid(row=0, column=0)
start_date_var = StringVar(value='2024-01-01')
Entry(root, textvariable=start_date_var).grid(row=0, column=1)

Label(root, text="End Date (YYYY-MM-DD):").grid(row=1, column=0)
end_date_var = StringVar(value='2024-05-27')
Entry(root, textvariable=end_date_var).grid(row=1, column=1)

volume_checkbox_var = BooleanVar()
volume_checkbox_var.set(False)
volume_checkbox = Checkbutton(root, text="Volume", variable=volume_checkbox_var)
volume_checkbox.grid(row=2, column=0, columnspan=2)

Button(root, text="Download prices", command=input_data).grid(row=3, column=0, columnspan=2)

root.mainloop()

# usuwanie plik tymczasowy z danymi - juz po wyjsciu z petli
os.remove('stock_data.csv')
