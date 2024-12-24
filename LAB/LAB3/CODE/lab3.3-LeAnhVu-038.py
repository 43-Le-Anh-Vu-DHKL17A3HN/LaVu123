import pandas as pd

file_path_1 = r'D:\\DHKL17A3\\LAB\\LAB3\\DATA\\stocks1.csv'
file_path_2 = r'D:\\DHKL17A3\\LAB\\LAB3\\DATA\\stocks2.csv'

stocks1 = pd.read_csv(file_path_1)
stocks2 = pd.read_csv(file_path_2)

stocks = pd.concat([stocks1,stocks2])
print(stocks)

trungbinhhigh = stocks['high'].mean()
print('trung binh cot high',trungbinhhigh)

trungbinhopen = stocks['open'].mean()
print('trung bình cột open',trungbinhopen)

trungbinhlow = stocks['low'].mean()
print('trung bình cột low',trungbinhlow)

trungbinhclose = stocks['close'].mean()
print('trung bình cột close :',trungbinhclose)

print('5 dòng đầu :',stocks.head())