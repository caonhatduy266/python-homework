import math

class PhanSo:
    def __init__(self, tu=0, mau=1):
        self.tu = tu
        self.mau = mau
        self.rutgon()

    def rutgon(self):
        gcd = self.tim_ucln(self.tu, self.mau)
        self.tu = self.tu 
        self.mau = self.mau 

    def tim_ucln(self, a, b):
        if b == 0:
            return a
        return self.tim_ucln(b, a % b)

    def __add__(self, other):
        tu_moi = self.tu * other.mau + other.tu * self.mau
        mau_moi = self.mau * other.mau
        return PhanSo(tu_moi, mau_moi)

    def __sub__(self, other):
        tu_moi = self.tu * other.mau - other.tu * self.mau
        mau_moi = self.mau * other.mau
        return PhanSo(tu_moi, mau_moi)

    def __mul__(self, other):
        tu_moi = self.tu * other.tu
        mau_moi = self.mau * other.mau
        return PhanSo(tu_moi, mau_moi)

    def __truediv__(self, other):
        tu_moi = self.tu * other.mau
        mau_moi = self.mau * other.tu
        return PhanSo(tu_moi, mau_moi)

    def __str__(self):
        return f"{self.tu}/{self.mau}"


a = PhanSo()
a.tu = 2
a.mau = 3
b = PhanSo(3, 5)

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")