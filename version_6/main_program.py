from tkinter import Tk, Label, Entry, Button, Checkbutton, StringVar, BooleanVar, Radiobutton, IntVar
from functions import stock_market_data, get_preset_dates
import datetime


def open_second_gui():
    def input_data():
        selected_preset = preset_var.get()
        if selected_preset != 4:  # if not specific date range
            start_date, end_date = get_preset_dates(selected_preset)
        else:  # if specific date range
            start_date = start_date_var.get()
            end_date = end_date_var.get()

        interval = interval_var.get()
        stock_market_data(start_date, end_date, interval, volume_checkbox_var.get(), max_min_checkbox_var.get())


    def toggle_date_range_button():
        if preset_var.get() == 4:
            show_date_fields()
        else:
            hide_date_fields()
            download_button.grid(row=9, column=0, columnspan=2)  # Move download button to row 6


    def show_date_fields():
        start_date_label.grid(row=2, column=2)
        start_date_entry.grid(row=2, column=3)
        end_date_label.grid(row=3, column=2)
        end_date_entry.grid(row=3, column=3)

        download_button.grid(row=9, column=0, columnspan=2)


    def hide_date_fields():
        start_date_label.grid_remove()
        start_date_entry.grid_remove()
        end_date_label.grid_remove()
        end_date_entry.grid_remove()

        download_button.grid(row=9, column=0, columnspan=2)


    root = Tk()
    root.title("CD Projekt Red Stock Price Data Downloader")

    # Section for preset date range options
    Label(root, text="Select chart range:", font=("Arial", 11, "bold"), fg="#003366").grid(row=0, column=0, columnspan=4)
    preset_var = IntVar(value=2)
    Radiobutton(root, text="Last Week", variable=preset_var, value=1, command=toggle_date_range_button).grid(row=1, column=0)
    Radiobutton(root, text="Last Month", variable=preset_var, value=2, command=toggle_date_range_button).grid(row=1, column=1)
    Radiobutton(root, text="Last Quarter", variable=preset_var, value=3, command=toggle_date_range_button).grid(row=1, column=2)
    Radiobutton(root, text="Select Specific Date Range", variable=preset_var, value=4, command=toggle_date_range_button).grid(row=1, column=3)

    # Section for specific date range inputs
    start_date_var = StringVar(value='2024-01-01')
    end_date_var = StringVar(value=datetime.datetime.now().strftime('%Y-%m-%d'))

    start_date_label = Label(root, text="Start Date (YYYY-MM-DD):")
    start_date_entry = Entry(root, textvariable=start_date_var)

    end_date_label = Label(root, text="End Date (YYYY-MM-DD):")
    end_date_entry = Entry(root, textvariable=end_date_var)

    # Section for interval selection
    interval_var = StringVar(value='1d')
    Label(root, text="Frequency:", font=("Arial", 11, "bold"), fg="#003366").grid(row=4, column=0, columnspan=4)
    Radiobutton(root, text="daily", variable=interval_var, value='1d').grid(row=5, column=1, sticky='e')
    Radiobutton(root, text="weekly", variable=interval_var, value='1wk').grid(row=5, column=2)
    Radiobutton(root, text="monthly", variable=interval_var, value='1mo').grid(row=5, column=3, sticky='w')

    # Volume checkbox
    volume_checkbox_var = BooleanVar()
    volume_checkbox_var.set(False)
    volume_checkbox = Checkbutton(root, text="Display volume", font=("Arial", 10), fg="#003366", variable=volume_checkbox_var)
    volume_checkbox.grid(row=7, column=0, columnspan=2, sticky='w')

    # Max/min value checkbox
    max_min_checkbox_var = BooleanVar()
    max_min_checkbox_var.set(False)
    max_min_checkbox = Checkbutton(root, text="Show max/min value", font=("Arial", 10), fg="#003366", variable=max_min_checkbox_var)
    max_min_checkbox.grid(row=8, column=0, columnspan=2, sticky='w')

    # Download button
    download_button = Button(root, text="Download Chart", font=("Arial", 10, "bold"), fg="#003366", command=input_data)
    Label(root, text="").grid(row=11, column=1)  # Additional empty row

    # Initially hide date fields and set initial positions
    hide_date_fields()

    root.mainloop()