# https://www.youtube.com/watch?v=Ql1tPKMqILA&list=PLV0FNhq3XMOJSj0TfDdHxgIKDKlTwSpmg&index=6
# math case используется для сопоставления значений.

command = input("Ведите команду ")

match command:
    case "start":
        print("Запуск")
    case "stop":
        print("Остановка")
    case _: # _ означает else
        print("Неизвестная команда")