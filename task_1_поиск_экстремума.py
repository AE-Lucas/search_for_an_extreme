# -*- coding: utf-8 -*-
"""Task_1_Поиск_экстремума.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LVxDOACnmBcw0nv_ma50uqdOg3htYGDp
"""

from sympy import *
x,y = symbols('x y')
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt



class Extremums:
  """
    Класс для поиска и визуализации экстремумов
    
    Methods
    -------
    extremum(self)
        Безусловный экстремум. Находит все критические точки и определяет их типы
    lagrange(self)
        Условный экстремум. Находит все критические точки и определяет их типы  
    visualize(self)
        Строит график целевой функции и наносит на него найденные критические точки
  """
  def __init__(self, variables, function, x_res = [-1000,1000], y_res = [-1000,1000], g = None):
    assert len(variables) !=0
    self.variables = variables
    self.function = function
    self.x_res = x_res
    self.y_res = y_res
    if g != None:
      self.g = g

  def extremum(self):
    self.decision = []
    self.x,self.y=symbols(self.variables)

    self.f = self.function.subs({x:self.x,y:self.y})

    # Анализируемая функция f  для переменных x,y 
    # Необходимые условия экстремума
    self.fx=self.f.diff(self.x)	
    self.fy=self.f.diff(self.y)
    try:
            self.sols=solve([self.fx,self.fy],self.x,self.y)
    except:
            self.decision.append([' Функция не дифференцируема'])
            raise SystemExit(1)
    # Стационарная точка M(x,y) - sols
    # Вторые производные в точке М
    if type(self.sols)==dict:
      self.sols = [tuple([self.sols[x],self.sols[y]])] 
    for i in range(len(self.sols)):
      self.dec = []
      self.cr_1 = float('{:.3f}'.format(float(self.sols[i][0])))
      self.cr_2 = float('{:.3f}'.format(float(self.sols[i][1])))
      if self.cr_1 < self.x_res[0] or self.cr_1 > self.x_res[1] or self.cr_2 < self.y_res[0] or self.cr_2 > self.y_res[1]:
        self.decision.append(['Не удовлетворяет ограничению'])
      else:  
        self.fxx=self.f.diff(self.x,x).subs({x:self.cr_1,y:self.cr_2})
        self.fxx = float('{:.3f}'.format(float(self.fxx)))
        self.fxy=self.f.diff(self.x,y).subs({x:self.cr_1,y:self.cr_2})
        self.fxy = float('{:.3f}'.format(float(self.fxy)))  
        self.fyy=self.f.diff(self.y,y).subs({x:self.cr_1,y:self.cr_2})
        self.fyy = float('{:.3f}'.format(float(self.fyy)))  
        self.fyx=self.fxy;# равенства из условия симметричности матрицы Гессе
        # Расчёт определителей матрицы Гессе
        self.d1=self.fxx
        # Определитель М1 = d1
        self.M2=Matrix([[self.fxx,self.fxy],[self.fyx,self.fyy]])
        #Матрица М2 = M2
        self.d2=self.M2.det()
        self.d2 = float('{:.3f}'.format(float(self.d2)))   
        #Определитель М2 = d2
        #Достаточные условия экстремума
        if  self.d2<0 :
          self.dec = [self.cr_1,self.cr_2, 'Нет экстремума']
        elif self.d2>0 and self.d1>0:
          self.dec = [self.cr_1,self.cr_2, 'Минимум']
        elif self.d2>0 and self.d1<0:
          self.dec = [self.cr_1,self.cr_2, 'Максимум']     
        elif  self.d3==0:
          self.dec = [self.cr_1,self.cr_2, 'Седловая точка']
        self.decision.append(self.dec)
    return(self.decision)

  def lagrange(self):
    self.decision = []
    self.x,self.y=symbols(self.variables)
    self.w = Symbol('w')
    self.f = self.function.subs({x:self.x,y:self.y}) 
    self.g = self.g.subs({x:self.x,y:self.y}) 
    # Вспомогательная функция Лагранжа
    self.z = self.f + self.w*self.g
    # Производные 
    self.fx = self.z.diff(self.x)
    self.fy = self.z.diff(self.y)
    self.fw = self.z.diff(self.w)
    try:
      self.sols = solve([self.fx,self.fy,self.fw],self.x,self.y,self.w)
    except:
      self.decision.append([' Функция не дифференцируема'])
      raise SystemExit(1)
    # Стационарная точка M(x,y) - sols
    if type(self.sols)==dict:
      self.sols = [tuple([self.sols[x],self.sols[y]])] 
    for i in range(len(self.sols)):
      self.dec = []
      self.cr_1 = float('{:.3f}'.format(float(self.sols[i][0])))
      self.cr_2 = float('{:.3f}'.format(float(self.sols[i][1])))
      if self.cr_1 < self.x_res[0] or self.cr_1 > self.x_res[1] or self.cr_2 < self.y_res[0] or self.cr_2 > self.y_res[1]:
        self.decision.append(['Не удовлетворяет ограничению'])
      else:  
        self.fxx=self.f.diff(self.x,x).subs({x:self.cr_1,y:self.cr_2})
        self.fxx = float('{:.3f}'.format(float(self.fxx)))
        self.fxy=self.f.diff(self.x,y).subs({x:self.cr_1,y:self.cr_2})
        self.fxy = float('{:.3f}'.format(float(self.fxy)))  
        self.fyy=self.f.diff(self.y,y).subs({x:self.cr_1,y:self.cr_2})
        self.fyy = float('{:.3f}'.format(float(self.fyy)))  

        self.d2f = self.fxx + 2*self.fxy + self.fyy
        #Достаточные условия экстремума
        if  self.d2f>0 :
          self.dec = [self.cr_1,self.cr_2, 'Минимум']
        elif self.d2f<0 :
          self.dec = [self.cr_1,self.cr_2, 'Максимум']     
        else:
          self.dec = [self.cr_1,self.cr_2, 'Стационарная точка']
        self.decision.append(self.dec)
    return(self.decision)

func = Extremums('x y', y*(x**2)+x*(y**3) - x*y ,x_res=[-10,10],y_res=[-1,1])
func.extremum()

func2 = Extremums('x y', x*y ,x_res=[-10,10],y_res=[-1,1], g = x**2+4*y**2 - 1)
func2.lagrange()

func2 = Extremums('x y', 5- 3*x- 4*y , g = x**2+y**2-25)
func2.lagrange()