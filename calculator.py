#calculator

while True:
    a, b = int(input("Введите первое число ? ")) , int(input("Введите первое число ? "))
    command = input("Введите команду ? ")
    match command:
        case "+":
            print(f'{a+b}')
        case "-":
            print(f'{a-b}')
        case "*":
            print(f'{a*b}')
        case "/":
            if b != 0:
                print(f"Результат: {a / b}")
            else:
                print("Ошибка: деление на ноль")
        case "//":
            print(f'{a//b}')
        case _:
            print(f'Задайте другую команду! ')