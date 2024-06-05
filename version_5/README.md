# Stock Analysis Program

The Stock Analysis Program is a GUI-based application that allows users to perform technical
analysis of companies listed on the Warsaw Stock Exchange (WIG20 and mWIG40). Users can 
select a stock, choose a date range and interval for the data, and visualize stock prices 
with additional options for volume and extreme values.

## Features

- Select a stock from WIG20 / mWIG40 indices.
- Choose a date range (last week, last month, last quarter, or a specific date range).
- Select data frequency (daily, weekly, monthly).
- Display stock price charts with options to show volume and highlight maximum/minimum prices.

## Requirements

- Python 3.x
- pandas
- matplotlib
- tkinter

## Installation

1. Clone the repository:
    ```sh
   git clone https://github.com/rszponarski/stockanalysis.git
   cd stockanalysis
    ```

2. Navigate to the directory:
    ```sh
    cd stockanalysis/version_5
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:
    ```sh
    python start_window.py

    ```
2. Follow the on-screen instructions:

- Select the index (WIG20 or mWIG40).
- Choose a stock from the selected index.
- Click "Next" to proceed to the second window.

- Select the date range and interval.
- Optionally, choose to display volume and maximum/minimum values.
- Click "Download Chart" to visualize the stock price data.

# Project Structure
- start_window.py: Main GUI for selecting the index and stock.
- main_program.py: Second GUI for selecting date range, interval, and additional options.
- functions.py: Contains functions for fetching and visualizing stock market data.
- wig20_40_data.py: Contains dictionaries for WIG20 and mWIG40 stocks with their respective Yahoo Finance symbols.


