**Stock Price Predictor**

This simple web application utilizes historical stock data and the Facebook Prophet forecasting model to predict stock prices for selected companies. Users can choose from a list of stocks, select the number of years for prediction, and visualize the forecasted stock prices. The application also provides an interactive chart displaying the historical stock data for the chosen company.

**Usage:**

1. **Select Stock and Timeframe:**
   - Choose a company from the dropdown menu to predict its stock prices (e.g., RIVN, META, RBLX, CPNG, U).
   - Adjust the slider to select the number of years into the future you want to predict (between 1 and 4 years).

2. **View Historical Data:**
   - The application displays the raw historical stock data for the selected company, showing the opening and closing prices over time.

3. **Forecast and Visualization:**
   - The application uses the Facebook Prophet model to forecast future stock prices.
   - It generates a plot showing the historical and forecasted stock prices for the selected company.

**How to Run:**

1. **Install Required Packages:**
   - Ensure you have the necessary Python packages installed: Streamlit, yfinance, pystan, and fbprophet. You can install them using the provided commands.

2. **Run the Application:**
   - Run the `app.py` file using the following command:
     ```
     streamlit run app.py
     ```

3. **Access the Web Application:**
   - Once the application is running, access it via your web browser at `http://localhost:8501`.
  
4. **Note:**
   - The application script includes installation commands for required packages. Make sure you have the required permissions to install packages if you run the script in a specific environment.

---

*Created by Mohammed Afroze Uddin*
