# CD Projekt Stock Data Downloader

This Python script downloads historical stock data for CD Projekt from the Warsaw Stock Exchange (GPW) using Yahoo Finance API.

## New Features in REV.00B

- Added functionality to display trading volume on the chart (with 00A).
- Current day added as END DATE when selecting the user's own date range
- Improved user interface by adding volume checkbox
(instead of entering from keyboard)
- By design, at the beginning, the GUI included a choice for the user whether
they wanted to see the closing price chart for the last week, month and
quarter (a checkbox allowing only one choice), and there was also a
"select specific date range" button after clicking, in which a window
for entering a date range appears, in which the user can select a date
range (as in the previous code) and a chart is generated on this basis.

## Requirements

- Python 3.x
- pandas
- matplotlib
- tkinter

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/rszponarski/stockanalysis.git
    ```

2. Navigate to the directory:

    ```sh
    cd stockanalysis/version_2
    ```

3. Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:

    ```sh
    python main_program.py
    ```

2. Enter the start date, end date, and interval (1d, 1wk, 1mo) in the GUI window.

3. Click on the "Download prices" button to download and visualize the stock data.

