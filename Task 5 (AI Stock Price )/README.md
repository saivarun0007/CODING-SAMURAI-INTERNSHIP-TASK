# 📊 AI Stock Price Visualization 

A Python-based GUI tool to visualize historical stock prices for multiple companies from the National Stock Exchange (NSE) with AI.  
This project allows users to select companies and price types dynamically, and view historical price charts with beautiful formatting.

---

## 🚩 Objective

> **⚠ This project does NOT perform stock price prediction or forecasting.**  
> Its main purpose is to provide an interactive way to visualize historical stock data for analysis and educational purposes.

---

## ✨ Features

- 🔽 **Company Dropdown**: Select from multiple companies.
- 🔽 **Price Type Dropdown**: Choose from `Open`, `Close`, `High`, `Low` prices.
- 📈 **Interactive Charts**: Visualize historical stock data with smooth, clean graphs.
- 🗓 **Beautiful Date Formatting**: Dates are displayed in an easily readable format.
- 🎨 **Smooth & Clean UI**: Simple interface built with Python Tkinter and Matplotlib.
- 📂 **Multiple CSV Support**: Automatically reads all valid CSV files in the folder.
- 🔄 **Quick Switching**: Seamlessly switch between companies and price types for instant visualization.

---

## 🧰 Technologies Used

- 🐍 **Python 3.9+**
- 📊 **Pandas** for data manipulation
- 📉 **Matplotlib** for data visualization
- 🖥 **Tkinter** for GUI dropdown menus

---

## 📥 Dataset

- Dataset Source: **Kaggle NSE Stock Market Dataset**
- You can download the dataset from Kaggle:

  👉 [Kaggle NSE Stock Dataset](https://www.kaggle.com/datasets/)

Place your extracted CSV files in the same folder as the script.
---

## 🚀 Installation and Running

### 1️⃣ Clone or Download the Repository

---

## Install Required Python Packages

pip install pandas matplotlib

---

## 🔮 Possible Future Enhancements
Although this project does not include forecasting or predictions, the following features can be added in future versions:

✅ Stock price prediction using ML models (LSTM, ARIMA, Prophet, etc.)

✅ Add technical indicators (Moving Averages, RSI, MACD, Bollinger Bands)

✅ Export charts as images or PDFs

✅ Time-range selection (last 1 month, 6 months, 1 year)

✅ Web-based interface (using Flask or Django)

✅ Interactive charts (using Plotly or Dash)

---

## ⚠ Disclaimer

This tool is strictly for educational and research purposes.

It does NOT provide any financial advice, trading signals, or investment guidance.

Users are solely responsible for any use of the data and its interpretation.

---

## 🙏 Acknowledgements & 📚 Learning Outcome

📊 Dataset Credits: Kaggle (NSE Stock Market Dataset)

🔗 Python Open Source Libraries (Pandas, Matplotlib, Tkinter)

- Real-world data parsing and preprocessing

- Building GUI applications with Tkinter

- Data visualization with Matplotlib

- Working with multiple datasets dynamically

- Clean code organization for multi-company analysis

---

## 📌 Repository Structure

nse-stock-visualizer/
│
├── nse_stock_visualizer.py   # Main application file
├── /CSV_FILES/               # Folder containing extracted stock CSV files
├── README.md                 # This file
└── requirements.txt          # Optional: list of dependencies

---

## 🔒 License

This project is for educational and personal portfolio use.