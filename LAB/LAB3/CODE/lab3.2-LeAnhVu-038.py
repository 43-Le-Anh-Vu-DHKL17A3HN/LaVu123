import pandas as pd

file_path = r'D:\\DHKL17A3\\LAB\\LAB3\\DATA\\stocks1.csv'
stocks1 = pd.read_csv(file_path)

print('kiem tra null :',stocks1.isnull())

mean_high = stocks1['high'].mean()
stocks1['high'].fillna(mean_high, inplace=True)

mean_low = stocks1['low'].mean() 
stocks1['low'].fillna(mean_low, inplace=True)

print('thông tin tổng quan :',stocks1.info())
