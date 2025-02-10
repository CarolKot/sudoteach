#def

# def greet(name= 'гость'): # = гость  это функция с параметром поумолчанию
#     return f'Hellow, {name}' # Функция может возвращать результат с
#     # с помощью ключегого слова  return
# result = greet('Carol')
# print (result)

# def adder(x, y):
#     return x * y
# result = adder(5, 5) # передаём в result значения 
# print(result)

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