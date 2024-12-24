import numpy as np

file_path_efficiency = r'D:\\DHKL17A3\\LAB\\LAB2\\DATA\\efficiency.txt'
file_path_shifts = r'D:\\DHKL17A3\\LAB\\LAB2\\DATA\\shifts.txt'

with open(file_path_efficiency, 'r') as file:
    efficiency = [int(line.strip()) for line in file]

with open(file_path_shifts, 'r') as file:
    shifts = [line.strip() for line in file]

print("Dữ liệu từ file efficiency.txt:",efficiency)
print("Dữ liệu từ file shifts.txt:",shifts)

np_shifts = np.array(shifts)

print("Kiểu dữ liệu của np_shifts:",np_shifts.dtype)

np_efficiency = np.array(efficiency)

print("Kiểu dữ liệu của np_efficiency:",np_efficiency.dtype)

morning_efficiency = np_efficiency[np_shifts == 'Morning']
average_morning_efficiency = np.mean(morning_efficiency)
print(f"\nHiệu suất sản xuất trung bình của ca 'Morning': {average_morning_efficiency:.2f}")

other_shifts_efficiency = np_efficiency[np_shifts != 'Morning']
average_other_shifts_efficiency = np.mean(other_shifts_efficiency)
print(f"\nHiệu suất sản xuất trung bình của các ca khác: {average_other_shifts_efficiency:.2f}")


