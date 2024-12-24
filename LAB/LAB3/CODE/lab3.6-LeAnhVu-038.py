import pandas as pd

file_path_1 = r'D:\\DHKL17A3\\LAB\\LAB3\\DATA\\stocks1.csv'
file_path_2 = r'D:\\DHKL17A3\\LAB\\LAB3\\DATA\\stocks2.csv'

stocks1 = pd.read_csv(file_path_1)
stocks2 = pd.read_csv(file_path_2)

stocks = pd.concat([stocks1,stocks2])
print(stocks)

pivot_table = stocks.pivot_table(values='close', index='date', columns='symbol', aggfunc='mean')

print("Pivot Table:",pivot_table.head())

total_volume = stocks.groupby('symbol')['volume'].sum()

pivot_table_df = pivot_table.reset_index()

pivot_table_df = pivot_table_df.join(total_volume, on='symbol', rsuffix='_total')

print("Pivot Table sau khi thêm cột tổng volume:",pivot_table_df.head())

sorted_pivot_table_df = pivot_table_df.sort_values(by='volume_total', ascending=False)

print("Pivot Table sau khi sắp xếp:",sorted_pivot_table_df.head())

print("5 mã chứng khoán có tổng volume giao dịch cao nhất:",sorted_pivot_table_df.head(5))

