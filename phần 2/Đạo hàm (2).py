# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 19:45:08 2022

@author: Duc
"""

from sympy import *

# 2x − 5y + z = −5
# 4x + 2y − 2z = 2
# x + y − z = 0
#(√x3 − 3x23+ √x2 − 2x)
def tinh_nguyen_ham1 (f3):
    x = symbols('x')
    answer = integrate(f3,  (x,(pi), ((2*pi)/3)))
    print("tích phân CỦA ",f3,"LÀ\n",answer)
def tinh_nguyen_ham (f2):
    x = symbols('x')
    
    answer = integrate(f2, x)
    print("tích phân CỦA ",f2,"LÀ\n",answer)
    
def tinh_dao_ham (f1):
    x = symbols('x')
    answer = diff(f1, x)
    print("ĐẠO HÀM CỦA ",f1,"LÀ\n",answer)

def tinh_gioi_han(f):
    
    x = symbols('x')

    answer = limit(f, x,oo)
    print('Kết quả giới hạn của: ',f,"là\n", answer)
def giai_he_pt(a,b,c):
    
    x, y,z = symbols('x y z')
    eq1 = Eq(a, 0)
    eq2 = Eq(b, 0)
    eq3 = Eq(c, 0)
    answer = solve((eq1, eq2, eq3), (x,y,z))
    print("nghiệm của hệ pt là:",answer)
def main():
    
    x = symbols('x')
    f3 = (1 - x*tan(x))/((x**2)*cos(x) + x)
    f2 = x / ((x**2) + 2)
    f1 = (2*x - 1)/ (x + 2)
    f = ((x**3) - 3*(x**2))**(1/3) + sqrt(x**2 - 2*x)
    x, y,z = symbols('x y z')
    a = 2*x - 5*y + z + 5
    b = 4*x + 2*y - 2*z - 2
    c = x + y - z 
    tinh_nguyen_ham1 (f3)
    tinh_nguyen_ham (f2)
    tinh_dao_ham (f1)
    tinh_gioi_han(f)
    giai_he_pt(a,b,c)
if __name__ == "__main__":
    main()     