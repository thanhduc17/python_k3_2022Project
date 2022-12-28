# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 10:05:12 2022

@author: Duc
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import cos,sin,pi

def cau31(x, y):
  z = (x/3)**2 - (y/2)**2
  return z
def x12():
  x = np.linspace(start=-5, stop=7,num=10)
  return x
def  y12():
  y = np.linspace(start=-5, stop=5,num=10)
  return y
def ve_3ds(x,y,z):
  
  fig, ax =plt.subplots(subplot_kw={"projection":"3d"})

  rosen_surf = ax.plot_surface(x, y, z,cmap=cm.gist_heat_r,linewidth=0, antialiased=False)

  ax.set_zlim(-6,6)

  fig.colorbar(rosen_surf, shrink=0.5,aspect=5)

  plt.show()

def main():
  x_1 = x12()
  y_1 = y12()
  x_2, y_6 = np.meshgrid(x_1, y_1)
  z = cau31(x_2, y_6)
  ve_3ds(x_2,y_6,z)

if __name__ == "__main__":
  main()