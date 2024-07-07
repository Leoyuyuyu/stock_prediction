[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15133405&assignment_repo_type=AssignmentRepo)

------------------------------------------------------------------------------

## Project Title 
Stock Price Trend Forecasting With Stats/ML algos 
=========================

## Project overview 

The objective of this project is to reliably predict stock price returns using historical time series data available online. This involves employing a combination of statistical methods and machine learning regression models to achieve accurate predictions.


## Methodology
### 1. Data Collection and Preprocessing
Sources: Fetch historical stock price data from APIs such as Yahoo Finance.
Time Frame: Collect data spanning multiple years to capture various market conditions and the data granularity is daily.

### 2. Feature Engineering(optional):
Create new features such as moving averages, volatility indices, and other technical indicators.
Lagged features to incorporate past values into the prediction model for SIRIMAX.

### 3.Exploratory Data Analysis (EDA)
Visualization:
Plot stock price trends over time and check the decomposition result.
Visualize moving averages, trading volumes, and other indicators.

Statistical Analysis:
Perform descriptive statistics to summarize data characteristics.
Analyze distributions, seasonality, and autocorrelation of stock prices.

Correlation Analysis:
Heatmaps to identify correlations between different features.

#### 3. Modeling

Statistical Models:
ARIMA (AutoRegressive Integrated Moving Average): Model for univariate time series data predicting future points.
SARIMA (Seasonal ARIMA): Extension of ARIMA for handling seasonality in data. Potential Exogerous terms: Volume, index 
Prophet 

Machine Learning Models:
XGBoost: Ensemble learning method to predict the next day return.

NN models: 
LSTM.



#### 4. Model Evaluation and Selection


Performance Metrics:
Mean Absolute Error (MAE): Average magnitude of errors.
Mean Squared Error (MSE): Average squared errors to penalize larger errors.
R-squared: Proportion of variance explained by the model.

Model Selection:
Compare models based on evaluation metrics.
Select the best-performing model or ensemble of models for deployment.



#### Dataset

AAPL stock data from yfinance api from 1980 to 2024. 

Data introduction:

Open 
High 
Low
Close
Adj Close 
Volume 

Added feature:
1-day return 
5-day return 
1-Month return 
Trading volume change (weekly)


### Credits & References

... Include any personal learning

------------------------------------------------------------------------------