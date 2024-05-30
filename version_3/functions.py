import os
import pandas as pd
import datetime
import yfinance as yf

def download_data():
    try:
        if not os.path.exists('stock_data.csv'):  # plik z danymi istnieje?
            # Pobranie danych przy użyciu yfinance
            stock_data = yf.download('CDR.WA', period='10y', interval='1d')

            # Zapisanie danych do pliku CSV
            stock_data.to_csv('stock_data.csv')
    except Exception as exc:
        raise exc


def process_data(data):
    try:
        # ___na razie nic- później
        pass
    except Exception as exc:
        raise exc

