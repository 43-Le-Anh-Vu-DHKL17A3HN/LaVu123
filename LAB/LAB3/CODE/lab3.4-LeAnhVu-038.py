import pandas as pd

file_path_1 = r'D:\\DHKL17A3\\LAB\\LAB3\\DATA\\stocks1.csv'
file_path_2 = r'D:\\DHKL17A3\\LAB\\LAB3\\DATA\\stocks2.csv'
file_path_companies = r'D:\\DHKL17A3\\LAB\\LAB3\\DATA\\companies.csv'

companies = pd.read_csv(file_path_companies)
stocks1 = pd.read_csv(file_path_1)
stocks2 = pd.read_csv(file_path_2)

stocks = pd.concat([stocks1,stocks2])
print(stocks)

print("5 dong dau :",companies.head())

ket_hop_data = pd.merge(stocks,companies,on='symbol')





