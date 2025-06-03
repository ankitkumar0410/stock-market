import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# from pandas_profiling import ProfileReport
data = pd.read_csv(r"C:\Users\ankit\OneDrive\Desktop\New folder\classroom\stocks.csv")
# print(data.isnull().any())
# print(data.isnull().sum())

# correlation_matrix= data.select_dtypes(include='number').corr()
# plt.figure(figsize=(15,10))
# sns.heatmap(correlation_matrix,annot=True,cmap='coolwarm',linewidths=0.5,fmt='.2f')
# plt.title("CorrelationMatrixHeatmap")
# plt.show()

# profile = ProfileReport(data, title="Stock Market Analysis")
# data['Date'] = pd.to_datetime(data['Date'])



# the distribution of the closing prices to understand their range and frequency.
# plt.hist(data['Close'], bins=20)
# plt.xlabel('Closing Price')
# plt.ylabel('Frequency')
# plt.title('Closing Price Distribution')
# plt.show()


#the cumulative volume traded over time to observe any trends or spikes.
# ticker_volume = data.groupby('Ticker')['Volume'].sum()
# ticker_volume.plot(kind='bar')
# plt.xlabel('Ticker')
# plt.ylabel('Total Volume')
# plt.title('Total Volume by Ticker')
# plt.show()




#Exploring the relationship between volume and closing prices,to identify any correlations.
# plt.scatter(data['Volume'], data['Close'])
# plt.xlabel('Volume')
# plt.ylabel('Closing Price')
# plt.title('Volume vs. Closing Price')
# plt.show()



#Illustrating the distribution of the closing prices, including the median, quartiles, and outliers.
# plt.boxplot(data['Close'])
# plt.ylabel('Closing Price')
# plt.title('Closing Price Distribution')
# plt.show()



































