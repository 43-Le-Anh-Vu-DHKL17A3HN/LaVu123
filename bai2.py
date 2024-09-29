class lopTS:
    def __init__(self,ho_ten="",diem_toan=0,diem_li=0,diem_hoa=0):
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_li = diem_li
        self.diem_hoa = diem_hoa
        
    def nhap_thong_tin(self):
        self.ho_ten = input("Nhap ho va ten :")
        self.diem_toan = float("Nhap diem toan :")
        self.diem_li = float("Nhap diem li :")
        self.diem_hoa = float("Nhap diem hoa :")
        
    def in_thong_tin(self):
        print(f"Ho ten : {self.ho_ten}")
        print(f"Diem toan : {self.diem_toan}")
        print(f"Diem li : {self.diem_li}")
        print(f"Diem hoa : {self.diem_hoa}")
        
    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_li + self.diem_hoa
    
if __name__ == "__main__" :
    danh_sach = []
    so_luong = int(input("Nhap so luong thi sinh :"))
    

