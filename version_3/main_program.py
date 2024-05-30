from tkinter import Tk, Label, Entry, Button, StringVar, Checkbutton, BooleanVar
from functions import stock_market_data
import datetime


def input_data():
    start_date = start_date_var.get()
    end_date = end_date_var.get()
    interval = interval_var.get()
    stock_market_data(start_date, end_date, interval, volume_checkbox_var.get())


root = Tk()
root.title("CD Projekt Red Stock Price Data Downloader")

Label(root, text="Start Date (YYYY-MM-DD):").grid(row=0, column=0)
start_date_var = StringVar(value='2024-01-01')
Entry(root, textvariable=start_date_var).grid(row=0, column=1)

Label(root, text="End Date (YYYY-MM-DD):").grid(row=1, column=0)
current_date = datetime.datetime.now().strftime('%Y-%m-%d')
end_date_var = StringVar(value=current_date)
Entry(root, textvariable=end_date_var).grid(row=1, column=1)

Label(root, text="Interval (1d, 1wk, 1mo):").grid(row=2, column=0)
interval_var = StringVar(value='1d')
Entry(root, textvariable=interval_var).grid(row=2, column=1)

volume_checkbox_var = BooleanVar()
volume_checkbox_var.set(False)
Checkbutton(root, text="Volume", variable=volume_checkbox_var).grid(row=3, column=0, columnspan=2)

Button(root, text="Download Prices", command=input_data).grid(row=4, column=0, columnspan=2)

root.mainloop()

