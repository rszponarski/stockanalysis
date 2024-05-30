from tkinter import Tk, Label, Entry, Button, StringVar, Checkbutton, BooleanVar, Radiobutton, Toplevel, IntVar
from functions import stock_market_data, get_preset_dates
import datetime


def input_data():
    selected_preset = preset_var.get()
    if selected_preset != 4:  # if not specific date range
        start_date, end_date = get_preset_dates(selected_preset)
    else:  # if specific date range
        start_date = start_date_var.get()
        end_date = end_date_var.get()

    interval = interval_var.get()
    stock_market_data(start_date, end_date, interval, volume_checkbox_var.get())


def open_date_range_window():
    top = Toplevel(root)
    top.title("Select Specific Date Range")

    Label(top, text="Start Date (YYYY-MM-DD):").grid(row=0, column=0)
    Entry(top, textvariable=start_date_var).grid(row=0, column=1)

    Label(top, text="End Date (YYYY-MM-DD):").grid(row=1, column=0)
    Entry(top, textvariable=end_date_var).grid(row=1, column=1)

    Button(top, text="OK", command=lambda: (top.destroy(), show_date_fields())).grid(row=2, column=0, columnspan=2)

def toggle_date_range_button():
    if preset_var.get() == 4:
        date_range_button.config(state='normal')
    else:
        date_range_button.config(state='disabled')
        hide_date_fields()

def set_interval(new_interval):
    interval_var.set(new_interval)
    if new_interval == '1d':
        checkbox_1d.select()
        checkbox_1wk.deselect()
        checkbox_1mo.deselect()
    elif new_interval == '1wk':
        checkbox_1d.deselect()
        checkbox_1wk.select()
        checkbox_1mo.deselect()
    elif new_interval == '1mo':
        checkbox_1d.deselect()
        checkbox_1wk.deselect()
        checkbox_1mo.select()

def show_date_fields():
    start_date_label.grid()
    start_date_entry.grid()
    end_date_label.grid()
    end_date_entry.grid()

def hide_date_fields():
    start_date_label.grid_remove()
    start_date_entry.grid_remove()
    end_date_label.grid_remove()
    end_date_entry.grid_remove()

root = Tk()
root.title("CD Projekt Red Stock Price Data Downloader")

# Section for preset date range options
preset_var = IntVar(value=1)
Radiobutton(root, text="Last Week", variable=preset_var, value=1, command=toggle_date_range_button).grid(row=0, column=0)
Radiobutton(root, text="Last Month", variable=preset_var, value=2, command=toggle_date_range_button).grid(row=0, column=1)
Radiobutton(root, text="Last Quarter", variable=preset_var, value=3, command=toggle_date_range_button).grid(row=0, column=2)
Radiobutton(root, text="Select Specific Date Range", variable=preset_var, value=4, command=toggle_date_range_button).grid(row=1, column=0, columnspan=3)

date_range_button = Button(root, text="Open Date Range Selector", command=open_date_range_window)
date_range_button.grid(row=2, column=0, columnspan=3)
date_range_button.config(state='disabled')  # Initially disabled

# Section for interval selection
interval_var = StringVar(value='1d')
Label(root, text="Interval:").grid(row=3, column=0)
checkbox_1d = Checkbutton(root, text="1d", variable=interval_var, onvalue='1d', offvalue='', command=lambda: set_interval('1d'))
checkbox_1d.grid(row=3, column=1)
checkbox_1wk = Checkbutton(root, text="1wk", variable=interval_var, onvalue='1wk', offvalue='', command=lambda: set_interval('1wk'))
checkbox_1wk.grid(row=3, column=2)
checkbox_1mo = Checkbutton(root, text="1mo", variable=interval_var, onvalue='1mo', offvalue='', command=lambda: set_interval('1mo'))
checkbox_1mo.grid(row=3, column=3)
checkbox_1d.select()  # Default selection

# Section for specific date range inputs
start_date_var = StringVar(value='2024-01-01')
end_date_var = StringVar(value=datetime.datetime.now().strftime('%Y-%m-%d'))

start_date_label = Label(root, text="Start Date (YYYY-MM-DD):")
start_date_entry = Entry(root, textvariable=start_date_var)

end_date_label = Label(root, text="End Date (YYYY-MM-DD):")
end_date_entry = Entry(root, textvariable=end_date_var)

# Initially hide date fields
hide_date_fields()

# Volume checkbox
volume_checkbox_var = BooleanVar()
volume_checkbox_var.set(False)
Checkbutton(root, text="Volume", variable=volume_checkbox_var).grid(row=6, column=0, columnspan=2)

# Download button
Button(root, text="Download Prices", command=input_data).grid(row=7, column=0, columnspan=2)

root.mainloop()

