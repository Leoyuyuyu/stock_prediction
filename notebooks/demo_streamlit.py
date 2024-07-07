### Import libraries
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from tqdm import tqdm
from statsmodels.tsa.arima.model import ARIMA
import numpy as np

# Title of the application
st.title('Apple Stock Investment')

st.write('## My last work in the BS bootcamp :sob:')

# Load data into a DataFrame
apple_stock = pd.read_csv(r'C:\Users\12436\Desktop\BrainStation\Capstone project\capstone-Leoyuyuyu\data\apple_stock.csv', index_col=0)
apple_stock.index = pd.to_datetime(apple_stock.index).date
# Display the DataFrame in the app
st.dataframe(apple_stock)

# Split the data into training and testing sets
initial_date = st.date_input('Initial date', value=pd.to_datetime('2023-02-01'))
train = apple_stock[apple_stock.index <= initial_date]
test = apple_stock[apple_stock.index > initial_date]

# Convert '5-Day Return' to list for training
history = train['5-Day Return'].tolist()
predictions = []
threshold_5days = []

Market_idea = st.slider('Rate your Prudence', min_value=0, max_value=10, value=0)

for t in tqdm(range(len(test)), desc="Processing"):  # Adjust the range to avoid index error
    # Fit the ARIMA model
    model = ARIMA(history[-300:], order=(7, 0, 0))
    model_fit = model.fit()
    
    # Forecast 5 days ahead
    output = model_fit.forecast(steps=5)
    yhat = output[-1]  # Take the 5th day forecast from the current point
    predictions.append(yhat)
    
    # Calculate moving average and standard deviation for the last 5 days
    if len(history) >= 5:
        moving_avg_5days = pd.Series(history[-5:]).mean()
        moving_std_5days = pd.Series(history[-5:]).std()
        threshold_5days.append(moving_avg_5days + (Market_idea/10)*moving_std_5days)
    
    # Get the actual value from the test set
    obs = test['5-Day Return'].iloc[t]
    history.append(obs)



# Backtesting Function with Bankruptcy Check
def backtest(df, initial_capital=10000, invest=500):
    capital = initial_capital
    df_capital = pd.DataFrame(index=df.index, columns=['Capital'])
    df_capital['Capital'] = 0
    
    for i in range(len(df)):

        if df['predicted binary'].iloc[i] == 1:
            if capital < invest:
                capital = 0
                current_invest = capital
            else:
                capital -= invest
                current_invest = invest

            capital_change = current_invest * (df['real return'].iloc[i] + 1)
            capital += capital_change
        
        if capital <= 0:
            df_capital['Capital'].iloc[i] = 0
            return f"You are bankrupted at {df.index[i].strftime('%Y-%m-%d')}", df_capital
        
        df_capital['Capital'].iloc[i] = capital
    
    return f"You have survived until {df.index[-1].strftime('%Y-%m-%d')}", df_capital

# df5 to be created 

df5 = pd.DataFrame(data=predictions, index=test.index, columns=['predicted return compared with today'])
df5['predicted return compared with today_shifted'] = df5['predicted return compared with today'].shift(4)
df5['real return'] =  test['5-Day Return']
df5['threshold'] = threshold_5days
df5['threshold'] = df5['threshold'].shift(4)
df5.dropna(inplace=True, axis=0)
df5['predicted binary'] = np.where((df5['predicted return compared with today_shifted'] >0) & (df5['predicted return compared with today_shifted'] >df5['threshold']), 1, 0)
df5['actual binary'] = np.where(df5['real return']>0, 1, 0)

initial_capital = st.number_input('Initial Capital', value=10000)
invest = st.number_input('Investment Amount', value=500)



# Apply Backtest
backtest_result, backtested_df = backtest(df5, initial_capital, invest)
st.write(backtest_result)

# Plot the capital over time
st.line_chart(backtested_df['Capital'])