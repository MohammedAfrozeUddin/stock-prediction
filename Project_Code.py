

%%writefile app.py
import streamlit as st
from datetime import date
import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go

start = "2017-01-01"
today = date.today().strftime("%Y-%m-%d")
st.title("STOCK PRICE PREDECTOR")
stocks = ('RIVN','META','RBLX','CPNG','U')
selected_stocks = st.selectbox("selected data set for the prediction ",stocks)
n_years = st.slider("Select no of years",1,4)
period = n_years*365

def load_data(ticker):
  data = yf.download(ticker,start,today)
  data.reset_index(inplace=True)
  return data

data_load_state = st.text("loading data")
data = load_data(selected_stocks)
data_load_state.text("Loading data .... Done")

st.subheader("RAW DATA")
st.write(data.head())

def plot_raw_data():
  fig = go.Figure()
  fig.add_trace(go.Scatter(x=data['Date'],y=data['Open'],name="Open stock"))
  fig.add_trace(go.Scatter(x=data['Date'],y=data['Close'],name="Close stock"))
  fig.layout.update(title_text='Time series with ragesliders',xaxis_rangeslider_visible=True)
  st.plotly_chart(fig)

plot_raw_data()
# **** My name ****
st.write("Mohammed Afroze Uddin")

df_train = data[['Date','Close']]
df_train = df_train.rename(columns={"Date": "ds","Close":"y"})

m=Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

st.subheader("Forecast Data")
st.write(forecast.tail())

st.write(f"Forecast plot for {n_years} years")
fig1 = plot_plotly(m,forecast)
st.plotly_chart(fig1)

# Installation of packages

!pip install streamlit
!pip install yfinance
!pip install pystan~=2.14
!pip install fbprophet


# Project execution

!streamlit run app.py & npx localtunnel --port 8501