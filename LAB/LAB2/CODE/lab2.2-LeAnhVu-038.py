import pandas as pd
import numpy as np

path = r'D:\\DHKL17A3\\LAB\\LAB2\\DATA\\diem_hoc_phan.csv'
df = pd.read_csv(path)

print("5 dòng đầu tiên của DataFrame:",df.head())

data_list = df.values.tolist()

data_numpy = np.array(data_list)

print("Dữ liệu dưới dạng list:",data_list)


print("Dữ liệu dưới dạng mảng NumPy:",data_numpy)

data_array = np.array(data_list)
print(data_array)

cot_diem = data_array[:,2:].astype(float)

def diem_tin_chi(diem):
    if 8.5<= diem <= 10:
        return 'A'
    elif 8.0 <= diem <= 8.4:
        return 'B+'
    elif 7 <= diem < 8:
        return 'B'
    elif 6.5 <= diem < 7:
        return 'C+'
    elif 5.5<= diem < 6:
        return 'C'
    elif 5.0 <= diem < 5:
        return 'D+'
    elif 4<= diem < 5:
        return 'D'
    else:
        return 'F'
    
quy_doi_diem = np.vectorize(diem_tin_chi)(cot_diem)
print("Diem tin chi:",quy_doi_diem)

hp1 = quy_doi_diem[:,0]
hp2 = quy_doi_diem[:,1]
hp3 = quy_doi_diem[:,2]

print("diem hoc phan 1 :",hp1)
print("diem hoc phan 2 :",hp2)
print("diem hoc phan 3 :",hp3)

total_hp1 = df['HP 1'].sum()
total_hp2 = df['HP 2'].sum()
total_hp3 = df['HP 3'].sum()

mean_hp1 = df['HP 1'].mean()
mean_hp2 = df['HP 2'].mean()
mean_hp3 = df['HP 3'].mean()

std_hp1 = df['HP 1'].std()
std_hp2 = df['HP 2'].std()
std_hp3 = df['HP 3'].std()

print(f"Tổng điểm HP 1: {total_hp1}, Trung bình: {mean_hp1:.2f}, Độ lệch chuẩn: {std_hp1:.2f}")
print(f"Tổng điểm HP 2: {total_hp2}, Trung bình: {mean_hp2:.2f}, Độ lệch chuẩn: {std_hp2:.2f}")
print(f"Tổng điểm HP 3: {total_hp3}, Trung bình: {mean_hp3:.2f}, Độ lệch chuẩn: {std_hp3:.2f}")






    
    

    

    
        
