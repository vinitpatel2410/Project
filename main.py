import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Load data from CSV
data = pd.read_csv('NIFTY50DATA.csv')

# Replace '-' with NaN
data.replace('-', np.nan, inplace=True)

# Drop rows with all NaN values
data.dropna(how='all', inplace=True)

# Preprocess data: Remove commas and convert to numeric
data = data.replace('[\$,]', '', regex=True)
data[['Open', 'High', 'Low', 'Close*']] = data[['Open', 'High', 'Low', 'Close*']].apply(pd.to_numeric, errors='coerce')
data.dropna(inplace=True)

# Linear Regression
X = data[['Open']]
y = data['Close*']

model = LinearRegression()
model.fit(X, y)

data['Predicted_Close'] = model.predict(X)

# Create Seasonality
data['Date'] = pd.to_datetime(data['Date'])
data['Month'] = data['Date'].dt.month
data['Price_Change_Percentage'] = ((data['Close*'] - data['Open']) / data['Open']) * 100
monthly_seasonality = data.groupby('Month')['Price_Change_Percentage'].mean()

# Golden Days
data['Price_Range'] = data['High'] - data['Low']
threshold = data['Price_Range'].quantile(0.9)
golden_days = data[data['Price_Range'] > threshold]['Date']

# Intraday Strategy: SMA Crossover
short_window = 50  # Short-term moving average window
long_window = 200   # Long-term moving average window

data['SMA_Short'] = data['Close*'].rolling(window=short_window).mean()
data['SMA_Long'] = data['Close*'].rolling(window=long_window).mean()

data['Signal'] = 0  # 1 for buy signal, -1 for sell signal
data.loc[data['SMA_Short'] > data['SMA_Long'], 'Signal'] = 1
data.loc[data['SMA_Short'] < data['SMA_Long'], 'Signal'] = -1

# Get user input for start and end year
start_year = int(input("Enter the start year: "))
end_year = int(input("Enter the end year: "))

# Filter data for the specified year range
filtered_data = data[(data['Date'].dt.year >= start_year) & (data['Date'].dt.year <= end_year)]

# Plotting
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(filtered_data['Date'], filtered_data['Close*'], label='Actual Close')
plt.plot(filtered_data['Date'], filtered_data['Predicted_Close'], label='Predicted Close', linestyle='dashed')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title(f'Actual vs Predicted Close Prices ({start_year}-{end_year})')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(filtered_data['Date'], filtered_data['SMA_Short'], label=f'SMA-{short_window}')
plt.plot(filtered_data['Date'], filtered_data['SMA_Long'], label=f'SMA-{long_window}')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('SMA Crossover Strategy')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(filtered_data['Date'], filtered_data['Signal'], label='Signal', marker='o', linestyle='None')
plt.xlabel('Date')
plt.ylabel('Signal')
plt.title('Buy/Sell Signals')
plt.ylim([-1.5, 1.5])
plt.legend()

plt.tight_layout()
plt.show()

# Print Golden Days
print("Golden Days:")
print(golden_days)
