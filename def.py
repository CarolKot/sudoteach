#def https://www.youtube.com/watch?v=UBkbP3fmUio&list=PLV0FNhq3XMOJSj0TfDdHxgIKDKlTwSpmg&index=6

def greet(name= 'гость'): # = гость  это функция с параметром поумолчанию
    return f'Hellow, {name}' # Функция может возвращать результат с
    # с помощью ключегого слова  return

result = greet('Carol')
print (result)

def adder(x, y):
    return x * y


result = adder(5, 5) # передаём в result значения 
print(result)

# можно сделать калькулятро
def adder(x,y, sign): # sign это просто имя аргумента #так же сверху параментры
    if sign  == '*':
        return x * y
    if sign  == '+':
        return x + y
    if sign  == '-':
        return x - y
    if sign  == '/':
        return x / y
result = adder (x=5,y=5,sign ='*') # снизу аргумкеты
print(result)

# Если я не знаю, что передавать то используется *args
def adder(*args): 
    return args  # Просто возвращаем переданные аргументы как кортеж


result = adder(1, 3, 2)  # Передаем числа напрямую
print(result)  # Выведет: (1, 3, 2)

# Если я хочу передать именнованны значения
def adder(*args, **kwargs): 
    return args, kwargs 


result = adder(1, 3, 2, name="Carol", age="32")  # Передаем напрямую
print(result)  # Выведет: ((1, 3, 2), {'name': 'Carol', 'age': '32'})

# Область видимых переменных

def greet(name= 'гость'): #переменная name работает только толкь в нутри функции greet (так, как названа)
    age = 25  #age = 25 равна ТОЛЬКО ВНУТРИ этой функции (greet). Она называется ЛОКАЛЬНОЙ ПЕРЕМЕННОЙ
   # Делаем ВЫВОД: переменные объявленные внутри функций, доступна ТОЛЬКО ВНУТРИ этой функции, в которой её объявили
    return f'Hellow, {name}'


result = greet('Carol') # ГЛОБЫЛЬНЫЕ переменные (функция result является глобальной переменной)
# ГЛОБЫЛЬНЫЕ переменные это переменные оъявленные ВНЕ ФУНКЦИЙ и которые доступны внутри ЛЮБЫХ ДРУГИХ функциях
print (result) 

# АНОНИМНЫЕ ФУНКЦИИ или ЛЯМДА функции (определяются с помощью клучегого слува lambda)
def square(x):
    return x * x

square_var = lambda x: x * x
print(square(5))
print(square_var(10))



# 
def outer_function(x):
    def inner_function(y):
        return y * y
    return inner_function(x)

print(outer_function(3))

# ДЕКОРАТОРЫ #декоратор это функция, котораяприниает принимает в себя другую функцию
# в качестве аргкумента и возвращает новую
import time 

def timer(func):
    def wrapper():
        start_time  = time.time() #записываем начало
        func()
        end_time = time.time() # время когда закончили
        print(f'Вермени ушдо {end_time-start_time}')
    return wrapper

@timer
def slow_func1():  # пусть функция выполняет ддоооллллгггооо что-либо и я хочу узнать, как долго
    # для этого импортируем import time для того чтобы узнать точное время выполнения 
    for i in range(999999):
        pass
    print('done')


@timer      
def slow_func2():
    for i in range(9999995):
        pass
    print('done')

@timer
def slow_func3():
    for i in range(9999994):
        pass
    print('done')


slow_func1()
slow_func2()
slow_func3()