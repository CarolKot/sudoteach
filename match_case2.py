day = input('Введите день недели ')
while True:
    day = input('Введите день недели ')
    match day:
        case "1":
            print("Понедельник")
        case "2":
            print("Вторник")
        case "3":
            print("Среда")
        case _:
            print("Такой команды нет! ")
            break
    




