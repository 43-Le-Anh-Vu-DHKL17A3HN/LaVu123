import pandas as pd

file_path = r'D:\\DHKL17A3\\LAB\\LAB3\\DATA\\stocks1.csv'
stocks1 = pd.read_csv(file_path)

print('5 dòng đầu :',stocks1.head())
print('kiểu dữ liệu :',stocks1.dtypes)
print('thong tin tong quan :',stocks1.info)