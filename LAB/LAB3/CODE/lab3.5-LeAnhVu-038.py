import pandas as pd

file_path_1 = r'D:\\DHKL17A3\\LAB\\LAB3\\DATA\\stocks1.csv'
file_path_2 = r'D:\\DHKL17A3\\LAB\\LAB3\\DATA\\stocks2.csv'

stocks1 = pd.read_csv(file_path_1)
stocks2 = pd.read_csv(file_path_2)

stocks = pd.concat([stocks1,stocks2])
print(stocks)

stocks.set_index(['date', 'symbol'], inplace=True)

print("DataFrame sau khi tạo MultiIndex:",stocks.head())

grouped_stocks = stocks.groupby(['date', 'symbol']).mean()

print("DataFrame sau khi GroupBy và tính trung bình:",grouped_stocks.head())

sorted_stocks = grouped_stocks.sort_index(level=['date', 'symbol'])

print("DataFrame sau khi sắp xếp:",sorted_stocks.head())

print("Kết quả cho 5 ngày đầu tiên:",sorted_stocks.head(5))

