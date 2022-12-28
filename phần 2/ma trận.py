# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 10:03:42 2022

@author: Duc
"""

import numpy as np
def sinh_ngau_nhien_1_vector(a,b):
  v5 = np.random.randint(low=a,high=b, size=3)
  return v5
def sinh_ngau_nhien_1_mt(a,b):
  v = np.random.randint(low=a,high=b, size=12)
  mt = v.reshape(3,4)
  return mt
def sinh_ngau_nhien_1_mt1(a,b):
  v = np.random.randint(low=a,high=b, size=20)
  mt = v.reshape(4,5)
  return mt
def main():
  a = 3
  b =12
  x = sinh_ngau_nhien_1_vector(a,b)
  y = sinh_ngau_nhien_1_mt(a,b)
  print("x =",x)
  print("A =\n",y)
  n = x@y
  print("x*A =",n)
  z = sinh_ngau_nhien_1_mt1(a,b)
  print('A*B =',y@z)
if __name__=="__main__":
  main()
