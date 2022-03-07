# search_for_an_extreme

Онлайн Google Colab Notebook - https://colab.research.google.com/drive/1WqOLCdNS66hnVWRylH2aMamRQ_Heh3If?usp=sharing

# documentation


1)	def extremum(variables, function, x_res = [-1000,1000], y_res = [-1000,1000], g = None):
Поиск экстремума функции с заданными параметрами. 
Ограничивающая функция и ограничения переменных устанавливаются.
   
	
   Variables

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

    Returns
     
    Result: list
	Список координат точек


2)	def lagrange(variables, function, x_res = [-1000,1000], y_res = [-1000,1000], g = None):

Поиск экстремума функции с заданными параметрами. 
Ограничивающая функция и ограничения переменных устанавливаются.
   
   Variables

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

    Returns
     
    Result: list
	Список координат точек





3)	def vizualize(variables, function, x_res = [-1000,1000], y_res = [-1000,1000], g = None):
Визуализация функции с точками. 
Границы графика и детализация настраиваются.

   Variables

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

    Returns
     
    fig: graph
	график

4)	def vizualize_lagrange(variables, function, x_res = [-1000,1000], y_res = [-1000,1000], g = None):
Визуализация функции с точками. 
Границы графика и детализация настраиваются.
	
   Variables

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

    Returns
     
    fig: graph
	график
  
  
5)	def user_input():

Пользовательский ввод

