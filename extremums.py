# -*- coding: utf-8 -*-
"""extremums.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LVxDOACnmBcw0nv_ma50uqdOg3htYGDp
"""

from sympy import *
x,y = symbols('x y')
import numpy as np
import pandas as pd

import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots

'''
Поиск безусловного и условного экстремума
'''

def extremum(variables, function, x_res = [-1000,1000], y_res = [-1000,1000], g = None):
  '''
  variables: str
    Входная строка с переменными
  function: sympy.function
    Функция
  x_res: list
    Ограничение на x
  y_res: list
    Ограничения на y
  g: sympy.function
    Функция ограничения

  Result: list
    Список координат точек
  '''

  decision = []
  x,y=symbols(variables)

  f = function.subs({x:x,y:y})

  # Анализируемая функция f  для переменных x,y 
  # Необходимые условия экстремума
  fx=f.diff(x)	
  fy=f.diff(y)
  try:
          sols=solve([fx,fy],x,y)
  except:
          decision.append([' Функция не дифференцируема'])
          raise SystemExit(1)
  # Стационарная точка M(x,y) - sols
  # Вторые производные в точке М
  if type(sols)==dict:
    sols = [tuple([sols[x],sols[y]])] 
  for i in range(len(sols)):
    dec = []
    cr_1 = float('{:.3f}'.format(float(sols[i][0])))
    cr_2 = float('{:.3f}'.format(float(sols[i][1])))
    if cr_1 < x_res[0] or cr_1 > x_res[1] or cr_2 < y_res[0] or cr_2 > y_res[1]:
      decision.append(['Не удовлетворяет ограничению'])
    else:  
      fxx=f.diff(x,x).subs({x:cr_1,y:cr_2})
      fxx = float('{:.3f}'.format(float(fxx)))
      fxy=f.diff(x,y).subs({x:cr_1,y:cr_2})
      fxy = float('{:.3f}'.format(float(fxy)))  
      fyy=f.diff(y,y).subs({x:cr_1,y:cr_2})
      fyy = float('{:.3f}'.format(float(fyy)))  
      fyx=fxy;# равенства из условия симметричности матрицы Гессе
      # Расчёт определителей матрицы Гессе
      d1=fxx
      # Определитель М1 = d1
      M2=Matrix([[fxx,fxy],[fyx,fyy]])
      #Матрица М2 = M2
      d2=M2.det()
      d2 = float('{:.3f}'.format(float(d2)))   
      #Определитель М2 = d2
      #Достаточные условия экстремума
      if  d2<0 :
        dec = [cr_1,cr_2, 'Нет экстремума']
      elif d2>0 and d1>0:
        dec = [cr_1,cr_2, 'Минимум']
      elif d2>0 and d1<0:
        dec = [cr_1,cr_2, 'Максимум']     
      elif  d3==0:
        dec = [cr_1,cr_2, 'Седловая точка']
      decision.append(dec)
  return(decision)

def lagrange(variables, function, x_res = [-1000,1000], y_res = [-1000,1000], g = None):

  '''
  variables: str
    Входная строка с переменными
  function: sympy.function
    Функция
  x_res: list
    Ограничение на x
  y_res: list
    Ограничения на y
  g: sympy.function
    Функция ограничения

  Result: list
    Список координат точек
  '''

  decision = []
  x,y=symbols(variables)
  w = Symbol('w')
  f = function.subs({x:x,y:y}) 
  g = g.subs({x:x,y:y}) 
  # Вспомогательная функция Лагранжа
  z = f + w*g
  # Производные 
  fx = z.diff(x)
  fy = z.diff(y)
  fw = z.diff(w)
  try:
    sols = solve([fx,fy,fw],x,y,w)
  except:
    decision.append([' Функция не дифференцируема'])
    raise SystemExit(1)
  # Стационарная точка M(x,y) - sols
  for i in range(len(sols)):
    dec = []
    cr_1 = float('{:.3f}'.format(float(sols[i][0])))
    cr_2 = float('{:.3f}'.format(float(sols[i][1])))
    la = float('{:.3f}'.format(float(sols[i][2])))
    if cr_1 < x_res[0] or cr_1 > x_res[1] or cr_2 < y_res[0] or cr_2 > y_res[1]:
      decision.append(['Не удовлетворяет ограничению'])
    else:  
      fxx=z.diff(x,x).subs({x:cr_1,y:cr_2,w:la})
      fxx = float('{:.3f}'.format(float(fxx)))
      fxy=z.diff(x,y).subs({x:cr_1,y:cr_2,w:la})
      fxy = float('{:.3f}'.format(float(fxy)))  
      fyy=z.diff(y,y).subs({x:cr_1,y:cr_2,w:la})
      fyy = float('{:.3f}'.format(float(fyy)))  

      d2f = fxx + 2*fxy + fyy
      #Достаточные условия экстремума
      if  d2f>0 :
        dec = [cr_1,cr_2, 'Минимум']
      elif d2f<0 :
        dec = [cr_1,cr_2, 'Максимум']     
      else:
        dec = [cr_1,cr_2, 'Стационарная точка']
      decision.append(dec)
  return(decision)

def vizualize(variables, function, x_res = [-1000,1000], y_res = [-1000,1000], g = None):
  '''
  variables: str
    Входная строка с переменными
  function: sympy.function
    Функция
  x_res: list
    Ограничение на x
  y_res: list
    Ограничения на y
  g: sympy.function
    Функция ограничения

  fig: graph
    график
  '''
   
  x,y=symbols(variables)

  f = function.subs({x:x,y:y})

  x_ = np.round(np.arange(x_res[0],x_res[1], 0.1),2)
  y_ = np.round(np.arange(y_res[0],y_res[1], 0.1),2)
  z_ = []

  X, Y = np.meshgrid(x_, y_)
  for j in range(len(y_)):
    ax  = []
    for i in range(len(x_)):
      ax.append(float(function.subs({x:x_[i],y:y_[j]})))
    z_.append(ax)

  Z = np.array(z_)

  Points = extremum(variables = variables, function = function ,x_res=x_res,y_res=y_res,g = g)

  x_points = []
  y_points = []
  z_points = []

  for i in Points:
    x_points.append(i[0])
    y_points.append(i[1])


  for j in range(len(y_points)):
    z_points.append(float(function.subs({x:x_points[j],y:y_points[j]})))


  fig = go.Figure()
  fig.add_trace(go.Surface(x=X,y=Y,z=Z,colorscale='Viridis'))
  fig.add_trace(go.Scatter3d(x=x_points,y=y_points,z=z_points,mode='markers')) 
  fig.update_layout(scene = dict(xaxis_title='X, у.е.',yaxis_title='Y, у.е.',zaxis_title='Z, у.е.'),title_text='F(x,y)= '+str(function),height=600)
  fig.show()

def vizualize_lagrange(variables, function, x_res = [-1000,1000], y_res = [-1000,1000], g = None):
  '''
  variables: str
    Входная строка с переменными
  function: sympy.function
    Функция
  x_res: list
    Ограничение на x
  y_res: list
    Ограничения на y
  g: sympy.function
    Функция ограничения

  fig: graph
    график
  '''

  x,y=symbols(variables)

  f = function.subs({x:x,y:y})
  g = g.subs({x:x,y:y})

  x_ = np.round(np.arange(x_res[0],x_res[1], 0.1),2)
  y_ = np.round(np.arange(y_res[0],y_res[1], 0.1),2)
  z_ = []

  X, Y = np.meshgrid(x_, y_)
  for j in range(len(y_)):
    ax  = []
    for i in range(len(x_)):
      ax.append(float(function.subs({x:x_[i],y:y_[j]})))
    z_.append(ax)

  Z = np.array(z_)

  Points = lagrange(variables = variables, function = function ,x_res=x_res,y_res=y_res,g = g)

  x_points = []
  y_points = []
  z_points = []

  for i in Points:
    x_points.append(i[0])
    y_points.append(i[1])


  for j in range(len(y_points)):
    z_points.append(float(function.subs({x:x_points[j],y:y_points[j]})))

  z_g = []
  for j in range(len(y_)):
    ax  = []
    for i in range(len(x_)):
      ax.append(float(g.subs({x:x_[i],y:y_[j]})))
    z_g.append(ax)

  Z_g = np.array(z_g)


  fig = go.Figure()
  fig.add_trace(go.Surface(x=X,y=Y,z=Z,colorscale='Viridis'))
  fig.add_trace(go.Surface(x=X,y=Y,z=Z_g,showscale=False))
  fig.add_trace(go.Scatter3d(x=x_points,y=y_points,z=z_points,mode='markers')) 
  fig.update_layout(scene = dict(xaxis_title='X, у.е.',yaxis_title='Y, у.е.',zaxis_title='Z, у.е.'),title_text='F(x,y)= '+str(function),height=600)
  fig.show()

def user_input():
  '''
  Пользовательский ввод
  '''


  print('Введите переменные в формате:')
  print('x y')
  variables_1 = input()

  print('Введите функцию в формате:')
  print('x*y')
  f_1 = sympify(input())

  print('Добавить ограничение на х?')
  print('Yes/No')
  answer_1 = input()
  if answer_1 == 'Yes':
    print('Введите ограничение в формате:')
    print('-1')
    print('1')
    x_res_1 = []
    x_res_1.append(int(input()))
    x_res_1.append(int(input()))
  else:
    x_res_1 = [-1000,1000]   

  print('Добавить ограничение на y?')
  print('Yes/No')
  answer_2 = input()
  if answer_2 == 'Yes':
    print('Введите ограничение в формате:')
    print('-1')
    print('1')
    y_res_1 = []
    y_res_1.append(int(input()))
    y_res_1.append(int(input()))
  else:
    y_res_1 = [-1000,1000]   
       
  print('Добавить функцию g?')
  print('Yes/No')
  answer_3 = input()
  if answer_3 == 'Yes':
    print('Введите функцию g в формате:')
    print('x*y')
    g_1 = sympify(input())
  else:
    g_1 = None
  if g_1 == None:
    result = extremum(variables_1,f_1,x_res_1,y_res_1,g_1) 
    for i in result:
      print(i)
    grafic = vizualize(variables_1,f_1,x_res_1,y_res_1,g_1)
    print(grafic)
  else:
    result = lagrange(variables_1,f_1,x_res_1,y_res_1,g_1) 
    for i in result:
      print(i)
    grafic = vizualize_lagrange(variables_1,f_1,x_res_1,y_res_1,g_1)
    print(grafic)