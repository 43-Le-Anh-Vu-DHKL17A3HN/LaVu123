import math

class PS:
    def __init__(self,tu_so = 0, mau_so = 1):
        self.tu_so = tu_so
        self.mau_so = mau_so
        self.kiem_tra()
        
    def kiem_tra(self):
        if self.mau_so == 0:
            return False
        print(f"Mau so khong duoc bang = 0!")
        
    def nhap_phan_so(self):
        self.tu_so = int(input("Nhap tu so :"))
        self.mau_so = int(input("Nhap mau so :"))
        self.kiem_tra()
        
    def in_ra_man_hinh(self):
        print(f"Phan so : {self.tu_so}/{self.mau_so}")
        
    def rut_gon(self):
        ucln = math.gcd(self.tu_so,self.mau_so)
        self.tu_so //= ucln
        self.mau_so //= ucln
        
if __name__ == "__main__":
    ps = PS()
    ps.nhap_phan_so()
    ps.in_ra_man_hinh()
    ps.rut_gon()
    
        
        
    
            
        