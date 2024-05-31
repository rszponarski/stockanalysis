from tkinter import Tk, Label, Entry, Button, StringVar, Checkbutton, BooleanVar, Radiobutton, IntVar
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


def toggle_date_range_button():
    if preset_var.get() == 4:
        show_date_fields()
    else:
        hide_date_fields()

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

# Section for interval selection
interval_var = StringVar(value='1d')
Label(root, text="Interval:").grid(row=2, column=0)
Radiobutton(root, text="1d", variable=interval_var, value='1d').grid(row=2, column=1)
Radiobutton(root, text="1wk", variable=interval_var, value='1wk').grid(row=2, column=2)
Radiobutton(root, text="1mo", variable=interval_var, value='1mo').grid(row=2, column=3)

# section for specific date range inputs
start_date_var = StringVar(value='2024-01-01')
end_date_var = StringVar(value=datetime.datetime.now().strftime('%Y-%m-%d'))

start_date_label = Label(root, text="Start Date (YYYY-MM-DD):")
start_date_entry = Entry(root, textvariable=start_date_var)

end_date_label = Label(root, text="End Date (YYYY-MM-DD):")
end_date_entry = Entry(root, textvariable=end_date_var)

# initially hide date fields
hide_date_fields()

# volume checkbox
volume_checkbox_var = BooleanVar()
volume_checkbox_var.set(False)
Checkbutton(root, text="Volume", variable=volume_checkbox_var).grid(row=3, column=0, columnspan=2)

# download button
Button(root, text="Download Prices", command=input_data).grid(row=4, column=0, columnspan=2)

root.mainloop()