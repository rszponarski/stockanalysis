from tkinter import Tk, Label, Entry, Button, StringVar, Checkbutton
from functions import stock_market_data
from tkinter import BooleanVar


def input_data():
    start_date = start_date_var.get()
    end_date = end_date_var.get()
    interval = interval_var.get()
    stock_market_data(start_date, end_date, interval, volume_checkbox_var.get())


root = Tk()
root.title("CD Projekt Red Stock Price Data downloader")

Label(root, text="Start Date (YYYY-MM-DD):").grid(row=0, column=0)
start_date_var = StringVar(value='2024-01-01')
Entry(root, textvariable=start_date_var).grid(row=0, column=1)

Label(root, text="End Date (YYYY-MM-DD):").grid(row=1, column=0)
end_date_var = StringVar(value='2024-05-27')
Entry(root, textvariable=end_date_var).grid(row=1, column=1)

Label(root, text="Interval (1d, 1wk, 1mo):").grid(row=2, column=0)
interval_var = StringVar(value='1d')
Entry(root, textvariable=interval_var).grid(row=2, column=1)

# Added VOLUME checkbox to GUI
volume_checkbox_var = BooleanVar()
volume_checkbox_var.set(False)
volume_checkbox = Checkbutton(root, text="Volume", variable=volume_checkbox_var)
volume_checkbox.grid(row=3, column=0, columnspan=2)


def input_data():
    start_date = start_date_var.get()
    end_date = end_date_var.get()
    interval = interval_var.get()
    # podanie info o zaznaczeniu checkboxa do funkcji stock_market_data
    stock_market_data(start_date, end_date, interval, volume_checkbox_var.get())

# modyfikacja przycisku wywołujący funkcję input_data
Button(root, text="Download prices", command=input_data).grid(row=4, column=0, columnspan=2)

root.mainloop()
