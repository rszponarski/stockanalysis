import tkinter as tk
from tkinter import ttk
from wig20_40_data import WIG20, mWIG40
from main_program import open_second_gui  # Import a function that opens the second GUI
from functions import stock_market_data, get_preset_dates


def on_index_selected(event):
    selected_index = index_var.get()
    print("Selected index:", selected_index)

    # Clear any existing stock selection widgets
    clear_stock_widgets()

    if selected_index == "WIG20":
        display_stock_selection(WIG20)

    elif selected_index == "mWIG40":
        display_stock_selection(mWIG40)


def display_stock_selection(stock_dict):
    global stock_combobox
    # Display "Choose stock" label
    stock_label = tk.Label(root, text="Choose a stock:", font=("Arial", 14, 'bold'), fg="#003366")
    stock_label.pack(pady=5)

    # Combobox for choosing stock
    stock_var = tk.StringVar()
    stock_combobox = ttk.Combobox(root, textvariable=stock_var, values=list(stock_dict.keys()))
    stock_combobox.pack(pady=5)

    # Bind event to stock combobox selection
    stock_combobox.bind("<<ComboboxSelected>>", on_stock_selected)

    # Store reference to stock selection widgets
    stock_widgets.append(stock_label)
    stock_widgets.append(stock_combobox)


def clear_stock_widgets():
    # Destroy all previous stock selection widgets
    for widget in stock_widgets:
        widget.destroy()
    # Clear the list of stock selection widgets
    stock_widgets.clear()


def on_stock_selected(event):
    global selected_stock
    selected_stock = event.widget.get()
    print("Selected stock:", selected_stock)
    # Display the Next button after selecting a stock
    next_button.pack_forget()  # Hide the Next button if it was previously visible
    next_button.pack(side="bottom")  # Place the Next button at the bottom


def on_next_button_click():
    selected_index = index_var.get()
    print("Next button clicked with index:", selected_index, "and stock:", selected_stock)
    root.destroy()  # Closing the main window before opening a new one
    open_second_gui(selected_index, selected_stock)
    # Opening a second GUI - passing user selections


root = tk.Tk()
root.title("Stock Analysis Program")

# List to store references to stock selection widgets
stock_widgets = []

# Welcome message
welcome_label = tk.Label(root, text="Welcome to the stock technical analysis program!", font=("Arial", 14, 'italic'),
                         fg="#003366")
welcome_label.pack(pady=10)

# Explanation
explanation_label = tk.Label(root, text="This application allows you to perform technical analysis of listed "
                                        "companies from the Warsaw Stock Exchange Index.", font=("Arial", 12))
explanation_label.pack(pady=10)

explanation_label = tk.Label(root, text="Let's get started!", font=("Arial", 14, 'bold'), fg="#003366")
explanation_label.pack(pady=1)

# Instructions
instruction_label = tk.Label(root, text="Please choose an index where your company is listed:", font=("Arial", 12))
instruction_label.pack(pady=1)

# Combobox for choosing index
index_var = tk.StringVar()
index_combobox = ttk.Combobox(root, textvariable=index_var, values=["WIG20", "mWIG40"], width=22)
index_combobox.pack(pady=5)

# Bind event to combobox selection
index_combobox.bind("<<ComboboxSelected>>", on_index_selected)

# Next button
next_button = tk.Button(root, text="Next", command=on_next_button_click, font=("Arial", 14, 'bold'), fg="#003366",
                        bg="#E0E0E0", bd=5, width=10)
next_button.pack_forget()  # Hide the Next button initially

root.mainloop()