import numpy as np

nhietdohangngay = np.random.uniform(5, 35, 30)

lamtron = np.round(nhietdohangngay, 2)

nhietdotrungbinh = np.mean(lamtron)

print("Nhiệt độ hàng ngày trong tháng:",lamtron)
print("Nhiệt độ trung bình trong tháng:",nhietdotrungbinh)

ngay_nhiet_do_cao_nhat = np.max(lamtron)
ngay_nhiet_do_thap_nhat = np.min(lamtron)

print("ngày có nhiệt độ cao nhất :",ngay_nhiet_do_cao_nhat)
print("ngày có nhiệt độ thấp nhất :",ngay_nhiet_do_thap_nhat)

chenh_lech_nhiet_do = np.abs(np.diff(lamtron))
ngay_bien_doi_cao_nhat = np.argmax(chenh_lech_nhiet_do)

print("ngày có sự biến đổi nhiệt độ cao nhất :",ngay_bien_doi_cao_nhat)

ngaynhietdotren20 = np.where(lamtron > 20)[0] +1
print("ngày nhiệt độ trên 20 độ :",ngaynhietdotren20)

nhietdongay = [4,9,14,19]
nhietdocuthe = lamtron[nhietdongay]
print("nhiệt độ ngày 5,10,15,20 :",nhietdocuthe)

ngaynhietdotrentb = np.where(lamtron > nhietdotrungbinh)[0] +1
nhietdotrentb = lamtron[lamtron > nhietdotrungbinh]
print('ngày có nhiệt độ trên trung bình :',ngaynhietdotrentb)
print('nhiệt độ trên trung bình:',nhietdotrentb)

ngaychan = np.arange(0,30,2)
nhietdongaychan = lamtron[ngaychan]
print('nhiệt độ ngày chẵn :',nhietdongaychan)

ngayle = np.arange(1,30,2)
nhietdongayle = lamtron[ngayle]
print('Nhiệt độ ngày lẻ :',nhietdongayle)


