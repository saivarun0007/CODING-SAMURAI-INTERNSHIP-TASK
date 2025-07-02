import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
import zipfile
from sklearn.linear_model import LinearRegression
import numpy as np

zip_path = 'AI Stock Price.zip' 
extract_dir = 'extracted_data'

# Extract ZIP if not already
if not os.path.exists(extract_dir):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)

# Get list of CSV files
csv_files = [f for f in os.listdir(extract_dir) if f.endswith('.csv')]
companies = [os.path.splitext(f)[0] for f in csv_files]
price_types = ['Open', 'High', 'Low', 'Close', 'Volume']

# --- Prediction & Plot Function ---
def plot_data(company, price_type):
    file_path = os.path.join(extract_dir, company + '.csv')
    data = pd.read_csv(file_path)
    data['Date'] = pd.to_datetime(data['Date'])
    data = data.sort_values('Date')

    # Select features
    data = data[['Date', price_type]].dropna()
    data.reset_index(drop=True, inplace=True)

    # Prepare for prediction
    data['Days'] = (data['Date'] - data['Date'].min()).dt.days
    X = data[['Days']]
    y = data[price_type]

    # Train model
    model = LinearRegression()
    model.fit(X, y)

    # Predict next 7 days
    last_day = data['Days'].iloc[-1]
    future_days = np.array([last_day + i for i in range(1, 8)]).reshape(-1, 1)
    future_dates = [data['Date'].iloc[-1] + pd.Timedelta(days=i) for i in range(1, 8)]
    future_preds = model.predict(future_days)

    # Plot actual + predicted
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], y, label='Historical', color='blue')
    plt.plot(future_dates, future_preds, label='Predicted (Next 7 Days)', color='orange', linestyle='--', linewidth=3, marker='o')

    for i in range(len(future_dates)):
        plt.annotate(f"{future_preds[i]:.2f}", (future_dates[i], future_preds[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='orange')

    plt.title(f'{company} - {price_type} Price with Prediction')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.gcf().autofmt_xdate()
    plt.show()

# --- Tkinter GUI ---
root = tk.Tk()
root.title("AI Stock Price Predictor")
root.geometry("400x200")

company_label = ttk.Label(root, text="Select Company:")
company_label.pack(pady=5)
company_combo = ttk.Combobox(root, values=companies, state='readonly')
company_combo.pack(pady=5)
company_combo.current(0)

price_label = ttk.Label(root, text="Select Price Type:")
price_label.pack(pady=5)
price_combo = ttk.Combobox(root, values=price_types, state='readonly')
price_combo.pack(pady=5)
price_combo.current(3)  # Default to 'Close'

plot_button = ttk.Button(root, text="Show Prediction", command=lambda: plot_data(company_combo.get(), price_combo.get()))
plot_button.pack(pady=20)

root.mainloop()
