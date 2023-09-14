# Delow - Stock Analysis and Trading Strategy

Delow is a Python script for analyzing historical stock price data and implementing a simple trading strategy using moving averages. This script uses the NIFTY50 stock market data as an example, but you can easily adapt it for other stock datasets. Delow performs the following tasks:

## Features

1. **Data Loading and Preprocessing**:
   - Reads historical stock data from a CSV file (`NIFTY50DATA.csv`).
   - Replaces '-' with NaN and drops rows with all NaN values.
   - Removes commas and converts relevant columns to numeric data types.

2. **Linear Regression**:
   - Uses linear regression to predict the closing price based on the opening price.
   - Adds a 'Predicted_Close' column to the data.

3. **Seasonality Analysis**:
   - Extracts the month from the date and calculates the average percentage price change for each month.
   - Displays the seasonal price change.

4. **Golden Days**:
   - Identifies "golden days" when the price range (high - low) is in the top 10% of all price ranges.
   - Lists the dates with golden price ranges.

5. **Intraday Strategy: SMA Crossover**:
   - Implements a Simple Moving Average (SMA) crossover strategy.
   - Defines short-term (50-day) and long-term (200-day) moving averages.
   - Generates buy (+1) and sell (-1) signals based on the crossover of these moving averages.

6. **User Input**:
   - Asks the user for a start and end year to filter the data for analysis.

7. **Data Visualization**:
   - Plots three subplots to visualize:
     - Actual vs. Predicted Close Prices over the specified year range.
     - Short-term and long-term SMAs over the specified year range.
     - Buy (+1) and sell (-1) signals.

8. **Display Golden Days**:
   - Prints the dates identified as golden days.

## Getting Started

1. Clone this GitHub repository to your local machine.

2. Ensure you have the necessary Python libraries installed (Pandas, Matplotlib, NumPy, and Scikit-Learn).

3. Place your historical stock data CSV file in the same directory as `delow.py`. Make sure your CSV file has columns named 'Date', 'Open', 'High', 'Low', and 'Close*'.

4. Run the script using Python. It will guide you through the analysis and display the results.

**Note**: Delow is a simplified example and may require further customization for more complex trading strategies or datasets. Use it as a starting point for your stock analysis and trading projects.

## Example Usage

Here's an example of how to use Delow:

```bash
python main.py
