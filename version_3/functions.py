import pandas as pd
import time
import datetime

def download_data(start_date, end_date, interval):
    try:
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        start_date_converted = int(time.mktime(start_date.timetuple()))
        end_date_converted = int(time.mktime(end_date.timetuple()))

        html_string = (f'https://query1.finance.yahoo.com/v7/finance/download/CDR.WA?'
                        f'period1={start_date_converted}&period2={end_date_converted}&interval={interval}&events=history&includeAdjustedClose=true')

        df = pd.read_csv(html_string)
        df['Date'] = pd.to_datetime(df['Date'])

        return df
    except Exception as exc:
        raise exc

def process_data(data):
    try:
        # ___na razie nic- później
        pass
    except Exception as exc:
        raise exc
